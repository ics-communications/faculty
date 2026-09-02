# -*- coding: utf-8 -*-
"""Extract structured faculty content from the Google Sites export."""
import json, os, re, glob
import lxml.html as LH
from lxml import etree

SRC = os.path.join(os.path.dirname(__file__), '..', 'info', 'Faculty-Page')
OUT = os.path.join(os.path.dirname(__file__), 'content.json')

BLOCK = {'h1', 'h2', 'h3', 'h4', 'p', 'ul', 'ol', 'blockquote', 'table'}
FOOTER_MARK = 'h.49f59de6304e4cd8_4'


def norm(s):
    return re.sub(r'\s+', ' ', (s or '')).strip()


def inline_html(el, drop_leading_img=True):
    """Serialize an element's children to clean inline HTML."""
    parts = []

    def walk(node, italic=False, bold=False):
        for child in node:
            tag = child.tag
            if not isinstance(tag, str):
                continue
            style = (child.get('style') or '').lower()
            it = italic or 'italic' in style
            bo = bold or bool(re.search(r'font-weight:\s*(700|bold)', style))
            if tag == 'a':
                href = child.get('href', '')
                txt = render(child, it, bo)
                if txt.strip():
                    parts.append('<a href="%s">%s</a>' % (esc_attr(href), txt))
            elif tag == 'br':
                parts.append('<br>')
            elif tag == 'img':
                pass
            else:
                parts.append(render(child, it, bo))
            if child.tail:
                parts.append(esc(child.tail))

    def render(node, italic, bold):
        buf = []
        if node.text:
            buf.append(esc(node.text))
        for child in node:
            tag = child.tag
            if not isinstance(tag, str):
                continue
            style = (child.get('style') or '').lower()
            it = italic or 'italic' in style
            bo = bold or bool(re.search(r'font-weight:\s*(700|bold)', style))
            if tag == 'a':
                inner = render(child, it, bo)
                if inner.strip():
                    buf.append('<a href="%s">%s</a>' % (esc_attr(child.get('href', '')), inner))
            elif tag == 'br':
                buf.append('<br>')
            elif tag in ('img', 'ul', 'ol'):
                pass
            else:
                buf.append(render(child, it, bo))
            if child.tail:
                buf.append(esc(child.tail))
        out = ''.join(buf)
        if not out.strip():
            return out
        if italic:
            out = '<em>%s</em>' % out
        if bold:
            out = '<strong>%s</strong>' % out
        return out

    html = render(el, False, False)
    # collapse adjacent identical tags produced by Google's span soup
    for _ in range(6):
        html = re.sub(r'</em>(\s*)<em>', r'\1', html)
        html = re.sub(r'</strong>(\s*)<strong>', r'\1', html)
        html = re.sub(r'<em>(\s*)</em>', r'\1', html)
        html = re.sub(r'<strong>(\s*)</strong>', r'\1', html)
    html = re.sub(r'[ \t\r\n]+', ' ', html)
    return html.strip()


def esc(s):
    return (s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))


def esc_attr(s):
    return esc(s).replace('"', '&quot;')


def list_html(el):
    """Serialize a list, keeping Google Sites' nested duplicates out of the output."""
    items = []
    for li in el.xpath('./li'):
        subs = li.xpath('./ul|./ol')
        parts = [t for t in (inline_html(p) for p in li.xpath('./p')) if t]
        if not parts:
            t = inline_html(li)          # skips ul/ol subtrees
            if t:
                parts = [t]
        body = ' '.join(parts) + ''.join(list_html(s) for s in subs)
        if body.strip():
            items.append('<li>%s</li>' % body)
    if not items:
        return ''
    # A wrapper list holding one item that is itself only a list adds a level of
    # indent and nothing else — unwrap it.
    if len(items) == 1:
        inner = items[0][4:-5].strip()
        if inner.startswith(('<ul>', '<ol>')) and inner.endswith(('</ul>', '</ol>')):
            return inner
    return '<%s>%s</%s>' % (el.tag, ''.join(items), el.tag)


