# -*- coding: utf-8 -*-
"""Reference lists, normalized to one house style.

The bios carried over from the old site cited work in four different conventions —
Strauss in APA author-date, Sweetman and Smick in an MLA variant, Ansell in a
journal volume/issue style, DeRoo in something closer to a publisher's catalogue.
This module restates all of them in one shape:

    book          <strong><em>Title</em></strong> (City: Publisher, Year).
    edited book   <strong><em>Title</em></strong>, eds. A, B and C (City: Publisher, Year).
    journal       <strong>“Title”</strong> in <em>Journal</em> (volume V:I, Date), pages.
    chapter       <strong>“Title”</strong> in <em>Container</em>, eds. A and B
                  (City: Publisher, Year), pages.

Notes that hang off an entry — an award, a reprint, a link — follow as a sentence
rather than a separate paragraph. Curly quotation marks and en-dashed ranges
throughout. Titles keep the wording and capitalization their authors gave them;
only the citation furniture around them is standardized. Where the source had a
plain misspelling in that furniture it is corrected, and each such correction is
marked with a `# sic:` comment naming the original.

Nothing here is generated. Any change to a person's list is a change to their
published bio — check with them, then edit the list in place.
"""


def ul(*items):
    return '<ul>' + ''.join('<li>%s</li>' % i for i in items) + '</ul>'


PORTAL = ('More of my projects can be found listed on the '
          '<a href="http://research-portal.icscanada.edu/search/label/%s">'
          '<strong>ICS Research Portal</strong></a>.')

# ─────────────────────────────────────────────────────────────────────────────
# Nik Ansell
# ─────────────────────────────────────────────────────────────────────────────

ANSELL_BOOKS = ul(
    '<strong><em>The Woman Will Overcome The Warrior: A Dialogue with the '
    'Christian/Feminist Theology of Rosemary Radford Ruether</em></strong> '
    '(Lanham, MD/London: University Press of America, 1994).',

    '<strong><em>The Annihilation Of Hell: Universal Salvation and the Redemption of '
    'Time in the Eschatology of Jürgen Moltmann</em></strong> (Paternoster Press, 2013).',
)

# The three "Available online at:" paragraphs and the "Reprinted in:" list that
# used to sit between these entries are folded into the entries they belong to.
ANSELL_ARTICLES = ul(
    '<strong>“Trees, Forestry, and the Responsiveness of Creation”</strong> in '
    '<em>Cross Currents</em> (volume 44:2, Summer 1994), 149–162. Co-authored with '
    'Brian J. Walsh and Marianne B. Karsh; the lead article in a theme issue on '
    'eco-theology. <a href="http://www.crosscurrents.org/trees.htm">Available '
    'online</a>. Reprinted in Roger S. Gottlieb, ed., <em>This Sacred Earth: Religion, '
    'Nature, Environment</em> (New York/London: Routledge, 1996), 423–435; in '
    '<em>The Other Journal</em> (volume 8, October 2, 2006), '
    '<a href="http://theotherjournal.com/article.php?id=206">available online</a>; and '
    'in David Clowney and Patricia Mosto, eds., <em>Earthcare: An Anthology in '
    'Environmental Ethics</em> (Lanham, MD: Rowman &amp; Littlefield, 2009).',
    # sic: the source read "Roman and Littlefield".


    '<strong>“The Call of Wisdom/The Voice of the Serpent: A Canonical Approach to the '
    'Tree of Knowledge”</strong> in <em>Christian Scholar’s Review</em> '
    '(volume 31:1, Fall 2001), 31–58. Winner of the Charles J. Miller award for '
    '<em>Christian Scholar’s Review</em> 31. <a href="http://faculty.gordon.edu/hu/bi/'
    'ted_hildebrandt/OTeSources/01-Genesis/Text/Articles-Books/Ansell-Serpent-CSR.pdf">'
    'Available online</a>.',

    '<strong>“Foundational and Transcendental Time: An Essay”</strong> in '
    '<em>Philosophy As Responsibility: A Celebration of Hendrik Hart’s Contribution to '
    'the Discipline</em>, eds. Ronald A. Kuipers and Janet Catherina Wesselius '
    '(Lanham, MD: University Press of America, 2002), chapter 5, 63–79.',

    '<strong>“Creational Man/Eschatological Woman: A Future for Theology”</strong>, ICS '
    'inaugural address, 2006. <a href="http://hdl.handle.net/10756/320796">Available '
    'online</a>.',

    '<strong>“Jesus On The Offensive”</strong> in <em>The Banner</em> (October 2008), '
    '44–46. <a href="http://www.thebanner.org/magazine/issue.cfm?id=173">Available '
    'online</a>.',

    '<strong>“Hell: The Nemesis of Hope?”</strong> in <em>The Other Journal</em> '
    '(volume 14, April 20, 2009). <a href="http://theotherjournal.com/2009/04/20/'
    'hell-the-nemesis-of-hope/">Available online</a>. Revised version in Bradley '
    'Jersak, <em>Her Gates Will Never Be Shut: Hell, Hope, and the New Jerusalem</em> '
    '(Eugene, OR: Wipf and Stock, 2009), 191–210.',
)


