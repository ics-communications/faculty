# -*- coding: utf-8 -*-
"""Generate every page of faculty.icscanada.edu from content.json + roster.py."""
import json, os, re, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import roster as R
import patches

CONTENT = patches.apply(
    json.load(open(os.path.join(HERE, 'content.json'), encoding='utf-8'))['bios'])

FONTS = ('https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@'
         '0,400;0,700;1,400&family=Outfit:wght@300;400;500;600;700&display=swap')


def rel(depth):
    return '../' * depth if depth else ''


# ── Masthead ────────────────────────────────────────────────────────────────
NAV = [
    ('faculty', 'Faculty', '', [
        ('Senior Members', '#senior-members'),
        ('Cross-Appointed', '#cross-appointed'),
    ]),
    ('emeriti', 'Emeriti', R.STANDING_PATH['emeriti'], None),
    ('adjuncts', 'Adjuncts', R.STANDING_PATH['adjuncts'], None),
    ('sessionals', 'Sessionals', R.STANDING_PATH['sessionals'], None),
    ('ics', 'ICS', None, [
        ('ICS Home', 'https://www.icscanada.edu/'),
        ('Programs', 'https://www.icscanada.edu/academics'),
        ('Courses &amp; Syllabi', 'https://www.icscanada.edu/academics/courses-and-syllabi'),
        ('Admissions', 'https://www.icscanada.edu/admissions'),
        ('Research (CPRSE)', 'https://www.icscanada.edu/research'),
        ('Critical Faith Podcast', 'https://www.icscanada.edu/critical-faith-podcast'),
    ]),
]


def header(active, depth):
    r = rel(depth)
    items, mob = [], []
    for key, label, href, sub in NAV:
        is_active = (key == active)
        cls = ' ics-nav__item--active' if is_active else ''
        if sub is None:
            items.append(
                '        <li class="ics-nav__item%s">\n'
                '          <a class="ics-nav__link" href="%s%s"%s>%s</a>\n'
                '        </li>' % (cls, r, href, ' aria-current="page"' if is_active else '', label))
            mob.append('  <a class="ics-mobile-menu__link%s" href="%s%s"%s>%s</a>' % (
                ' ics-mobile-menu__link--current' if is_active else '', r, href,
                ' aria-current="page"' if is_active else '', label))
        else:
            links = []
            mlinks = []
            for slabel, shref in sub:
                if shref.startswith('http'):
                    full = shref
                elif key != 'faculty':
                    full = r + shref
                elif depth or active != 'faculty':
                    # a same-page anchor only resolves on the faculty index itself
                    full = r + 'index.html' + shref
                else:
                    full = shref
                ext = ' target="_blank" rel="noopener"' if shref.startswith('http') else ''
                links.append('            <a class="ics-dropdown__link" href="%s"%s>%s</a>'
                             % (full, ext, slabel))
                mlinks.append('      <a href="%s"%s>%s</a>' % (full, ext, slabel))
            items.append(
                '        <li class="ics-nav__item%s">\n'
                '          <button class="ics-nav__link" aria-expanded="false" aria-haspopup="true">'
                '%s<span class="ics-nav__caret"></span></button>\n'
                '          <div class="ics-dropdown">\n%s\n          </div>\n'
                '        </li>' % (cls, label, '\n'.join(links)))
            mob.append('  <div class="ics-mobile-menu__group">\n'
                       '    <span class="ics-mobile-menu__link">%s</span>\n'
                       '    <div class="ics-mobile-menu__sub">\n%s\n    </div>\n  </div>'
                       % (label, '\n'.join(mlinks)))

    return '''<header class="ics-header">
  <div class="ics-header__inner">
    <a class="ics-header__logo-link" href="https://www.icscanada.edu/">
      <img class="ics-header__logo-img" src="%sassets/logos/ics-logo-white-red.png"
           alt="Institute for Christian Studies" width="900" height="160">
    </a>

    <nav aria-label="Main navigation">
      <ul class="ics-nav">
%s
      </ul>
    </nav>

    <button class="ics-burger" aria-label="Open menu" type="button">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>

<div class="ics-mobile-menu" id="mobileMenu">
  <button class="ics-mobile-menu__close" aria-label="Close menu" type="button">&times;</button>
%s
</div>''' % (r, '\n'.join(items), '\n'.join(mob))


