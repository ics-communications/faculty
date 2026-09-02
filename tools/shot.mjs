import { chromium } from 'playwright';
const [,, url, out, w, h, full] = process.argv;
const b = await chromium.launch();
const p = await b.newPage({ viewport:{ width:+w, height:+h }, deviceScaleFactor: 2 });
await p.goto(url, { waitUntil:'networkidle' });
await p.evaluate(() => document.fonts.ready);
await p.waitForTimeout(700);
await p.evaluate(async () => {
  await new Promise(r => { let y=0; const t=setInterval(()=>{ window.scrollTo(0,y); y+=600;
    if (y > document.body.scrollHeight) { clearInterval(t); window.scrollTo(0,0); r(); } }, 30); });
});
await p.evaluate(async () => {
  await Promise.all([...document.images].filter(i=>!i.complete)
    .map(i => new Promise(r => { i.addEventListener('load', r); i.addEventListener('error', r); })));
});
await p.waitForTimeout(700);
await p.screenshot({ path: out, fullPage: full === 'full' });
await b.close();
