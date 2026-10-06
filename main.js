/* ==========================================================================
   NutraNurture — light behaviour only.
   Mobile nav, sticky-header shadow, gentle reveals, counters, inquiry form.
   Nothing here takes over scrolling, the cursor, or page navigation.
   ========================================================================== */
(function () {
  'use strict';

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------------------------------------------------------- mobile nav */
  var toggle = document.querySelector('.pill__toggle');
  var nav = document.getElementById('primary-nav');

  if (toggle && nav) {
    var setOpen = function (open) {
      toggle.setAttribute('aria-expanded', String(open));
      nav.classList.toggle('is-open', open);
    };

    toggle.addEventListener('click', function () {
      setOpen(toggle.getAttribute('aria-expanded') !== 'true');
    });

    nav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') setOpen(false);
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('is-open')) {
        setOpen(false);
        toggle.focus();
      }
    });

    document.addEventListener('click', function (e) {
      if (!nav.classList.contains('is-open')) return;
      if (nav.contains(e.target) || toggle.contains(e.target)) return;
      setOpen(false);
    });

    window.addEventListener('resize', function () {
      if (window.innerWidth > 1080) setOpen(false);
    });
  }

  /* -------------------------------------------------- sticky header shade */
  var header = document.querySelector('.site-header');
  if (header) {
    var shade = function () {
      header.classList.toggle('is-stuck', window.scrollY > 4);
    };
    shade();
    window.addEventListener('scroll', shade, { passive: true });
  }

  /* --------------------------------------------------------- reveals ----
     A short fade-up, nothing more. Numbers are rendered in the HTML, so they
     are correct even before this runs. */
  var reveals = document.querySelectorAll('.reveal');

  if (reduce || !('IntersectionObserver' in window)) {
    reveals.forEach(function (el) { el.classList.add('is-in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        var el = e.target;
        var delay = Number(el.dataset.delay || 0);
        setTimeout(function () { el.classList.add('is-in'); }, delay);
        io.unobserve(el);
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -5% 0px' });

    reveals.forEach(function (el) { io.observe(el); });
  }

  /* -------------------------------------------------------- inquiry form --
     No backend is wired up: the form opens a pre-filled email so nothing a
     visitor types is lost. Point FORM_ENDPOINT at Formspree, Netlify Forms or
     your own API and it will POST there instead. */
  var FORM_ENDPOINT = '';
  var form = document.getElementById('inquiry-form');

  if (form) {
    var status = document.getElementById('form-status');
    var say = function (msg) {
      if (!status) return;
      status.textContent = msg;
      status.classList.add('is-visible');
    };

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;

      var data = new FormData(form);
      var get = function (k) { return (data.get(k) || '').toString().trim(); };

      if (FORM_ENDPOINT) {
        fetch(FORM_ENDPOINT, { method: 'POST', body: data })
          .then(function () {
            say('Thank you — your inquiry has been sent. Akanksha or her team will reply within one working day.');
            form.reset();
          })
          .catch(function () {
            say('Something went wrong. Please call or WhatsApp +91 99200 39625 instead.');
          });
        return;
      }

      var body = [
        'Name: ' + get('name'),
        'Email: ' + get('email'),
        'Phone / WhatsApp: ' + get('phone'),
        'Type of inquiry: ' + get('inquiry'),
        'City / Location: ' + get('city'),
        '', 'Health goals / requirements:', get('message')
      ].join('\n');

      window.location.href = 'mailto:akanksha.bhargava81@gmail.com' +
        '?subject=' + encodeURIComponent('Website inquiry — ' + (get('inquiry') || 'Consultation')) +
        '&body=' + encodeURIComponent(body);

      say('Your email app is opening with the details filled in. Prefer to talk? Call or WhatsApp +91 99200 39625.');
    });
  }

  /* ------------------------------------------------------------ #anchors --
     The browser performs its jump to location.hash before web fonts and
     images have settled, so the page grows underneath it and the jump lands
     short (often back at the top). Re-apply it once things stop moving.
     scrollIntoView respects scroll-margin-top, so the fixed header is
     cleared automatically. */
  if (location.hash.length > 1) {
    var anchor = null;
    try { anchor = document.querySelector(location.hash); } catch (e) { anchor = null; }

    if (anchor) {
      var jump = function () {
        // 'instant' matters: with scroll-behavior:smooth an animated scroll
        // gets aborted when fonts finish loading and resize the page.
        var margin = parseFloat(getComputedStyle(anchor).scrollMarginTop) || 0;
        var y = anchor.getBoundingClientRect().top + window.scrollY - margin;
        window.scrollTo({ top: Math.max(0, y), behavior: 'instant' });
      };

      // Re-apply until the page stops growing underneath us. Fonts, images and
      // the reveal styles all settle at slightly different moments, and a
      // single jump lands short whichever one you pick.
      var settle = function () {
        var last = -1, tries = 0;
        var tick = function () {
          jump();
          var now = document.documentElement.scrollHeight;
          tries++;
          if (now !== last && tries < 12) {
            last = now;
            setTimeout(tick, 100);
          }
        };
        tick();
      };

      settle();
      window.addEventListener('load', settle);
      if (document.fonts && document.fonts.ready) document.fonts.ready.then(settle);
    }
  }

  /* -------------------------------------------------------------- footer */
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });
})();