# ── Footer — copied verbatim from the ICS main site ─────────────────────────
FOOTER = '''<footer class="site-footer">
  <div class="footer__grid">
    <div>
      <div class="footer__brand">Institute for Christian Studies</div>
      <p class="footer__desc">Graduate education, research, and community service in the Reformational tradition since 1967. Forming the next generation of Christian scholars.</p>
      <address class="footer__address">
        59 St. George Street<br>Toronto, Ontario M5S 2E6<br>Canada<br><br>
        1-416-979-2331<br>
        <a id="footer-email" style="color:var(--accent-light)"></a>
      </address>
    </div>
    <div>
      <h4 class="footer__heading">Programs</h4>
      <ul class="footer__links">
        <li><a href="https://www.icscanada.edu/academics/phd-program">PhD in Philosophy</a></li>
        <li><a href="https://www.icscanada.edu/academics/master-of-arts-in-philosophy">MA in Philosophy</a></li>
        <li><a href="https://education.icscanada.edu/mael">MA(Phil) Ed. Leadership</a></li>
        <li><a href="https://education.icscanada.edu/mwse">MWS in Education (MWS-E)</a></li>
        <li><a href="https://www.icscanada.edu/academics/master-of-worldview-studies">Master of Worldview Studies</a></li>
        <li><a href="https://www.icscanada.edu/academics/courses-and-syllabi">Courses &amp; Syllabi</a></li>
        <li><a href="https://f2bf.icscanada.edu">Free to be Faithful</a></li>
      </ul>
    </div>
    <div>
      <h4 class="footer__heading">Admissions</h4>
      <ul class="footer__links">
        <li><a href="https://www.icscanada.edu/admissions">Prospective Students</a></li>
        <li><a href="https://www.icscanada.edu/admissions/admission-requirements-modes-of-study">Requirements &amp; Modes</a></li>
        <li><a href="https://www.icscanada.edu/admissions/financial-aid">Financial Aid</a></li>
        <li><a href="https://www.icscanada.edu/admissions/tuition-fees">Tuition &amp; Fees</a></li>
        <li><a href="https://www.icscanada.edu/admissions/international-students">International Students</a></li>
        <li><a href="https://www.icscanada.edu/faq">FAQ</a></li>
      </ul>
    </div>
    <div>
      <h4 class="footer__heading">Connect</h4>
      <ul class="footer__links">
        <li><a href="https://www.icscanada.edu/about/our-story">Our Story</a></li>
        <li><a href="https://www.icscanada.edu/about/mission-educational-creed">Mission &amp; Creed</a></li>
        <li><a href="https://faculty.icscanada.edu/">Faculty</a></li>
        <li><a href="https://www.icscanada.edu/research">Research (CPRSE)</a></li>
        <li><a href="https://www.icscanada.edu/events">Events</a></li>
        <li><a href="https://www.icscanada.edu/critical-faith-podcast">Critical Faith Podcast</a></li>
        <li><a href="https://perspective.icscanada.edu/">Perspective Newsletter</a></li>
        <li><a href="https://www.icscanada.edu/about/become-a-member">Become a Member</a></li>
        <li><a href="https://www.icscanada.edu/donate">Donate</a></li>
      </ul>
    </div>
  </div>
  <div class="footer__bottom">
    <span>&copy; 2026 Institute for Christian Studies &middot;
      <a href="https://www.icscanada.edu/about/privacy-policy" style="color:inherit">Privacy</a> &middot;
      <a href="https://www.icscanada.edu/about/accessibility-policy" style="color:inherit">Accessibility</a>
    </span>
    <div class="footer__social">
      <a href="https://www.facebook.com/instituteforchristianstudies" aria-label="Facebook" title="Facebook">f</a>
      <a href="https://twitter.com/InsChr" aria-label="X" title="X / Twitter">&#x1D54F;</a>
      <a href="https://www.instagram.com/instituteforchristianstudies/" aria-label="Instagram" title="Instagram">ig</a>
      <a href="https://www.linkedin.com/school/icscanada" aria-label="LinkedIn" title="LinkedIn">in</a>
      <a href="https://www.youtube.com/user/ChristianStudies" aria-label="YouTube" title="YouTube">&#x25B6;</a>
      <a href="https://instituteforchristianstudies.substack.com" aria-label="Substack" title="Substack" class="social-substack">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
          <path d="M22.539 8.242H1.46V5.406h21.08v2.836zM1.46 10.812V24l9.54-5.58L20.54 24V10.812H1.46zM22.54 0H1.46v2.836h21.08V0z"/>
        </svg>
      </a>
    </div>
  </div>
</footer>'''