def _third_way(ref, vol, date, page):
    v = '(volume %s, %s)' % (vol, date) if vol else '(%s)' % date
    return ('<strong>“Commentary: %s”</strong> in <em>Third Way</em> %s, %s.'
            % (ref, v, page))


ANSELL_THIRD_WAY = ul(*[_third_way(*a) for a in [
    ('Job 1:1ff and 42:12–15',                          '19:7',  'September 1996', '20'),
    ('Mark 12:38–13:2',                                 '20:4',  'May 1997',       '20'),
    ('Romans 1:26f.',                                   '20:7',  'September 1997', '20'),
    ('Colossians 3:1f.',                                '22:1',  'February 1999',  '22'),
    ('Luke 20:27–36',                                   '22:2',  'March 1999',     '22'),
    ('Revelation 17:3',                                 '22:6',  'July 1999',      '22'),
    ('Revelation 12:1–6',                               '22:8',  'October 1999',   '23'),
    ('Revelation 20:1–6',                               '23:1',  'March 2000',     '22'),
    ('Revelation 20:11–15',                             '23:10', 'December 2000',  '20'),
    ('Revelation 1:7',                                  '24:1',  'February 2001',  '22'),
    # sic: the source read "February 20001".
    ('Genesis 1:27f., Daniel 2:35 and Ephesians 1:22f.', '25:1', 'February 2002',  '24'),
    ('Genesis 27:29, Isaiah 60:14–16 and Genesis 32:27–30', '25:6', 'August 2002', '16'),
    ('Exodus 19:5–6',                                   None,    'November 2002',  '22'),
    ('John 2.15–16, 18–19, 10:30–39 and 14:2a, 3',      '26:6',  'Summer 2003',    '15'),
    ('Genesis 22',                                      None,    'April 2004',     '16'),
    ('Genesis 11:4 &amp; 22.15–17a',                    None,    'Summer 2004',    '15'),
    ('Daniel 7.13–14, 27',                              None,    'June 2006',      '26'),
]])

ANSELL_PORTAL = ('More of my written work can be found listed on the '
                 '<a href="http://research-portal.icscanada.edu/search/label/nansell">'
                 '<strong>ICS Research Portal</strong></a>.')


# ─────────────────────────────────────────────────────────────────────────────
# Bob Sweetman
# ─────────────────────────────────────────────────────────────────────────────

SWEETMAN_BOOKS = ul(
    '<a href="https://wipfandstock.com/9781498296816/tracing-the-lines/"><strong><em>'
    'Tracing the Lines: Spiritual Exercise and the Gesture of Christian Scholarship'
    '</em></strong></a>, <em>Currents in Reformational Thought</em> series '
    '(Eugene, OR: Wipf and Stock, 2016).',

    '<strong><em>Changing to Stay the Same: Meditations on Faithfulness and the Witness '
    'of the Institute for Christian Studies</em></strong>, eds. Allyson Carr and '
    'Ronald A. Kuipers (Toronto, ON: Institute for Christian Studies, 2014).',

    '<a href="https://www.amazon.ca/Phrygian-Mode-Neo-Calvinism-Lamentations-'
    'Reformational/dp/0761830219"><strong><em>In the Phrygian Mode: Neo-Calvinism, '
    # sic: the book list read "Reformed Philosophy"; his own prose lower down the page
    # had it right. Title per the publisher (ISBN 978-0-7618-3021-4).
    'Antiquity and the Lamentations of Reformational Philosophy</em></strong></a> '
    '(Lanham, MD: University Press of America, 2007).',
)

