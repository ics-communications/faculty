/* ICS Faculty — navigation, reveal, and the footer address.
   Everything here is progressive enhancement: the pages are complete without it. */
(function () {
  'use strict';

  document.documentElement.classList.add('js');

  /* ── Mobile menu ─────────────────────────────────────────────── */
  var burger = document.querySelector('.ics-burger');
  var menu = document.getElementById('mobileMenu');

  function closeMenu() {
    if (!menu) return;
    menu.classList.remove('is-open');
    document.body.style.overflow = '';
    if (burger) {
      burger.setAttribute('aria-expanded', 'false');
      burger.focus();
    }
  }

  if (burger && menu) {
    burger.setAttribute('aria-expanded', 'false');
    burger.setAttribute('aria-controls', 'mobileMenu');
    burger.addEventListener('click', function () {
      menu.classList.add('is-open');
      document.body.style.overflow = 'hidden';
      burger.setAttribute('aria-expanded', 'true');
      var close = menu.querySelector('.ics-mobile-menu__close');
      if (close) close.focus();
    });
    var closeBtn = menu.querySelector('.ics-mobile-menu__close');
    if (closeBtn) closeBtn.addEventListener('click', closeMenu);
    menu.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') closeMenu();
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && menu.classList.contains('is-open')) closeMenu();
    });
  }

  /* ── Desktop dropdowns: hover opens them in CSS, this is for keyboards ── */
  Array.prototype.forEach.call(
    document.querySelectorAll('.ics-nav__item > button'),
    function (btn) {
      btn.addEventListener('click', function () {
        var open = this.getAttribute('aria-expanded') === 'true';
        this.setAttribute('aria-expanded', open ? 'false' : 'true');
      });
    }
  );

  /* ── The authored moment: entries settle in, drop-rules draw ── */
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)');
  var targets = document.querySelectorAll('.entry');

  function settle(el, delay) {
    if (delay) setTimeout(function () { el.classList.add('is-in'); }, delay);
    else el.classList.add('is-in');
  }

  if (!('IntersectionObserver' in window) || reduce.matches) {
    Array.prototype.forEach.call(targets, function (el) { settle(el, 0); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry, i) {
        var el = entry.target;
        if (entry.isIntersecting) {
          settle(el, i * 55);
        } else if (entry.boundingClientRect.top < 0) {
          // Scrolled clean past without ever intersecting — a fast flick, or a
          // deep link. Land it immediately rather than leaving the rule undrawn.
          settle(el, 0);
        } else {
          return;
        }
        io.unobserve(el);
      });
    }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });
    Array.prototype.forEach.call(targets, function (el) { io.observe(el); });
    // Last resort: nothing stays hidden because an observer never fired.
    setTimeout(function () {
      Array.prototype.forEach.call(targets, function (el) { settle(el, 0); });
    }, 3000);
  }

  /* ── Bio page: mark the section you are reading ── */
  var index = document.querySelector('.bio__index');
  if (index && 'IntersectionObserver' in window) {
    var links = {};
    Array.prototype.forEach.call(index.querySelectorAll('a[href^="#"]'), function (a) {
      links[a.getAttribute('href').slice(1)] = a;
    });
    var sections = document.querySelectorAll('.bio__section[id], .bio__epigraph[id]');
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        var a = links[e.target.id];
        if (!a) return;
        if (e.isIntersecting) {
          Object.keys(links).forEach(function (k) { links[k].classList.remove('is-current'); });
          a.classList.add('is-current');
          // Scroll the strip itself, never the page — scrollIntoView would walk
          // every scrollable ancestor and abort the page's own smooth scroll.
          var inner = index.querySelector('.bio__index-inner');
          if (inner && inner.scrollWidth > inner.clientWidth) {
            inner.scrollLeft = Math.max(0, a.offsetLeft - 16);
          }
        }
      });
    }, { rootMargin: '-140px 0px -65% 0px' });
    Array.prototype.forEach.call(sections, function (s) { spy.observe(s); });
  }

  /* ── Footer address, assembled here rather than sat in the markup ── */
  var el = document.getElementById('footer-email');
  if (el) {
    var addr = 'info' + '@' + 'icscanada.edu';
    el.href = 'mai' + 'lto:' + addr;
    el.textContent = addr;
  }
})();