def blocks_of(path):
    tree = LH.parse(path).getroot()
    h1s = tree.xpath('//h1')
    if not h1s:
        return None, []
    h1 = h1s[0]
    stops = tree.xpath("//section[@id='%s']" % FOOTER_MARK)
    stop = stops[0] if stops else None
    started = False
    skip_until = None
    out = []
    for el in tree.iter():
        if el is h1:
            started = True
        if stop is not None and el is stop:
            break
        if not started:
            continue
        if skip_until is not None:
            anc = el
            inside = False
            while anc is not None:
                if anc is skip_until:
                    inside = True
                    break
                anc = anc.getparent()
            if inside:
                continue
            skip_until = None
        if not isinstance(el.tag, str):
            continue
        if el.tag in ('ul', 'ol'):
            out.append(('list', list_html(el)))
            skip_until = el
        elif el.tag in BLOCK:
            out.append((el.tag, inline_html(el)))
    return norm(h1.text_content()), out


def parse_bio(path):
    name, blocks = blocks_of(path)
    if name is None:
        return None
    rec = {'name': name, 'epigraphs': [], 'title_lines': [],
           'email': None, 'sections': []}

    items = []
    for tag, html in blocks[1:]:
        text = norm(re.sub(r'<[^>]+>', '', html))
        if text or tag == 'list':
            items.append((tag, html, text))

    i = 0
    # 1. consecutive h2s straight after the name are the title / degree block
    while i < len(items) and items[i][0] == 'h2':
        rec['title_lines'].append(items[i][1])
        i += 1
    # 2. contact block: h3 "Contact Me" plus any paragraphs holding an address
    while i < len(items) and items[i][0] != 'h2':
        tag, html, text = items[i]
        m = re.search(r'[\w.\-+]+@[\w.\-]+\.[A-Za-z]{2,}', text)
        if m and rec['email'] is None:
            rec['email'] = m.group(0)
        elif tag == 'p' and 'contact' not in text.lower() and len(text) > 3:
            rec['title_lines'].append(html)
        i += 1
    # 3. everything from here on is h2-delimited content
    cur = None
    for tag, html, text in items[i:]:
        if tag == 'h2':
            cur = {'heading': html, 'heading_text': text, 'blocks': []}
            rec['sections'].append(cur)
        elif cur is not None:
            cur['blocks'].append({'t': tag, 'h': html})

    # 4. lift the epigraph section out — it may hold several quote/attribution pairs
    keep = []
    for s in rec['sections']:
        if s['heading_text'].lower().startswith('something worth considering'):
            pairs, body = [], []
            for b in s['blocks']:
                text = norm(re.sub(r'<[^>]+>', '', b['h']))
                if not text:
                    continue
                if re.match(r'^\s*[\u2014\u2013-]\s*\S', text):
                    pairs.append({'quote': body, 'attr': b['h']})
                    body = []
                else:
                    body.append(b['h'])
            if body:
                pairs.append({'quote': body, 'attr': None})
            rec['epigraphs'] = [p for p in pairs if p['quote']]
        elif s['blocks']:
            keep.append(s)
    rec['sections'] = keep
    return rec


def headshot_for(stem):
    d = os.path.join(SRC, stem + '_files')
    for cand in ['unnamed(1).png', 'unnamed(1).jpg']:
        p = os.path.join(d, cand)
        if os.path.exists(p):
            return p
    return None


def main():
    data = {'bios': {}}
    for path in sorted(glob.glob(os.path.join(SRC, 'Our Faculty - *.html'))):
        stem = os.path.splitext(os.path.basename(path))[0]
        label = stem.replace('Our Faculty - ', '')
        if label in ('Adjuncts', 'Emeriti', 'Sessionals'):
            continue
        rec = parse_bio(path)
        if rec is None:
            continue
        rec['source'] = label
        rec['headshot'] = headshot_for(stem)
        data['bios'][label] = rec
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
    for k, v in data['bios'].items():
        print('%-28s email=%-28s sections=%s' % (
            k, v['email'], [s['heading_text'] for s in v['sections']]))


main()