# The card image scrapers show for any page on the site; without it they
# grab whichever headshot happens to come first in the roster.
OG_IMAGE = R.SITE + '/assets/headshots/neal-deroo.jpg'


def page(title, description, body, active, depth, canonical, image=None):
    r = rel(depth)
    return '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<link rel="canonical" href="%s">
<meta property="og:site_name" content="Institute for Christian Studies">
<meta property="og:title" content="%s">
<meta property="og:description" content="%s">
<meta property="og:type" content="website">
<meta property="og:url" content="%s">
<meta property="og:image" content="%s">
<meta property="og:image:width" content="800">
<meta property="og:image:height" content="800">
<meta property="og:image:alt" content="Institute for Christian Studies faculty">
<meta name="twitter:card" content="summary">
<link rel="icon" href="%sassets/logos/ics-favicon.png" type="image/png">
<link rel="apple-touch-icon" href="%sassets/logos/ics-favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="%s">
<link rel="stylesheet" href="%scss/styles.css">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
%s

<main id="main">
%s
</main>

%s
<script src="%sjs/site.js"></script>
</body>
</html>
''' % (title, description, canonical, title, description, canonical, image or OG_IMAGE, r, r, FONTS, r,
       header(active, depth), body, FOOTER, r)


DEGREE_LINE = re.compile(
    r'\b(BA|BSc|MA|MAS|MPhil|MPhilF|MEd|MDiv|MSc|PhD|DPhil|ThD|LLB)\b[^.]{0,60}\(')


def clean_heading(h):
    """Google Sites wraps headings in bold spans; the stylesheet owns the weight."""
    h = re.sub(r'^\s*<strong>(.*)</strong>\s*$', r'\1', h.strip())
    return re.sub(r'^\s*<strong>(.*)</strong>\s*$', r'\1', h.strip())


def nav_label(h):
    """Index labels carry no markup — some headings are themselves links, and an
    anchor inside an anchor is un-nested by the parser into an empty control."""
    return re.sub(r'</?a\b[^>]*>', '', clean_heading(h))


def trim_biography(blocks):
    """Drop the name / title / degree stack that repeats the page masthead.

    Stops at the first paragraph naming degree-granting institutions, or at the
    first paragraph of real prose, so nothing substantive can be eaten.
    """
    i = 0
    while i < len(blocks) and i < 5:
        b = blocks[i]
        if b['t'] != 'p':
            break
        text = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', b['h'])).strip()
        if len(text) > 120 or DEGREE_LINE.search(text):
            break
        i += 1
    return blocks[i:] if i else blocks



# ── Register entries ────────────────────────────────────────────────────────
_FIRST = {'n': 0}


def portrait(p, depth, link=None, cls='entry__figure'):
    r = rel(depth)
    src = 'assets/headshots/%s.jpg' % p['slug']
    if os.path.exists(os.path.join(ROOT, src)):
        _FIRST['n'] += 1
        loading = 'eager" fetchpriority="high' if _FIRST['n'] <= 2 else 'lazy'
        small = 'assets/headshots/%s-400.jpg' % p['slug']
        srcset = ''
        if os.path.exists(os.path.join(ROOT, small)):
            sizes = ('(max-width: 700px) 116px, 168px' if cls == 'bio__portrait'
                     else '(max-width: 700px) 76px, (max-width: 900px) 96px, 132px')
            srcset = (' srcset="%s%s 400w, %s%s 800w" sizes="%s"'
                      % (r, small, r, src, sizes))
        inner = ('<img src="%s%s"%s alt="%s" width="800" height="800" loading="%s" '
                 'decoding="async">' % (r, src, srcset, p['name'], loading))
        tag = 'a' if link else 'div'
        attrs = (' class="%s" href="%s" tabindex="-1" aria-hidden="true"' % (cls, link)
                 if link else ' class="%s"' % cls)
        return '<%s%s>%s</%s>' % (tag, attrs, inner, tag)
    initials = ''.join(w[0] for w in p['name'].split()[:2])
    return '<div class="%s %s--placeholder" aria-hidden="true">%s</div>' % (cls, cls, initials)


def line_html(p, rec):
    """The right-hand column: the scholar's chosen epigraph, or a précis."""
    pairs = epigraphs(rec)
    if pairs:
        first = pairs[0]
        quote, _ = shorten(typographic(' '.join(first['quote'])))
        attr = typographic(first.get('attr') or '')
        return ('<blockquote class="epigraph">%s%s</blockquote>'
                % (quote,
                   '<cite class="epigraph__attr">%s</cite>' % attr if attr else ''))
    if p.get('precis'):
        return '<p class="precis">%s</p>' % p['precis']
    if rec:
        for s in rec['sections']:
            for b in s['blocks']:
                if b['t'] == 'p':
                    txt = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', b['h'])).strip()
                    if len(txt) > 90:
                        short, _ = shorten(b['h'], soft=55, hard=270)
                        return '<p class="precis">%s</p>' % short
    return ''


def epigraphs(rec):
    """Attributed pairs only — an unattributed trailing block is a caption, not an epigraph."""
    pairs = (rec or {}).get('epigraphs') or []
    attributed = [p for p in pairs if p.get('attr')]
    return attributed or pairs


def typographic(html):
    """Normalise quotation marks in the epigraphs.

    The old site mixes straight and curly marks, sometimes within one quotation.
    These run at reading size in the site's most exposed column, so they get set
    properly: alternating curly doubles, curly singles, and a real apostrophe
    between letters. Tags are stepped over, never rewritten.
    """
    out = []
    i = 0
    dbl_open = True
    sgl_open = True
    while i < len(html):
        ch = html[i]
        if ch == '<':
            j = html.index('>', i) + 1
            out.append(html[i:j])
            i = j
            continue
        if ch == '&':                       # step over an entity intact
            m = re.match(r'&[#0-9A-Za-z]{1,8};', html[i:])
            if m:
                out.append(m.group(0))
                i += len(m.group(0))
                continue
        if ch == '\u201c':
            dbl_open = False
        elif ch == '\u201d':
            dbl_open = True
        elif ch == '"':
            ch = '\u201c' if dbl_open else '\u201d'
            dbl_open = not dbl_open
        elif ch == "'":
            prev = html[i - 1] if i else ''
            nxt = html[i + 1] if i + 1 < len(html) else ''
            if prev.isalpha() and nxt.isalpha():
                ch = '\u2019'              # apostrophe
            else:
                ch = '\u2018' if sgl_open else '\u2019'
                sgl_open = not sgl_open
        out.append(ch)
        i += 1
    return ''.join(out)


ABBREV = {'dr', 'mr', 'mrs', 'ms', 'prof', 'st', 'ed', 'eds', 'vol', 'no', 'pp', 'ch',
          'cf', 'etc', 'trans', 'rev', 'jr', 'sr', 'univ'}


def sentence_end(out):
    """True when the period just written really ends a sentence.

    Guards the two things that trip a naive cut: initials (N.T. Wright, J. Aaron
    Simmons) and the handful of abbreviations that show up in academic prose.
    """
    word = ''
    for ch in reversed(out[:-1]):
        if ch.isalpha():
            word = ch + word
        else:
            break
    if len(word) == 1:
        return False
    return word.lower() not in ABBREV


def shorten(html, soft=150, hard=250):
    """Trim an epigraph to its opening thought, keeping inline markup balanced.

    The full quotation stays on the scholar's own page; the register shows the
    opening so the column reads at a glance.
    """
    plain = re.sub(r'<[^>]+>', '', html)
    if len(plain) <= hard + 40:
        return html, False

    out, stack, count, i, cut = [], [], 0, 0, None
    while i < len(html):
        if html[i] == '<':
            j = html.index('>', i) + 1
            tag = html[i:j]
            m = re.match(r'</?([a-zA-Z0-9]+)', tag)
            if m:
                if tag.startswith('</'):
                    if stack and stack[-1] == m.group(1):
                        stack.pop()
                elif not tag.endswith('/>') and m.group(1) not in ('br',):
                    stack.append(m.group(1))
            out.append(tag)
            i = j
            continue
        ch = html[i]
        out.append(ch)
        count += 1
        i += 1
        if count >= soft and ''.join(out[-5:]) in ('. . .', '.\u2009.\u2009.'):
            cut = len(out)          # a spaced ellipsis is itself a clean stopping point
            break
        if (count >= soft and ch in '.?!' and out[-2:-1] != [' ']
                and (i >= len(html) or html[i] in ' <\u201d"\'')
                and html[i:i + 2] not in (' .', ' \u2026')
                and (ch != '.' or sentence_end(out))):
            cut = len(out)
            break
        if count >= hard:
            while out and out[-1] not in (' ',):
                out.pop()
            cut = len(out)
            break
    body = ''.join(out[:cut] if cut else out).rstrip()
    # A quotation cut short has to say so, and has to close.
    opener = plain.lstrip()[:1]
    close = {'"': '"', '\u201c': '\u201d', '\u2018': '\u2019'}.get(opener, '')
    trail = re.search(r'(?:\.[ \u2009\u00a0]*){2,}$|\u2026$', body)
    if trail:
        body = body[:trail.start()].rstrip() + '\u2026'   # one convention, not three
    elif body.endswith(('.', '?', '!')):
        body = body[:-1] + '\u2026'
    else:
        body += '\u2009\u2026'
    body += close
    for t in reversed(stack):
        body += '</%s>' % t
    return body, True



def entry_html(p, depth, level=3):
    rec = CONTENT.get(p.get('source') or '')
    has_page = bool(rec) or bool(p.get('bio'))
    href = rel(depth) + R.href(p)
    dagger = ('<span class="entry__dagger" aria-hidden="true">†</span>'
              '<span class="sr-only"> (deceased)</span>') if p.get('deceased') else ''

    name = ('<a href="%s">%s</a>%s' % (href, p['name'], dagger)) if has_page \
        else p['name'] + dagger

    meta = ['<h%d class="entry__name">%s</h%d>' % (level, name, level)]
    meta.append('<p class="entry__degrees">%s</p>' % p['degrees'])
    lines = []
    if p['standing'] == 'faculty':
        lines = list(p.get('titles') or []) or ([p['field']] if p.get('field') else [])
    else:
        # outside the salaried faculty the field is the identifying fact, not the rank
        if p.get('field'):
            lines.append(p['field'])
        lines += [t for t in (p.get('titles') or []) if t != p.get('field')]
    if lines:
        meta.append('<ul class="entry__titles">%s</ul>'
                    % ''.join('<li>%s</li>' % clean_heading(t) for t in lines))
    gutter = [portrait(p, depth, href if has_page else None)]
    if p.get('years'):
        cls = ' entry__years--tbc' if p.get('years_tbc') else ''
        gutter.append('<p class="entry__years%s">%s</p>' % (cls, p['years']))

    line = line_html(p, rec)
    if has_page:
        line += '<a class="entry__more" href="%s">Full profile</a>' % href
    elif p.get('external'):
        line += ('<a class="entry__more" href="%s" target="_blank" rel="noopener">%s</a>'
                 % (p['external'], p.get('external_label', 'Profile')))

    return '''      <article class="entry">
        <div class="entry__gutter">
