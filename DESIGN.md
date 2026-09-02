# DESIGN.md — ICS Faculty site

The visual world is **inherited**, not invented. `info/Design-References/ics-site/css/styles.css`
is the authority for colour, type and the footer; `education.icscanada.edu` is the authority
for navigation geometry. This file records what carries across and what this surface adds.

---

## Direction contract

**THESIS** — A faculty page is a set of positions, not a staff photo wall. Each scholar is
introduced by the sentence they chose to think alongside. It refuses the category default:
a grid of identical portrait-plus-title cards.

**OWN-WORLD** — The contributors' pages of an academic quarterly. Cream ground, wine rules,
Libre Baskerville set large for the quotations and small-caps Outfit for the apparatus.
Circular portraits with a copper ring, inherited from `.announce__photo`. Full-measure
hairlines separate entries the way a journal separates contributors. Recognizable with all
content removed by: the hairline register, the asymmetric three-column split
(132px portrait / 1fr apparatus / 1.35fr line), and the wine drop-rule that draws itself.

**STORY** — The visitor scans four standings, reads three or four quotations, recognizes one
mind worth following, and lands on that person's page — where the same quotation opens at
full scale, unabridged, and the work follows underneath. The register shows only the opening
of a long epigraph; finishing it is a reason to click.

**FIRST VIEWPORT** — Black masthead. Then a typographic opening: "Our Faculty" in Baskerville
at clamp(2.4rem, 6vw, 4rem), a single line of orientation beneath it, and the four standings
as a horizontal rule of links. No hero image — the portraits are the images, and they start
one scroll down. The first entry's epigraph is partly visible above the fold.

**FORM** — The journal contributors' register. First on the ordered list of six structures
derived from the content (register / directory table / portrait mosaic / grouped card grid /
service timeline / research-foci filter); chosen because it is the only one that puts the
epigraphs — the site's one uncopyable asset — in the primary position.

Structure varies by standing rather than repeating:

- **Faculty** (7, grouped) — the three-column register: gutter, apparatus, line.
- **Emeriti** (7) — the same register ordered by the year each member joined, 1967 to 2025,
  with the service span set in the gutter under the portrait in oldstyle numerals. The page
  reads as the Institute's own chronology.
- **Adjuncts** and **Sessionals** (3 each) — `.register--sparse`: a 172px portrait, the name
  a step larger, and the line at a full 36em measure below the apparatus rather than beside
  it. Three contributor notes, not three rows of a seven-row table.

---

## Tokens

Inherited verbatim from the ICS stylesheet. Do not re-derive.

```
--wine #9B0D24   --wine-deep #7A0A1C   --wine-mid #BE0B28   --wine-soft #D44B5E
--accent #A85A32 --accent-light #C87A52 --accent-muted #8E4A28 --accent-pale #EEDACA
--accent-deep #7A4020
--teal #7A5C3A   --teal-light #A07A4E  --teal-pale #E6D9C6
--cream #FDFBF7  --cream-warm #F9F5ED  --parchment #F0E9DD
--text-dark #2E1318  --text-body #3A3330  --text-on-dark #E8C2C2
--text-muted #6E6862   (darkened from the ICS #857E78, which is 3.6:1 on cream)
--serif 'Libre Baskerville', Georgia, serif
--sans  'Outfit', -apple-system, BlinkMacSystemFont, sans-serif
--ease  cubic-bezier(0.25, 0.46, 0.45, 0.94)
```

Added for this surface only:

```
--ink #000000        masthead ground
--brand-red #D31145  from ICS-Logo-Red.svg — masthead accent only
--paper #FFFFFF
--rule rgba(155,13,36,0.14)   full-measure hairline
--nav-sans 'Helvetica Neue', Helvetica, Arial   masthead only
```

## Colour strategy

**Restrained.** Cream ground, wine for structure and headings, copper for the apparatus
(eyebrows, attributions, links-on-dark). One saturated field per page at most: the footer.

`--brand-red` is scoped to the masthead and nothing else. It is the logo red, and using it
in body content would put two reds on one page.

## The masthead is a separate object

Black ground, white type, red accents. It is deliberately not of the cream world — it reads
as an institutional bar sitting above the page, the same bar that runs across
`education.icscanada.edu`. Geometry is copied exactly: 100px tall (69px ≤1200px), logo 53px
(30px ≤1200px), links 0.8rem / 600 / 0.14em uppercase, hover underline at 6px offset and
1.5px thickness, right-aligned dropdowns, asymmetric three-bar burger, full-screen overlay
menu — all verified against that site's `shared.css`.

The type is that site's stack too — `--nav-sans: 'Helvetica Neue', Helvetica, Arial` — not
the page's Outfit, so the bar renders identically to the sibling property on any given
device. Swapping `--nav-sans` to `var(--sans)` is the one line that folds it back into the
page's own voice.

Brand red is used for accents only, never as text: `#D31145` on `#000000` is 3.94:1. The
active item and the current mobile-menu item are marked with a red underline under white
type.

## The line

Each register entry ends in a right-hand column carrying one of three things, in this order
of preference:

1. **The scholar's own epigraph**, from "Something Worth Considering…" — trimmed to its
   opening sentence when long, with the attribution intact. Nine people have one; several
   chose two or three, and the register shows the first.
2. **A précis** — authored for the seven people with no ICS bio page (the two cross-appointed
   professors, the two new sessionals) or with no prose on it (Hart, Olthuis, Seerveld).
   Sourced and factual; the sources are named in the handover.