SWEETMAN_SCHOLASTICISM = ul(
    '<strong>“Exemplary Care: Storytelling and the ‘Art of Arts’ among '
    'Thirteenth-Century Dominicans”</strong> in <em>From Learning to Love: Schools, Law, '
    'and Pastoral Care in the Middle Ages. Essays in Honour of Joseph W. Goering</em>, '
    # sic: the source read "Esssays".
    'eds. Tristan Sharp, Isabelle Cochelin, Greti Dinkova-Bruun, Abigail Firey and '
    'Giulio Silano (Toronto, ON: Pontifical Institute of Mediaeval Studies, 2017), '
    '628–646.',

    '<strong>“Foreword”</strong> in Louis Mackey, <em>Faith Order Understanding: '
    'Natural Theology in the Augustinian Tradition</em> (Toronto, ON: Pontifical '
    'Institute of Mediaeval Studies, 2011), xi–xxiii.',

    '<strong>“Univocity, Analogy and the Mystery of Being According to John Duns '
    'Scotus”</strong> in <em>Creation, Covenant and Participation: Radical Orthodoxy '
    'and the Reformed Tradition</em>, eds. James K.A. Smith and James H. Olthuis '
    '(Grand Rapids, MI: Baker Academic, 2005), 73–87.',

    '<strong>“John Paul II’s Account of the Unity of Christian Scholarship in '
    '<em>Fides et Ratio</em>”</strong> in <em>That the World May Believe: Essays on '
    'Mission and Unity in Honour of George Vandervelde</em>, eds. Margaret O’Gara and '
    'Michael Goheen (Lanham, MD: University Press of America, 2006), 203–214.',

    '<strong>“Haunting Conceptual Boundaries: Miracle in the <em>Summa theologiae</em> '
    'of Thomas Aquinas”</strong> in <em>Limina: Thresholds and Borders</em>, '
    'eds. J. Goering, F. Guardiani and G. Silano (Ottawa: Legas, 2005), 63–72.',
    # sic: the source read "Thresholds and Boundaries", "F. Guardini" and
    # "New York". Title, editor and city per PhilPapers records for the volume.


    '<strong>“Plotting the Margins: An Historical Episode in the Management of Social '
    'Plurality”</strong> in <em>Towards an Ethics of Community: Negotiations of '
    'Difference in a Pluralist Society</em>, ed. James H. Olthuis (Waterloo, ON: '
    'Wilfrid '
    # sic: the source read "Wildred Laurier".
    'Laurier University Press, 2001), 11–35.',

    '<strong>“When Popular Piety and Theological Learning Conjoin: St. Bonaventure on '
    'Demonic Powers and the Christian Soul”</strong> in <em>Fides et Historia</em> '
    '(volume 23, 1991), 4–18.',
)

SWEETMAN_PLATONISM = ul(
    '<strong>“Love, Understanding, and the Mystical Knowledge of God”</strong> in '
    '<em>Mystics, Visions and Miracles</em>, eds. J. Goering, F. Guardiani and '
    'G. Silano (New York: Legas, 2002), 173–183.',
)