%s
        </div>
        <div class="entry__meta">
%s
        </div>
        <div class="entry__line">
%s
        </div>
      </article>''' % ('\n'.join('          ' + x for x in gutter),
                       '\n'.join('          ' + m for m in meta),
                       '\n'.join('          ' + l for l in line.split('\n') if l))


def standings_nav(current, depth):
    r = rel(depth)
    out = []
    for key, label, _title, _lede in R.STANDINGS:
        href = r + R.STANDING_PATH[key]
        cur = ' standings__item--current' if key == current else ''
        aria = ' aria-current="page"' if key == current else ''
        out.append('    <li class="standings__item%s"><a class="standings__link" href="%s"%s>%s</a></li>'
                   % (cur, href, aria, label))
    return '  <ul class="standings">\n%s\n  </ul>' % '\n'.join(out)


def elsewhere(current, depth):
    r = rel(depth)
    counts = {k: len(R.of(k)) for k, _, _, _ in R.STANDINGS}
    items = []
    for key, label, title, lede in R.STANDINGS:
        if key == current:
            continue
        href = r + R.STANDING_PATH[key]
        items.append('      <li><a href="%s">%s<span>%d %s</span></a></li>'
                     % (href, title, counts[key],
                        'scholar' if counts[key] == 1 else 'scholars'))
    return '''<section class="elsewhere">
  <div class="container">
    <h2 class="elsewhere__title">More ICS Faculty</h2>
    <ul class="elsewhere__list">
