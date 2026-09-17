/* Wakalat Travel & Migration Ltd. — site scripts */
(function () {
  'use strict';
  const WA_NUMBER = '8801886270118';
  const $ = (s, c) => (c || document).querySelector(s);
  const $$ = (s, c) => Array.from((c || document).querySelectorAll(s));

  /* Sticky header shadow */
  const header = $('.header');
  const totop = $('.totop');
  const onScroll = () => {
    if (header) header.classList.toggle('scrolled', window.scrollY > 10);
    if (totop) totop.classList.toggle('show', window.scrollY > 500);
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
  if (totop) totop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

  /* Mobile drawer */
  const drawer = $('.drawer');
  const openDrawer = () => { drawer.classList.add('open'); document.body.style.overflow = 'hidden'; };
  const closeDrawer = () => { drawer.classList.remove('open'); document.body.style.overflow = ''; };
  if (drawer) {
    $$('.burger').forEach(b => b.addEventListener('click', openDrawer));
    $$('.drawer .close, .drawer .backdrop').forEach(b => b.addEventListener('click', closeDrawer));
    $$('.mnav > li > a.has-sub').forEach(a => a.addEventListener('click', e => {
      e.preventDefault();
      a.parentElement.classList.toggle('open');
    }));
  }

  /* Active nav link */
  const path = location.pathname.split('/').pop() || 'index.html';
  $$('.nav a, .mnav a').forEach(a => {
    const href = a.getAttribute('href');
    if (href && href === path) a.classList.add('active');
  });

  /* Search tabs */
  $$('.search-box').forEach(box => {
    const tabs = $$('.search-tabs button', box);
    const panels = $$('.search-panel', box);
    tabs.forEach(t => t.addEventListener('click', () => {
      tabs.forEach(x => x.classList.remove('active'));
      panels.forEach(p => p.classList.remove('active'));
      t.classList.add('active');
      const p = $('#' + t.dataset.tab, box);
      if (p) p.classList.add('active');
    }));
    /* Return date only for round trip */
    $$('input[name="trip"]', box).forEach(r => r.addEventListener('change', () => {
      const ret = $('.return-field', box);
      if (ret) ret.style.opacity = r.value === 'oneway' && r.checked ? '.45' : '1';
    }));
  });

  /* Broken image fallback */
  $$('img[data-fallback]').forEach(img => {
    img.addEventListener('error', () => img.classList.add('broken'));
    if (img.complete && img.naturalWidth === 0) img.classList.add('broken');
  });

  /* Date min = today */
  const today = new Date().toISOString().slice(0, 10);
  $$('input[type="date"]').forEach(i => { if (!i.min) i.min = today; });

  /* WhatsApp / mail quote forms */
  const toast = (msg) => {
    let t = $('.toast');
    if (!t) { t = document.createElement('div'); t.className = 'toast'; document.body.appendChild(t); }
    t.textContent = msg; t.classList.add('show');
    clearTimeout(t._h); t._h = setTimeout(() => t.classList.remove('show'), 3500);
  };
  $$('form[data-wa]').forEach(form => form.addEventListener('submit', e => {
    e.preventDefault();
    const title = form.dataset.wa;
    const lines = ['*' + title + ' — Wakalat Travel & Migration Ltd.*', ''];
    $$('input, select, textarea', form).forEach(el => {
      if (!el.name || el.type === 'submit') return;
      if (el.type === 'radio' && !el.checked) return;
      if (el.type === 'checkbox' && !el.checked) return;
      const label = el.dataset.label || el.name;
      if (el.value) lines.push(label + ': ' + el.value);
    });
    lines.push('', 'Sent from wakalat website');
    const url = 'https://wa.me/' + WA_NUMBER + '?text=' + encodeURIComponent(lines.join('\n'));
    window.open(url, '_blank', 'noopener');
    toast('Opening WhatsApp with your request…');
  }));
  $$('form[data-demo]').forEach(form => form.addEventListener('submit', e => {
    e.preventDefault();
    toast(form.dataset.demo);
    form.reset();
  }));

  /* FAQ accordion */
  $$('.faq-item button').forEach(b => b.addEventListener('click', () => {
    const item = b.parentElement;
    const open = item.classList.contains('open');
    $$('.faq-item.open', item.parentElement).forEach(i => i.classList.remove('open'));
    if (!open) item.classList.add('open');
  }));

  /* Counters */
  const counters = $$('[data-count]');
  const runCounter = el => {
    const target = +el.dataset.count; const suffix = el.dataset.suffix || '';
    const dur = 1600; const start = performance.now();
    const step = now => {
      const p = Math.min(1, (now - start) / dur);
      const eased = 1 - Math.pow(1 - p, 3);
      el.firstChild.nodeValue = Math.round(target * eased).toLocaleString();
      if (p < 1) requestAnimationFrame(step); else el.firstChild.nodeValue = target.toLocaleString();
    };
    requestAnimationFrame(step);
  };

  /* Reveal on scroll */
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver(entries => entries.forEach(en => {
      if (!en.isIntersecting) return;
      en.target.classList.add('in');
      if (en.target.hasAttribute('data-count')) runCounter(en.target);
      io.unobserve(en.target);
    }), { threshold: .15 });
    $$('.reveal, [data-count]').forEach(el => io.observe(el));
  } else {
    $$('.reveal').forEach(el => el.classList.add('in'));
    counters.forEach(runCounter);
  }

  /* Footer year */
  $$('.year').forEach(el => el.textContent = new Date().getFullYear());
})();
