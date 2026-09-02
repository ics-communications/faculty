# -*- coding: utf-8 -*-
"""Edits to the carried-over bio text, requested by the faculty themselves.

Each patch names the person, the section, the block it replaces, and a fragment of
the original so the build fails loudly if the source text ever changes underneath it.
"""

GIDEON_OPENING = (
    'I currently articulate my life-long primal research question as follows: What is good '
    'for humans, taking into consideration what is good for the whole earth? This question '
    'provides the lens through which I ethnographically consider the stories humans tell to '
    'account practically for our actions and critically and appreciatively read theoretical '
    'studies of such stories by philosophers in the Aristotelian, Thomist, Marxist, and '
    'Dooyeweerdian traditions.'
)

GIDEON_CLOSING = (
    'For a little more, see my <a href="https://gideonstrauss.substack.com">Substack</a> '
    'account.'
)

PATCHES = [
    # info/gideon.txt
    dict(person='Gideon Strauss', section='About My Work', index=0,
         expect='I think about the stories we humans tell',
         replace=GIDEON_OPENING),
    dict(person='Gideon Strauss', section='About My Work', index=-1,
         expect='not very active',
         replace=GIDEON_CLOSING),

    # "Obviously, please remove the 'Academic Dean' position from my page."
    # The title was also the closing clause of his biography. Only that clause is
    # dropped; the sentence and the 2015 date are his own words, untouched.
    # To restore it, delete this patch and rerun build/generate.py.
    dict(person='Gideon Strauss', section='Biography', index=-1,
         expect='appointed as Academic Dean in 2018',
         replace='Gideon started teaching at ICS in 2015.'),
]


def apply(bios):
    for p in PATCHES:
        rec = bios[p['person']]
        sec = next(s for s in rec['sections'] if s['heading_text'] == p['section'])
        block = sec['blocks'][p['index']]
        if p['expect'] not in block['h']:
            raise SystemExit(
                'patch no longer matches: %s / %s / block %s\n  expected to find: %r\n'
                '  found: %r' % (p['person'], p['section'], p['index'],
                                 p['expect'], block['h'][:120]))
        block['h'] = p['replace']
    return bios