%s
    </ul>
  </div>
</section>''' % '\n'.join(items)


# ── Index pages ─────────────────────────────────────────────────────────────
def start_year(p):
    m = re.match(r'(\d{4})', p.get('years') or '')
    return int(m.group(1)) if m else 9999


def index_page(key, label, title, lede, depth):
    people = R.of(key)
    if key == 'emeriti':
        # The years are this page's spine — read it as the history it is.
        people = sorted(people, key=start_year)
    groups = []
    seen = []
    for p in people:
        g = p.get('group')
        if g not in seen:
            seen.append(g)
        groups.append(g)

    body = []
    for g in seen:
        members = [p for p in people if p.get('group') == g]
        if g:
            anchor = re.sub(r'[^a-z]+', '-', g.lower()).strip('-')
            if 'senior' in anchor:
                anchor = 'senior-members'
            elif 'cross' in anchor:
                anchor = 'cross-appointed'
            body.append('      <div class="register__group-head" id="%s">\n'
                        '        <h2 class="register__group-title">%s</h2>\n'
                        '        <span class="register__group-rule"></span>\n'
                        '      </div>' % (anchor, g))
        for p in members:
            body.append(entry_html(p, depth, 3 if seen != [None] else 2))

    note = ''
    if any(p.get('deceased') for p in people):
        note = ('\n    <p class="standings__note"><span>†</span> '
                'indicates a member who has died.</p>')
    census = ''
    if key in R.CENSUS:
        top, sub = R.CENSUS[key]
        census = ('\n      <p class="opening__census"><strong>%s</strong>%s</p>'
                  % (top, sub or ''))
    main = '''<div class="container">
  <div class="opening">
    <div class="opening__head">
      <p class="opening__kicker">Institute for Christian Studies</p>
      <h1 class="opening__title">%s</h1>%s
    </div>
