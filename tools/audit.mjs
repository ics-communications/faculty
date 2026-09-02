import { chromium } from 'playwright';
const b = await chromium.launch();
const pages = ['/','/emeriti/','/adjunct/','/sessional-faculty/','/nansell/','/neal-deroo/',
 '/rkuipers/','/gstrauss/','/evanderboom/','/dblomberg/','/hhart/',
 '/jolthuis/','/cseerveld/','/rsmick/','/bsweetman/','/lzuidervaart/',
 '/jchaplin/','/adengerinkchaplin/','/skeesmaat/','/dean-dettloff/',
 '/andrew-tebbutt/','/jacob-benjamins/'];
const widths = [360, 390, 768, 1024, 1440];
const out = [];
for (const w of widths) {
  const p = await b.newPage({ viewport:{ width:w, height:900 } });
  const errs = [];
  p.on('pageerror', e => errs.push(e.message));
  p.on('console', m => { if (m.type()==='error') errs.push(m.text()); });
  for (const u of pages) {
    await p.goto('http://127.0.0.1:8901'+u, { waitUntil:'networkidle' });
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(120);
    const r = await p.evaluate(() => {
      const over = document.documentElement.scrollWidth - window.innerWidth;
      const broken = [...document.images].filter(i => i.complete && i.naturalWidth === 0).length;
      const tiny = [...document.querySelectorAll('a,button')].filter(el => {
        const b = el.getBoundingClientRect();
        return b.width > 0 && b.height > 0 && b.height < 24 &&
               !el.closest('.site-footer,.prose,.bio__crumb');
      }).length;
      return { over, broken, tiny };
    });
    if (r.over > 1 || r.broken || r.tiny) out.push({ w, u, ...r });
  }
  if (errs.length) out.push({ w, errs });
  await p.close();
}
console.log(out.length ? JSON.stringify(out, null, 1) : 'clean across ' + widths.join('/') + ' × ' + pages.length + ' pages');
await b.close();
