# -*- coding: utf-8 -*-
"""The faculty roster.

`source` names the record in content.json extracted from the old site; people with no
source have no ICS bio page and appear only as a register entry.

`slug` is the internal name — the key for a person's headshot files. `path` is the URL
the page is published at, which is the live site's own slug and usually differs; people
who arrived after the live site was captured have no `path` and are served at `slug`.
"""

SITE = 'https://faculty.icscanada.edu'

# The live site's paths for the standings pages; the keys above were never the URLs.
STANDING_PATH = {
    'faculty': '',
    'emeriti': 'emeriti/',
    'adjuncts': 'adjunct/',
    'sessionals': 'sessional-faculty/',
}

STANDINGS = [
    ('faculty',    'Faculty',   'Our Faculty',
     'The scholars who teach, supervise and hold appointments at ICS.'),
    ('emeriti',    'Emeriti',   'Emeritus Faculty',
     'Those who built the Institute’s scholarship, in the order they joined it, from '
     'the founding year to last spring.'),
    ('adjuncts',   'Adjuncts',  'Adjunct Faculty',
     'Scholars who supervise ICS students and teach alongside their own posts.'),
    ('sessionals', 'Sessionals', 'Sessional Faculty',
     'Scholars teaching individual courses in the current cycle.'),
]