%s%s
  </div>

  <div class="register%s">
%s
  </div>
</div>

%s''' % (title, census, standings_nav(key, depth), note,
         ' register--sparse' if len(people) <= 3 else '', '\n'.join(body),
         elsewhere(key, depth))

    canonical = R.SITE + '/' + R.STANDING_PATH[key]
    return page('%s — Institute for Christian Studies' % title,
                lede, main, key, depth, canonical)


# ── Bio pages ───────────────────────────────────────────────────────────────
def anchor_for(text):
    a = re.sub(r'<[^>]+>', '', text)
    a = re.sub(r'&[a-z]+;', ' ', a)
    a = re.sub(r'[^a-z0-9]+', '-', a.lower()).strip('-')
    return a or 'section'


def blocks_html(blocks, section_anchor=None):
    """Render a section's blocks, and return any sub-headings worth indexing."""
    out, subs, seen = [], [], set()
    for b in blocks:
        if b['t'] == 'list':
            out.append(b['h'])
        elif b['t'] == 'h3':
            label = nav_label(b['h'])
            if section_anchor and label:
                a = '%s-%s' % (section_anchor, anchor_for(label))
                n = 2
                while a in seen:
                    a, n = '%s-%s-%d' % (section_anchor, anchor_for(label), n), n + 1
                seen.add(a)
                subs.append((label, a))
                out.append('<h3 id="%s">%s</h3>' % (a, clean_heading(b['h'])))
            else:
                out.append('<h3>%s</h3>' % clean_heading(b['h']))
        else:
            out.append('<p>%s</p>' % b['h'])
    return '\n'.join(out), subs


LIST_SECTIONS = ('publication', 'books', 'lecture', 'archive', 'file', 'video',
                 'perspective', 'my books')


def bio_page(p):
    depth = 1
    r = rel(depth)
    rec = CONTENT.get(p.get('source') or '')
    standing_key = p['standing']
    standing = dict((k, (l, t, d)) for k, l, t, d in
                    [(a, b, c, e) for a, b, c, e in R.STANDINGS])[standing_key]
    parent_href = r + R.STANDING_PATH[standing_key]

    titles = p.get('titles') or []
    if not titles and rec and rec.get('title_lines'):
        titles = [t for t in rec['title_lines']
                  if not re.match(r'^\s*<?[a-z]*>?\s*(PhD|MA|MPhil|DPhil|BA|MEd|MAS)',
                                  re.sub(r'<[^>]+>', '', t))]
    if not titles and p.get('field'):
        titles = [p['field']]

    email = rec.get('email') if rec else None
    if p.get('deceased'):
        email = None

    # ── head ──
    head = ['      <div class="bio__head">',
            '        ' + portrait(p, depth, None, 'bio__portrait'),
            '        <div>',
            '          <h1 class="bio__name">%s%s</h1>' % (
                p['name'],
                ' <span class="entry__dagger" title="deceased">†</span>'
                if p.get('deceased') else ''),
            '          <p class="bio__degrees">%s</p>' % p['degrees']]
    if titles:
        head.append('          <ul class="bio__titles">%s</ul>'
                    % ''.join('<li>%s</li>' % clean_heading(t) for t in titles))
    if email:
        head.append('          <a class="bio__contact" href="mailto:%s">%s</a>' % (email, email))
    head += ['        </div>', '      </div>']

    # A page made only of resource links gets the register's line as an opening note.
    has_prose = any(s['heading_text'].lower().startswith(('about', 'biography'))
                    for s in (rec['sections'] if rec else []))
    if p.get('precis') and not has_prose and rec:
        head.append('      <p class="bio__lede">%s</p>' % p['precis'])

    # ── sections ──
    sections, index = [], []
    pairs = epigraphs(rec)
    if pairs:
        index.append(('Something Worth Considering', 'epigraph'))
        quotes = []
        for q in pairs:
            body = (''.join('<p>%s</p>' % typographic(b) for b in q['quote'])
                    if len(q['quote']) > 1 else typographic(q['quote'][0]))
            quotes.append('      <blockquote class="epigraph">%s%s</blockquote>' % (
                body,
                '<cite class="epigraph__attr">%s</cite>' % typographic(q['attr'])
                if q.get('attr') else ''))
        sections.append('''    <section class="bio__epigraph" id="epigraph">
      <p class="bio__epigraph-label">Something Worth Considering&hellip;</p>