SWEETMAN_MYSTICISM = ul(
    '<strong>“Sin Has Its Place, but All Shall Be Well: The Universalism of Hope in '
    'Julian of Norwich (c. 1342–c. 1416)”</strong> in <em>“All Shall Be Well”: '
    'Explorations in Universalism and Christian Theology, from Origen to Moltmann</em>, '
    'ed. Gregory MacDonald (Eugene: Cascade Books, 2011), 66–92.',

    '<strong>“<em>Exempla</em> and the Promotion of Religious Identity: Gerard of '
    'Frachet’s <em>Vitae fratrum</em>”</strong> in <em>Weapons of Mass Instruction: '
    'Secular and Religious Institutions Teaching the World</em>, eds. Joseph Goering, '
    'Francesco Guardiani and Giulio Silano (Ottawa: Legas, 2008), 41–50.',

    '<strong>“<em>Nisi necessitate et utilitate</em>: Catherine of Sienna’s Dominican '
    'Confessors and the Principles of a Licit Pastoral ‘Irregularity’”</strong> in '
    '<em>Rule Makers and Rule Breakers</em>, eds. Joseph Goering, Francesco Guardiani '
    'and Giulio Silano (Ottawa: Legas, 2006), 199–210.',

    '<strong>“Christine the Astonishing”</strong> in <em>Women and Gender in Medieval '
    'Europe: An Encyclopedia</em>, ed. Margaret Schaus (New York: Routledge, 2006).',
    # sic: the source read "Margaret Schmauss".


    '<strong>“Talking Dirty, Analogically Speaking”</strong> in <em>Pro Rege</em> '
    '(volume 32, 2004), 16–19.',

    '<strong>“Thomas of Cantimpré and the Performative Reading of Scripture: A Study in '
    'Two <em>Exempla</em>”</strong> in <em>With Reverence for the Word: Medieval '
    # sic: the source read "With Reverance for the Word".
    'Scriptural Exegesis in Judaism, Christianity and Islam</em>, eds. Jane Dammen '
    'McAuliffe, Barry D. Walfish '
    'and Joseph Goering (New York: Oxford University Press, 2003), 256–275.',

    '<strong>“Love, Understanding, and the Mystical Knowledge of God”</strong> in '
    '<em>Mystics, Visions and Miracles</em>, eds. J. Goering, F. Guardiani and '
    'G. Silano (New York: Legas, 2002), 173–183.',

    '<strong>“Of Women, Ire and Other Dangerous Things”</strong> in <em>Fides et '
    'Historia</em> (volume 32, 2000), 127–133.',

    '<strong>“Thomas of Cantimpré, Performative Reading and Pastoral Care”</strong> in '
    '<em>Performance and Transformation: New Approaches to Late Medieval '
    'Spirituality</em>, eds. Mary Suydam and Joanna Ziegler (New York: St. Martin’s '
    'Press, 1999), 134–163.',

    '<strong>“Thomas of Cantimpré, <em>Mulieres Religiosae</em> and Purgatorial Piety: '
    'Hagiographical <em>Vitae</em> and the Beguine ‘Voice’”</strong> in <em>In a '
    'Distinct Voice: Medieval Studies in Honor of Leonard E. Boyle O.P.</em>, '
    'eds. Jacqueline Brown and William Stoneman (Notre Dame, IN: University of Notre '
    'Dame, 1997), 606–626.',

    '<strong>“Christianity, Women and the Medieval Family”</strong> in <em>Religion, '
    'Feminism and the Family</em>, The Family, Religion and Culture series, eds. Anne '
    'Carr and Mary Stewart Van Leeuwen (Louisville: John Knox/Westminster Press, 1996), '
    '127–147.',

    '<strong>“Visions of Purgatory and Their Role in the <em>Bonum universale de '
    'apibus</em> of Thomas of Cantimpré”</strong> in <em>Ons Geestelijk Erf</em> '
    '(volume 67, 1993), 20–33.',

    '<strong>“Christine of St. Trond and Her Preaching Apostolate: Thomas of '
    'Cantimpré’s Hagiographical Method Revisited”</strong> in <em>Vox Benedictina</em> '
    '(volume 7, 1992), 67–97.',
)

# ─────────────────────────────────────────────────────────────────────────────
# Gideon Strauss — was APA author-date; he is the first author or an editor on
# every item, so dropping the leading author block loses nothing.
# ─────────────────────────────────────────────────────────────────────────────

STRAUSS_BOOKS = ul(
    '<strong><em>To Honor God (A monograph on executive business '
    'leadership)</em></strong>, with J. Avedisian, R. Pennings and W. Wright '
    '(Max De Pree Center for Leadership with the Work Research Foundation, 2004).',

    '<strong><em>Does the rainbow cost too much? Polemical essays on the economics of '
    'language</em></strong> (University of the Free State Acta Varia, 1997).',

    '<strong><em>The Economics of Language</em></strong>, eds. G. Strauss, '
    'M. Leibbrandt, E. P. Beukes and K. Heugh (Government of South Africa: Department '
    'of Arts, Culture, Science and Technology, 1996).',
)

STRAUSS_ARTICLES = ul(
    '<strong>“Love is not a four-letter word”</strong> in <em>Tydskrif vir Christelike '
    'Wetenskap</em> (1998), 51–69.',

    '<strong>“Language, telematics and economic development”</strong> in <em>Journal '
    'for Community Communication</em> (volume 3, 1997), 1–18.',

    '<strong>“Footprints in the dust: Can neocalvinist theory be credible in '
    'postcolonial Africa?”</strong> in <em>Acta Academica</em> (volume 28, 1996), 1–35.',

    '<strong>“Language and telematics: Interpretation and translation services, '
    'telephony, and the internet”</strong> in <em>Language and Business Life</em> '
    '(volume 22:2, 1996), 304–321.',

    '<strong>“Writing history in postcolonial Africa”</strong> in <em>Journal for '
    'Contemporary History</em> (volume 20, 1995), 1–24.',
)