PEOPLE = [
    # ── Senior Members ───────────────────────────────────────────────────────
    dict(slug='nik-ansell', path='nansell', name='Nik Ansell', standing='faculty',
         group='ICS Senior Members', degrees='PhD, MPhilF, BA',
         titles=['Associate Professor of Theology'], source='Nik Ansell'),

    dict(slug='neal-deroo', name='Neal DeRoo', standing='faculty',
         group='ICS Senior Members', degrees='PhD, MA, BA',
         titles=['Professor of Philosophy'], source='Neal DeRoo'),

    dict(slug='ronald-kuipers', path='rkuipers', name='Ronald A. Kuipers',
         standing='faculty', group='ICS Senior Members', degrees='PhD, MPhilF, BA',
         titles=['Professor of Philosophy of Religion', 'Interim Academic Dean',
                 'Director, Centre for Philosophy, Religion, and Social Ethics'],
         source='Ronald A. Kuipers'),

    # Academic Dean title removed at Gideon Strauss's request; Ronald A. Kuipers
    # holds it on an interim basis.
    dict(slug='gideon-strauss', path='gstrauss', name='Gideon Strauss',
         standing='faculty', group='ICS Senior Members', degrees='PhD, MA, BA',
         titles=['Associate Professor of Leadership and Worldview Studies'],
         source='Gideon Strauss'),

    dict(slug='edith-van-der-boom', path='evanderboom', name='Edith van der Boom',
         standing='faculty', group='ICS Senior Members', degrees='PhD, MEd, BA',
         titles=['Associate Professor of Philosophy of Education and Practice of Pedagogy',
                 'Director of the MA-EL Program'],
         source='Edith van der Boom'),

    # ── Cross-appointed from The King's University ───────────────────────────
    dict(slug='michael-demoor', name='Michael DeMoor', standing='faculty',
         group='Cross-Appointed Faculty from The King’s University',
         degrees='PhD, MPhilF, BA',
         titles=['Associate Professor of Social Philosophy'],
         precis='Works on how competing accounts of human rationality shape the way public '
                'policy is made and justified, across social ontology, democracy and '
                'plurality, and the history of political thought.',
         external='https://www.kingsu.ca/about-us/staff-directory/contact_id/3627',
         external_label='Profile at The King’s University'),

    dict(slug='jeffrey-dudiak', name='Jeffrey Dudiak', standing='faculty',
         group='Cross-Appointed Faculty from The King’s University',
         degrees='PhD, MPhilF, MA, BA',
         titles=['Professor of Philosophy'],
         precis='Reads Emmanuel Levinas on the ethical structure of discourse, and writes on '
                'philosophical anthropology, Quaker thought, and what faithfulness to the '
                'truth asks of us in a post-truth era.',
         external='https://www.kingsu.ca/about-us/staff-directory/contact_id/3625',
         external_label='Profile at The King’s University'),

    # ── Emeriti ──────────────────────────────────────────────────────────────
    dict(slug='doug-blomberg', path='dblomberg', name='Doug Blomberg', standing='emeriti',
         degrees='PhD', field='Philosophy of Education', years='2003–2018',
         source='Doug Blomberg'),

    dict(slug='hendrik-hart', path='hhart', name='Hendrik Hart', standing='emeriti',
         deceased=True, degrees='PhD', field='Systematic Philosophy', years='1967–2001',
         precis='The Institute’s first professor, who taught systematic philosophy from its '
                'founding year until 2001. <em>Understanding Our World: An Integral '
                'Ontology</em> (1984) set out the categorial framework much of ICS’s later '
                'work argued with and built on.',
         source='Hendrik Hart'),

    dict(slug='james-olthuis', path='jolthuis', name='James Olthuis', standing='emeriti',
         degrees='PhD', field='Philosophical Theology', years='1968–2004',
         precis='Joined the faculty in 1968 and has practised as a psychotherapist since '
                '1982. In <em>I Pledge You My Troth</em> and <em>The Beautiful Risk</em> he '
                'trades mastery for love, and reads relationship itself as the site of '
                'healing.',
         source='James Olthuis'),

    dict(slug='calvin-seerveld', path='cseerveld', name='Calvin Seerveld', standing='emeriti',
         deceased=True, degrees='PhD', field='Aesthetics', years='1972–1995',
         precis='A pioneering voice in Reformational aesthetics. <em>Rainbows for the Fallen '
                'World</em> (1980) gave a generation of Christian artists a way to square '
                'their faith with their vocation, and is still the book people arrive at ICS '
                'having read.',
         source='Calvin Seerveld'),

    # Moved from Senior Members in this rebuild; retired May 2025.
    # Start year not verifiable from any public source — ICS to supply.
    dict(slug='rebekah-smick', path='rsmick', name='Rebekah Smick', standing='emeriti',
         degrees='PhD, MA, BA', years='Retired 2025', years_tbc=True,
         titles=['Professor Emerita of Philosophy of Arts and Culture'],
         source='Rebekah Smick'),

    dict(slug='robert-sweetman', path='bsweetman', name='Robert Sweetman',
         standing='emeriti', degrees='PhD',
         field='H. Evan Runner Chair in the History of Philosophy',
         years='1991–2023', source='Bob Sweetman'),

    dict(slug='lambert-zuidervaart', path='lzuidervaart', name='Lambert Zuidervaart',
         standing='emeriti', degrees='PhD', field='Philosophy', years='2002–2016',
         source='Lambert Zuidervaart'),

    # ── Adjuncts (Michael R. Wagenman removed) ───────────────────────────────
    dict(slug='jonathan-chaplin', path='jchaplin', name='Jonathan Chaplin',
         standing='adjuncts', degrees='PhD, MPhil, BA',
         field='Political Philosophy and Theology',
         source='Jonathan Chaplin'),

    dict(slug='adrienne-dengerink-chaplin', path='adengerinkchaplin',
         name='Adrienne Dengerink Chaplin', standing='adjuncts',
         degrees='PhD, MA, BA', field='Aesthetics',
         source='Adrienne Dengerink Chaplin'),

    dict(slug='sylvia-keesmaat', path='skeesmaat', name='Sylvia Keesmaat',
         standing='adjuncts', degrees='DPhil, MA, BA',
         field='Biblical Studies and Hermeneutics',
         source='Sylvia Keesmaat'),

    # ── Sessionals (Michael Buttrey and Robert Covolo removed) ───────────────
    dict(slug='dean-dettloff', name='Dean Dettloff', standing='sessionals',
         degrees='PhD, MA, BA', field='Political Philosophy', source='Dean Dettloff'),

    dict(slug='andrew-tebbutt', name='Andrew Tebbutt', standing='sessionals',
         degrees='PhD, MA, MA, BA', field='Social and Political Philosophy',
         titles=['SSHRC Postdoctoral Research Fellow'],
         precis='Asks how ethical and religious community forms personal identity, and how '
                'that formation carries into public dialogue, reading German idealism, '
                'phenomenology, and contemporary social and political philosophy together.',
         bio='Andrew Tebbutt holds a PhD from the University of Toronto (2020), an MA from '
             'the Institute for Christian Studies, and an MA and BA from Brock University. '
             'He has taught at ICS as a sessional lecturer and served as Postdoctoral '
             'Research Associate in the Centre for Philosophy, Religion and Social Ethics, '
             'where he hosted the <em>Critical Faith</em> podcast. He is a SSHRC '
             'Postdoctoral Research Fellow at the Institute for Christian Studies.',
         foci=['Ethical and religious community as a formative context',
               'German idealist philosophy',
               'Phenomenology',
               'Contemporary social and political philosophy',
               'Public dialogue and public space']),

    dict(slug='jacob-benjamins', name='Jacob Benjamins', standing='sessionals',
         degrees='PhD, MAS, MA, MA', field='Phenomenology and Political Theology',
         titles=['SSHRC Postdoctoral Research Fellow'],
         precis='Works on the theological, existential and socio-political dynamics of '
                'experiencing God’s absence or presence, and on what metaphor is doing '
                'when philosophy and theology reach for it.',
         bio='Jacob Benjamins is a SSHRC Postdoctoral Research Fellow at the Institute for '
             'Christian Studies. He completed a double doctorate with KU Leuven and '
             'Australian Catholic University, and holds a Master of Advanced Studies in '
             'Theology and Religion (KU Leuven), an MA in Philosophy of Religion (McGill '
             'University), and an MA in Theology (Regent College). At KU Leuven he '
             'coordinates the Interfaculty Centre for Catholic Thought and takes part in '
             '<em>Atheism and Christianity: Moving Past Polemic</em>, a research '
             'collaboration with Australian Catholic University. His recent work follows the '
             'Christian contemplative traditions — monastic and religious lives shaped '
             'by silence, solitude, asceticism and stillness.',
         foci=['Phenomenology', 'Political theology',
               'Metaphor in philosophy and theology',
               'The experience of divine absence and presence',
               'Christian contemplative traditions'],
         pubs=['<em>The Play of Goodness: Creation, Phenomenology, and Culture</em> '
               '(New York: Fordham University Press, 2025).',
               'Co-editor, <em>The Act of Contemplation: Metaphysics, Phenomenology and the '
               'Religious Life</em> (University of Toronto Press, forthcoming).',
               'Co-editor, <em>From Contemplation to Critique: Key Figures of Social '
               'Spirituality in the Twentieth Century</em> (Studies in Spirituality, '
               'forthcoming).'],
         external='https://theo.kuleuven.be/en/research/researchers/00111799',
         external_label='Profile at KU Leuven'),
]

CENSUS = {
    'faculty':    ('Five senior members', 'Two cross-appointed'),
    'emeriti':    ('Seven members', '1967 &ndash; 2025'),
    'adjuncts':   ('Three adjunct scholars', None),
    'sessionals': ('Three sessional scholars', None),
}

BY_SLUG = {p['slug']: p for p in PEOPLE}


def of(standing):
    return [p for p in PEOPLE if p['standing'] == standing]


def href(p):
    """A person's directory, with its trailing slash."""
    return (p.get('path') or p['slug']) + '/'