%s
    </section>''' % '\n'.join(quotes))

    if not rec:
        # People with no ICS page of their own: an authored entry from research
        if p.get('bio'):
            index.append(('Biography', 'biography'))
            sections.append('''    <section class="bio__section" id="biography">
      <h2 class="bio__section-title">Biography</h2>
      <div class="prose"><p>%s</p></div>
    </section>''' % p['bio'])
        if p.get('foci'):
            index.append(('Research Foci', 'research-foci'))
            sections.append('''    <section class="bio__section" id="research-foci">
      <h2 class="bio__section-title">Research Foci</h2>
      <div class="prose"><ul>%s</ul></div>
    </section>''' % ''.join('<li>%s</li>' % f for f in p['foci']))
        if p.get('pubs'):
            pubs_title = p.get('pubs_title', 'Publications')
            index.append((pubs_title, 'publications'))
            sections.append('''    <section class="bio__section" id="publications">
      <h2 class="bio__section-title">%s</h2>
      <div class="prose prose--list"><ul>%s</ul></div>
    </section>''' % (pubs_title, ''.join('<li>%s</li>' % x for x in p['pubs'])))
    else:
        for s in rec['sections']:
            a = anchor_for(s['heading'])
            heading = clean_heading(s['heading'])
            index.append((nav_label(s['heading']), a))
            listish = any(k in s['heading_text'].lower() for k in LIST_SECTIONS)
            cls = 'prose prose--list' if listish else 'prose'
            blocks = s['blocks']
            if s['heading_text'].strip().lower() == 'biography':
                blocks = trim_biography(blocks)
            inner, subs = blocks_html(blocks, a if listish else None)
            if len(subs) > 1:
                index[-1] = (index[-1][0], index[-1][1], subs)
            sections.append('''    <section class="bio__section" id="%s">
      <h2 class="bio__section-title">%s</h2>
      <div class="%s">