STRAUSS_REVIEWS = ul(
    '<strong>Review of <em>Shaping Public Theology: Selections from the Writings of '
    'Max L. Stackhouse</em></strong>, eds. Scott R. Paeth, E. Harold Breitenberg Jr. '
    'and Hak Joon Lee, in <em>The Review of Faith &amp; International Affairs</em> '
    '(volume 13:2, 2015), 85–86.',

    '<strong>“Face to Face with the Wronged”: review of <em>Journey toward Justice: '
    'Personal Encounters in the Global South</em></strong> by Nicholas P. Wolterstorff, '
    'in <em>Comment</em> (Spring 2014), 58–62.',

    '<strong>“Civil Society and Creation Order”: review of <em>Herman Dooyeweerd: '
    'Christian Philosopher of State and Civil Society</em></strong> by Jonathan '
    'Chaplin, in <em>Books &amp; Culture</em> (September/October 2013), 22–23.',

    '<strong>Review of <em>Truth is stranger than it used to be: Biblical faith in a '
    'Postmodern age</em></strong> by J. Richard Middleton and Brian J. Walsh, in '
    '<em>European Journal of Theology</em> (volume 7:1, 1998), 71–74.',
)

# ─────────────────────────────────────────────────────────────────────────────
# Rebekah Smick
# ─────────────────────────────────────────────────────────────────────────────

SMICK_BOOKS = ul(
    '<strong>“Section B: Roman Catholic Sources and Documents”</strong>, editor, '
    'Volume V: Early Modern Sources and Documents, in <em>Sources and Documents in the '
    'History of Christian Art</em>, ed. Diane Apostolos-Cappadona (Bloomsbury/T&amp;T '
    'Clark, forthcoming 2024).',

    '<strong><em>Antiquity and Its Interpreters: From the Renaissance to the Modern '
    'Era</em></strong>, eds. Ann Kuttner, Alina Payne and Rebekah Smick (Cambridge and '
    'New York: Cambridge University Press, 2000).',
)

SMICK_CHAPTERS = ul(
    '<strong>“Kuyper’s Calvin: The Aesthetics of Disenchantment”</strong> in '
    '<em>Seeking Stillness or The Sound of Wings: Scholarly and Artistic Comment, on '
    'Art, Truth, and Society in Honour of Lambert Zuidervaart</em>, eds. Héctor Acero '
    'Ferrer, Michael DeMoor, Peter Enneson and Matthew Klaassen (Eugene: Wipf and '
    'Stock, 2021).',

    '<strong>“‘The Second Book of God’: Protestant Mysticism”</strong> in <em>Mystical '
    'Landscapes: from Vincent van Gogh to Emily Carr</em>, eds. Katharine Lochnan, '
    'Roald Nasgaard and Bogomila Welsh-Ovcharov, Art Gallery of Ontario &amp; Musée '
    'd’Orsay exhibition catalogue (Munich: DelMonico Books–Prestel, 2016). Winner of '
    'the Canadian Museums Association Research Award for 2017.',
    # sic: the source read "Canadian Museum’s Association".

    '<strong>“<em>Grazia</em> in <em>The Lives</em> of Giorgio Vasari: Rhetorical '
    'Flourish or the Power of God?”</strong> in <em>Image Makers and Image '
    'Breakers</em>, ed. Jennifer A. Harris (Ottawa: Legas, 2003).',

    '<strong>“Touch in the <em>Hypnerotomachia Poliphili</em>: The Sensual Ethics of '
    'Architecture”</strong> in <em>Early Modern Senses of Touch</em>, ed. Elizabeth D. '
    'Harvey (Philadelphia: University of Pennsylvania Press, 2002).',

    '<strong>“Vivid Thinking: Word and Image in Descriptive Techniques of the '
    'Renaissance”</strong> in <em>Antiquity and Its Interpreters: From the Renaissance '
    'to the Modern Era</em>, eds. Ann Kuttner, Alina Payne and Rebekah Smick (Cambridge '
    'and New York: Cambridge University Press, 2000).',

    '<strong>“Evoking the Vatican <em>Pietà</em>: Renaissance and Baroque Contributions '
    'to the Topos of Living Stone”</strong> in <em>The Eye of the Poet: Studies in the '
    'Reciprocity of the Visual and Literary Arts</em>, ed. Amy Golahny (Lewiston: '
    'Bucknell University Press, 1995).',
)
