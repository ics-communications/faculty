import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await b.newPage({ viewport:{ width:390, height:844 } });
await p.goto('http://127.0.0.1:8901/neal-deroo/', { waitUntil:'networkidle' });
const target = await p.evaluate(() => document.getElementById('publications').getBoundingClientRect().top + window.scrollY);
await p.click('.bio__index a[href="#publications"]');
await p.waitForTimeout(1600);
const after = await p.evaluate(() => window.scrollY);
console.log('mobile strip → Publications: target', Math.round(target), 'landed', Math.round(after),
            '| off by', Math.round(after - target + 72));
// desktop rail
const p2 = await b.newPage({ viewport:{ width:1440, height:900 } });
await p2.goto('http://127.0.0.1:8901/bsweetman/', { waitUntil:'networkidle' });
const t2 = await p2.evaluate(() => document.getElementById('publications').getBoundingClientRect().top + window.scrollY);
await p2.click('.bio__index a[href="#publications"]');
await p2.waitForTimeout(1600);
const a2 = await p2.evaluate(() => window.scrollY);
console.log('desktop rail → Publications: target', Math.round(t2), 'landed', Math.round(a2),
            '| off by', Math.round(a2 - t2 + 24));
// sub-heading deep link
await p2.goto('http://127.0.0.1:8901/bsweetman/#publications-my-books', { waitUntil:'networkidle' });
await p2.waitForTimeout(900);
const sub = await p2.evaluate(() => {
  const el = document.getElementById('publications-my-books');
  return el ? Math.round(el.getBoundingClientRect().top) : null;
});
console.log('deep link to sub-heading, viewport offset:', sub);
// fast scroll: are drop-rules drawn?
await p2.goto('http://127.0.0.1:8901/sessional-faculty/', { waitUntil:'networkidle' });
await p2.evaluate(() => window.scrollTo(0, document.body.scrollHeight));
await p2.waitForTimeout(900);
const rules = await p2.evaluate(() => [...document.querySelectorAll('.entry')].map(e => e.className));
console.log('after instant scroll:', JSON.stringify(rules));
await b.close();