3. **The opening of their own "About" text**, trimmed at a sentence boundary.

Never an empty column. A page whose only content is resource links repeats its précis as a
serif lede under the name (`.bio__lede`), so it does not open on a bare list.

## Portraits

Square JPEG, masked to a circle in CSS with a 3px `--accent-light` ring. Most source images
are already circle-masked on white, so the CSS circle lands exactly on the existing one; they
are composited onto `--cream` so no white corner can show. `object-fit: cover`, explicit
`width`/`height` attributes, `loading="lazy"` below the first two.

## Type scale

| Role | Face | Size |
|---|---|---|
| Page title | serif 700 | clamp(2.4rem, 6vw, 4rem), -0.02em |
| Epigraph — register | serif 400 italic | clamp(1.05rem, 1.9vw, 1.32rem) |
| Epigraph — bio page | serif 400 italic | clamp(1.2rem, 2.6vw, 1.75rem) |
| Entry name | serif 700 | clamp(1.3rem, 2.2vw, 1.65rem) |
| Bio name | serif 700 | clamp(2rem, 5vw, 3.1rem), -0.025em |
| Section heading | serif 700 | clamp(1.4rem, 3vw, 2rem) |
| Body | sans 400 | 1rem / 1.7, measure 68ch |
| Apparatus | sans 600–700 | 0.7rem, 0.14–0.18em tracking, uppercase |
| Register epigraph, sparse | serif 400 italic | clamp(1.1rem, 2vw, 1.4rem) |
| Folio census | serif 400 | 0.92rem, oldstyle numerals |

Tracking floor -0.025em. Display never exceeds 3.1rem — this is a Read surface.

## Bio page composition

Two columns at ≥1000px: content left at a 36em measure (`ch` in Outfit measures far wider
than the average glyph — 68ch renders about 93 characters), and the section index as a sticky
rail on the right (`.bio__index`, `position: sticky; top: 2.5rem`), hairline-ruled, marking
the section being read. Below 1000px the same markup becomes a horizontal sticky strip with a
masked right edge so a clipped label reads as scrollable. The rail exists because without it
the right 40% of every bio page was empty; it is suppressed below three sections, where it
would be a stub.

Long ruled sections index their own sub-headings as a second rail level. Sweetman's
Publications runs to ~75 citations, and its `h3`s are set in the register's group-label
grammar — 0.7rem copper small caps with a full-measure hairline — so they out-rank the
citations instead of disappearing among them.

**The epigraph is the page's one ground change.** `.bio__epigraph` is a `--cream-warm` panel
that steps left to the container margin while the quotation itself stays on the same rule as
the prose below it, closed by a hairline. Each quotation carries its own attribution under a
short copper rule, and stacked quotations (van der Boom has three) are separated by a full
hairline — they are several positions, not one italic slab. Opening quotes hang.

Anchor offsets: `scroll-padding-top` is 1.5rem on desktop, where the masthead does not stick,
and 4.5rem below 1000px, where the strip does. Nothing carries a second `scroll-margin-top`;
stacking the two overshot every jump by ~260px.

## Motion

**One authored moment.** Entries settle upward 14px while their drop-rule draws from left to
right over 620ms on `--ease` — a fixed 88px rule revealed with `transform: scaleX()` from a
left origin, never an animated width. Nothing else animates on scroll.

The rule is **drawn by default**; JavaScript opts in to the draw by adding `.js`. So a fast
flick, a deep link, a dead script or a disabled one all show the finished mark rather than
nothing. The observer additionally settles any entry that scrolled past without ever
intersecting, and a 3s timeout settles whatever is left. No content depends on opacity.

Under `prefers-reduced-motion: reduce` the rule is simply drawn and the settle removed.

Hover is not motion: links get a wine underline, portraits lift their ring to `--wine`.

## Prohibitions

- No card grid as page structure, and no nested cards. This includes `.elsewhere`, which is a
  ruled row of links, not a row of bordered cells.
- No tracked uppercase eyebrow over every section — the standing label is the one named kicker.
- No `border-left` accent bars above 1px.
- No gradient text, no glass, no icon tiles.
- No second red. `--brand-red` stays in the masthead, and never as text.

## The folio

Each listing opening carries a right-aligned census in the serif, under a hairline, in the
position a journal puts its volume and date: "Five senior members / Two cross-appointed",
"Seven members / 1967 – 2025". It fills the opening's right column, which was otherwise dead,
with the one fact a directory should state up front.

## Footer

Markup copied byte-for-byte from `info/Design-References/perspective.html:673-740`, verified
by diff on every page. Styles from `ics-site/css/styles.css:1378-1465` with two deliberate
deviations, both in our stylesheet and neither touching the markup:

- `max-width` 1200px → **1120px**, to sit on the same left margin as `.container`. At 1200px
  the footer began 40px left of every other element on the page.
- `.footer__bottom` colour `rgba(212,172,172,0.5)` → **`#C6A9A9`** (2.30:1 → 5.11:1). That
  colour is inherited by the Privacy and Accessibility links, so it was failing contrast on
  interactive text.

`--accent-light` on `--wine-deep` (3.37:1) for the column headings is left as ICS has it —
a decorative label, and changing it would visibly diverge from the house footer. Do not
restyle the footer to match the masthead; the crimson footer is the ICS house standard.

## Site furniture

`404.html`, `sitemap.xml` and `robots.txt` are generated by `build/generate.py` alongside the
pages, so the roster is their single source of truth. The 404 page reuses the register's
opening and the four standings, with no current standing marked.