%s
      </div>
    </section>''' % (a, heading, cls, inner))

    if p.get('external'):
        sections.append('''    <section class="bio__section">
      <a class="bio__external" href="%s" target="_blank" rel="noopener">%s</a>
    </section>''' % (p['external'], p.get('external_label', 'Profile')))

    index_html = ''
    if len(index) > 2:
        rows = []
        for item in index:
            h, a = item[0], item[1]
            rows.append('        <a href="#%s">%s</a>' % (a, h))
            for label, sa in (item[2] if len(item) > 2 else []):
                rows.append('        <a class="bio__index-sub" href="#%s">%s</a>'
                            % (sa, label))
        index_html = '''    <nav class="bio__index" aria-label="On this page">
      <p class="bio__index-title">On this page</p>
      <div class="bio__index-inner">
%s
      </div>
    </nav>''' % '\n'.join(rows)

    label = standing[0]
    subtitle = re.sub(r'<[^>]+>', '', (titles[0] if titles else p.get('field', '')))
    main = '''<article class="bio">
  <div class="container">
    <div class="bio__masthead">
      <p class="bio__crumb"><a href="%s">%s</a> <span>&nbsp;/&nbsp;</span> %s</p>
%s
    </div>
  </div>

  <div class="container">
    <div class="bio__body">
%s
      <div class="bio__content">
%s
      </div>
    </div>
  </div>
</article>

%s''' % (parent_href, standing[1], p['name'], '\n'.join(head), index_html,
         '\n'.join(sections), elsewhere(standing_key, depth))

    desc = '%s, %s at the Institute for Christian Studies.' % (p['name'], subtitle) \
        if subtitle else '%s at the Institute for Christian Studies.' % p['name']
    shot = 'assets/headshots/%s.jpg' % p['slug']
    og = (R.SITE + '/' + shot) if os.path.exists(os.path.join(ROOT, shot)) else None
    return page('%s — ICS Faculty' % p['name'], desc[:180], main,
                standing_key, depth, '%s/%s' % (R.SITE, R.href(p)), og)


# ── Write ───────────────────────────────────────────────────────────────────
def write(path, html):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w', encoding='utf-8') as f:
        f.write(html)
    return len(html)


def not_found():
    body = '''<div class="container">
  <div class="opening">
    <div class="opening__head">
      <p class="opening__kicker">Institute for Christian Studies</p>
      <h1 class="opening__title">Page not found</h1>
      <p class="opening__lede">That page has moved or never existed. The faculty are all
        listed below.</p>
    </div>
%s
  </div>
</div>

%s''' % (standings_nav(None, 0), elsewhere(None, 0))
    return page('Page not found — ICS Faculty',
                'The page you asked for is not here. Browse the ICS faculty listings instead.',
                body, None, 0, R.SITE + '/404.html')


def sitemap():
    from datetime import date
    today = date.today().isoformat()
    urls = [(R.SITE + '/' + R.STANDING_PATH[k],
             '1.0' if k == 'faculty' else '0.9') for k, _, _, _ in R.STANDINGS]
    urls += [('%s/%s' % (R.SITE, R.href(p)), '0.8') for p in R.PEOPLE
             if p.get('source') or p.get('bio')]
    rows = '\n'.join('  <url><loc>%s</loc><lastmod>%s</lastmod><priority>%s</priority></url>'
                      % (u, today, pr) for u, pr in urls)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s\n</urlset>\n'
            % rows)


def main():
    n = 0
    for key, label, title, lede in R.STANDINGS:
        _FIRST['n'] = 0
        depth = 0 if key == 'faculty' else 1
        out = R.STANDING_PATH[key] + 'index.html'
        size = write(out, index_page(key, label, title, lede, depth))
        print('%-34s %6.1f KB' % (out, size / 1024.0))
        n += 1
    for p in R.PEOPLE:
        if not (p.get('source') or p.get('bio')):
            continue
        _FIRST['n'] = 0
        out = R.href(p) + 'index.html'
        size = write(out, bio_page(p))
        print('%-34s %6.1f KB' % (out, size / 1024.0))
        n += 1
    _FIRST['n'] = 99
    write('404.html', not_found())
    write('sitemap.xml', sitemap())
    write('robots.txt', 'User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n' % R.SITE)
    print('404.html, sitemap.xml, robots.txt')
    print('\n%d pages' % n)


if __name__ == '__main__':
    main()
