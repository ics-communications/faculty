# -*- coding: utf-8 -*-
"""Build square, circle-ready portraits on the ICS cream ground.

Most source headshots are already circle-masked PNGs on white, so a square
output plus a CSS `border-radius:50%` lands exactly on the existing circle.
"""
import os, sys, json
from PIL import Image, ImageOps, ImageFilter, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'assets', 'headshots')
CREAM = (253, 251, 247)
SIZE = 800


def load(src):
    im = ImageOps.exif_transpose(Image.open(src))
    if im.mode in ('RGBA', 'LA', 'P'):
        im = im.convert('RGBA')
        bg = Image.new('RGB', im.size, CREAM)
        bg.paste(im, mask=im.split()[-1])
        return bg
    return im.convert('RGB')


def square(src, top_bias=0.30, size=SIZE):
    im = load(src)
    w, h = im.size
    s = min(w, h)
    left = (w - s) // 2
    top = int(round((h - s) * top_bias))
    im = im.crop((left, top, left + s, top + s))
    return im.resize((size, size), Image.LANCZOS)


def extend(src, head_top, head_bot, head_frac=0.60, size=SIZE):
    """Widen a portrait too tall for a square crop, using its own blurred ground."""
    im = load(src)
    w, h = im.size
    scale = (head_frac * size) / float(head_bot - head_top)
    fg = im.resize((max(1, int(w * scale)), max(1, int(h * scale))), Image.LANCZOS)
    cover = max(size / float(w), size / float(h)) * 1.3
    bg = im.resize((int(w * cover), int(h * cover)), Image.LANCZOS)
    bg = bg.crop(((bg.width - size) // 2, (bg.height - size) // 2,
                  (bg.width - size) // 2 + size, (bg.height - size) // 2 + size))
    bg = bg.filter(ImageFilter.GaussianBlur(38))
    ox = (size - fg.width) // 2
    oy = int(size * 0.16) - int(head_top * scale)
    mask = Image.new('L', fg.size, 0)
    ImageDraw.Draw(mask).rectangle([26, 26, fg.width - 27, fg.height - 27], fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(18))
    bg.paste(fg, (ox, oy), mask)
    return bg


def write(im, slug, q=85):
    p = os.path.join(OUT, slug + '.jpg')
    im.save(p, 'JPEG', quality=q, optimize=True, progressive=True)
    # a 400px variant for the register, where the slot is never wider than 132 CSS px
    small = im.resize((400, 400), Image.LANCZOS) if im.width > 400 else im.copy()
    small.save(os.path.join(OUT, slug + '-400.jpg'), 'JPEG', quality=82,
               optimize=True, progressive=True)
    return p


if __name__ == '__main__':
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from headshots import SLUGS
    SP = sys.argv[1]
    data = json.load(open(os.path.join(ROOT, 'build', 'content.json'), encoding='utf-8'))
    jobs = []
    for name, rec in data['bios'].items():
        if rec.get('headshot'):
            jobs.append((os.path.normpath(os.path.join(ROOT, 'build', rec['headshot'])),
                         SLUGS[name], 0.30))
    jobs += [
        (os.path.join(SP, 'keesmaat-new.jpg'), 'sylvia-keesmaat', 0.10),
        (os.path.join(SP, 'demoor.png'), 'michael-demoor', 0.30),
        (os.path.join(SP, 'dudiak.jpg'), 'jeffrey-dudiak', 0.30),
        (os.path.join(ROOT, 'info/NewerHeadshots/AndrewTebbut.jpg'), 'andrew-tebbutt', 0.25),
        (os.path.join(ROOT, 'info/NewerHeadshots/JacobBenjamins.jpg'), 'jacob-benjamins', 0.25),
    ]
    for src, slug, bias in jobs:
        native = Image.open(src).size
        size = SIZE if min(native) >= 400 else int(min(native) * 1.4)
        p = write(square(src, bias, size), slug)
        print('%-28s %-11s -> %d  %.0f KB' % (slug, '%dx%d' % native, size,
                                              os.path.getsize(p) / 1024))
    dett = os.path.join(SP, 'pt-Screenshot-2026-07-02-at-4.51.48-PM.png')
    p = write(extend(dett, 34, 595, 0.74, 640), 'dean-dettloff')
    print('%-28s %-11s -> %d  %.0f KB (extended)' % ('dean-dettloff', '440x676', 600,
                                                     os.path.getsize(p) / 1024))
