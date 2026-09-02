# -*- coding: utf-8 -*-
"""Crop, resize and optimize headshots out of the Google Sites export."""
import json, os, re
from PIL import Image, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'assets', 'headshots')
SIZE = 800

SLUGS = {
    'Nik Ansell': 'nik-ansell', 'Neal DeRoo': 'neal-deroo',
    'Ronald A. Kuipers': 'ronald-kuipers', 'Rebekah Smick': 'rebekah-smick',
    'Gideon Strauss': 'gideon-strauss', 'Edith van der Boom': 'edith-van-der-boom',
    'Doug Blomberg': 'doug-blomberg', 'Hendrik Hart': 'hendrik-hart',
    'James Olthuis': 'james-olthuis', 'Calvin Seerveld': 'calvin-seerveld',
    'Bob Sweetman': 'robert-sweetman', 'Lambert Zuidervaart': 'lambert-zuidervaart',
    'Jonathan Chaplin': 'jonathan-chaplin',
    'Adrienne Dengerink Chaplin': 'adrienne-dengerink-chaplin',
    'Sylvia Keesmaat': 'sylvia-keesmaat', 'Dean Dettloff': 'dean-dettloff',
}


def square(im, size=SIZE):
    im = ImageOps.exif_transpose(im)
    if im.mode in ('RGBA', 'LA', 'P'):
        im = im.convert('RGBA')
        bg = Image.new('RGB', im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[-1])
        im = bg
    else:
        im = im.convert('RGB')
    w, h = im.size
    s = min(w, h)
    # bias the crop upward so faces sit in the frame
    left = (w - s) // 2
    top = int((h - s) * 0.32)
    im = im.crop((left, top, left + s, top + s))
    if im.width > size:
        im = im.resize((size, size), Image.LANCZOS)
    return im


def save(im, slug):
    p = os.path.join(OUT, slug + '.jpg')
    im.save(p, 'JPEG', quality=84, optimize=True, progressive=True)
    return p


if __name__ == '__main__':
    data = json.load(open(os.path.join(ROOT, 'build', 'content.json'), encoding='utf-8'))
    for name, rec in data['bios'].items():
        slug = SLUGS.get(name)
        src = rec.get('headshot')
        if not slug or not src:
            print('SKIP', name, src)
            continue
        src = os.path.normpath(os.path.join(ROOT, 'build', src))
        im = Image.open(src)
        w0, h0 = im.size
        p = save(square(im), slug)
        print('%-28s %sx%s -> %s (%.0f KB)' % (name, w0, h0, os.path.basename(p),
                                               os.path.getsize(p) / 1024))
