# tools

Playwright checks for the built site. One-time setup, from the project root:

```bash
npm install                        # installs playwright
npx playwright install chromium    # ~115 MB headless browser
```

Then, with a server running:

```bash
npm run serve &     # python3 -m http.server 8901
npm run check       # audit + motion + navtest
```

| Script | What it checks |
|---|---|
| `audit.mjs` | Every page at 360 / 390 / 768 / 1024 / 1440 — horizontal overflow, broken images, tap targets under 24px, console errors. Prints `clean` when there is nothing to report. |
| `shot.mjs` | `node tools/shot.mjs <url> <out.png> <w> <h> <top\|full>` — screenshot at 2x for visual review. |
| `motion.mjs` | That entries and drop-rules are visible with JavaScript disabled and under `prefers-reduced-motion: reduce`. |
| `navtest.mjs` | That rail and strip anchor links land on their target, and that a fast scroll still settles every entry. |

All four assume the site is served at `http://127.0.0.1:8901/`.
