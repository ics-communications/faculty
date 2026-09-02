import { chromium } from 'playwright';
const b = await chromium.launch();
// reduced motion
const c1 = await b.newContext({ viewport:{width:1440,height:900}, reducedMotion:'reduce' });
const p1 = await c1.newPage();
await p1.goto('http://127.0.0.1:8901/', { waitUntil:'networkidle' });
await p1.waitForTimeout(500);
console.log('reduced-motion:', JSON.stringify(await p1.evaluate(() => {
  const e = document.querySelectorAll('.entry')[2];
  return { cls: e.className, transform: getComputedStyle(e).transform,
           rule: getComputedStyle(e, '::before').transform };
})));
// no JS
const c2 = await b.newContext({ javaScriptEnabled:false, viewport:{width:1440,height:900} });
const p2 = await c2.newPage();
await p2.goto('http://127.0.0.1:8901/', { waitUntil:'load' });
await p2.waitForTimeout(500);
console.log('no-JS:', JSON.stringify(await p2.evaluate(() => {
  const es = [...document.querySelectorAll('.entry')];
  return { n: es.length,
           allOpaque: es.every(e => getComputedStyle(e).opacity === '1'),
           rulesDrawn: es.slice(1).every(e => getComputedStyle(e, '::before').transform === 'none'),
           noTranslate: es.every(e => getComputedStyle(e).transform === 'none') };
})));
await b.close();
