# faculty.icscanada.edu

The ICS faculty directory — 4 listing pages and 18 scholar pages, static HTML, no framework.

Read [PRODUCT.md](PRODUCT.md) for what the site is and who it is for, and
[DESIGN.md](DESIGN.md) for the visual system and the decisions behind it.

## Layout

```
index.html                  Faculty          ← generated
emeriti/  adjunct/  sessional-faculty/       ← generated
<path>/index.html           18 bio pages     ← generated
404.html  sitemap.xml  robots.txt            ← generated

css/styles.css              the only stylesheet
js/site.js                  nav, entry reveal, section spy, footer address
assets/headshots/*.jpg      20 portraits, square, on the cream ground
assets/logos/               masthead logo + ICS SVG marks

build/                      the generator — see below
tools/                      Playwright checks — see tools/README.md
info/                       source material — git-ignored, not served
package.json                dev-only: playwright, and the npm scripts above
```

Everything above the `build/` line is regenerated. **Do not hand-edit the HTML** — edit the
roster or the source content and rebuild.

## Rebuilding

```bash
python3 build/extract.py     # info/Faculty-Page/*.html  →  build/content.json
python3 build/generate.py    # content.json + roster.py  →  every page
```

`extract.py` only needs re-running if the Google Sites export changes. Day to day, edit
`build/roster.py` and run `generate.py`.

`info/` is git-ignored — it holds the Google Sites capture, the design references and the
headshot originals, none of which are ours to redistribute. `content.json` and the built
portraits are committed, so a fresh clone can run `generate.py`; `extract.py`,
`headshots.py` and `portraits.py` need the working material restored first.

Requires Python 3 with `lxml` (extract) and `Pillow` (portraits). Serve with any static
server: `python3 -m http.server 8901`.

### The build files

| File | Owns |
|---|---|
| `build/roster.py` | **Who is on the site.** Standing, degrees, titles, field, years, slug and URL path, and the authored précis for people with no ICS page. Start here for almost every change. |
| `build/extract.py` | Parsing the Google Sites export into structured content — sections, epigraph pairs, publication lists. |
| `build/patches.py` | Edits to carried-over bio text that faculty have requested. Each patch asserts on a fragment of the original, so the build fails loudly if the source shifts underneath it. |
| `build/portraits.py` | Square, circle-ready portraits at 800px on `--cream`. |
| `build/generate.py` | Page assembly — masthead, register, bio pages, footer, 404, sitemap. |

## Common changes

**Someone joins, leaves, or changes standing** — edit `build/roster.py`, run `generate.py`.
A person with a `source` gets a full page; one without gets a register entry plus whatever
`bio` / `foci` / `pubs` you give them.

**A new headshot** — drop the file anywhere, add a line to the `jobs` list in
`build/portraits.py`, run it. The `top_bias` argument (0 = top of frame, 1 = bottom) places
the face in the square.

**A faculty member asks for a text change** — add a patch to `build/patches.py` rather than
editing `content.json`, so the change survives a re-extract and is reviewable.

**A page URL** — the site inherits the live site's paths, which are mostly initial +
surname (`/nansell`, `/bsweetman`) and are not derivable from a name. `slug` in
`build/roster.py` is the internal name and the headshot filename; `path` is the URL, given
only where it differs from the slug. `STANDING_PATH` holds the same thing for the four
listing pages (`/adjunct`, `/sessional-faculty`). Changing either breaks an inbound link,
so change it only when the live site does.

**Nav or footer** — `NAV` and `FOOTER` at the top of `build/generate.py`. The footer markup is
copied byte-for-byte from the ICS main site; if ICS ever publishes a shared `footer.js`, this
is the block to replace. The masthead uses `--nav-sans` (Helvetica Neue / Arial, the stack
`education.icscanada.edu` uses) rather than the page's Outfit, so it renders identically to
the sibling property; change that one token to fold it into the page's own voice.

## Checks

`tools/` holds four Playwright checks. One-time setup: `npm install && npx playwright install
chromium` (see `tools/README.md`).

```bash
npm run serve &     # python3 -m http.server 8901
npm run build       # python3 build/generate.py
npm run check       # audit + motion + navtest

node tools/shot.mjs http://127.0.0.1:8901/ shot.png 1440 1000 full
node ~/.claude/skills/impeccable/scripts/detect.mjs --json css/styles.css index.html
```

`audit.mjs` walks 22 pages at 360 / 390 / 768 / 1024 / 1440 and should print `clean`.

## Known, deliberate

The footer **markup** is byte-identical to the ICS house footer, verified by diff on every
page. Two **style** values were changed, both in `css/styles.css`, neither touching the markup:
its `max-width` is 1120px rather than 1200px so its left edge sits on the same margin as the
rest of the page, and `.footer__bottom` is `#C6A9A9` rather than `rgba(212,172,172,0.5)` —
the old value was 2.30:1 and it colours the Privacy and Accessibility links.

Two inherited traits are left exactly as ICS has them: the `<h4>` column headings follow an
`<h2>` (a skipped heading level), and `--accent-light` on `--wine-deep` is 3.37:1 for the
column labels. Both are one-line changes if ICS wants them fixed estate-wide.

The `info@` address is assembled in JavaScript, as on the house footer, so it is absent with
JS off; the postal address and phone number are in the markup, so no-JS visitors still have
contact details.

Everything outside the footer meets 4.5:1, and every page renders complete with JavaScript
disabled — the drop-rules are drawn by default and JavaScript only opts in to animating them.
