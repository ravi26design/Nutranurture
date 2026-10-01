# -*- coding: utf-8 -*-
"""Shared chrome — floating pill nav, Cinzel headings, gradient footer."""

VER = "8"

PHONE = "+91 9920039625"
PHONE_PRETTY = "+91 99200 39625"
PHONE_ALT = "+91 8879328790"
PHONE_ALT_PRETTY = "+91 88793 28790"
EMAIL = "akanksha.bhargava81@gmail.com"
WA = "https://wa.me/919920039625"
GOOGLE_REVIEWS = "https://share.google/3kBdsfwZ9VlHKa3qR"
INSTAGRAM = "#"
FACEBOOK = "#"

# Parked for now — rendered but not clickable (anchor with no href).
DISABLED = {"about.html", "services.html", "corporate.html", "stories.html", "contact.html"}

NAV = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("services.html", "Consultations"),
    ("corporate.html", "Corporate"),
    ("stories.html", "Stories"),
    ("contact.html", "Contact"),
]

FOOTER_SERVICES = [
    ("services.html#diabetes", "Diabetes &amp; Metabolic Health"),
    ("services.html#weight", "Weight &amp; Body Composition"),
    ("services.html#hormonal", "PCOD / PCOS &amp; Hormones"),
    ("services.html#maternal", "Maternal &amp; Child Nutrition"),
    ("corporate.html", "Corporate Wellness"),
]
FOOTER_INFO = [
    ("about.html", "About Akanksha"),
    ("services.html", "Consultations"),
    ("corporate.html", "Corporate &amp; Partners"),
    ("stories.html", "Client Stories"),
    ("contact.html", "Contact"),
]

ICON_WA = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.47 14.38c-.3-.15-1.75-.86-2.02-.96-.27-.1-.47-.15-.67.15-.2.3-.77.96-.94 1.16-.17.2-.35.22-.64.07-.3-.15-1.25-.46-2.38-1.47-.88-.79-1.47-1.75-1.65-2.05-.17-.3-.02-.46.13-.61.13-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.67-1.6-.92-2.2-.24-.58-.48-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.01-1.04 2.47s1.06 2.86 1.21 3.06c.15.2 2.1 3.2 5.08 4.49.71.3 1.26.49 1.69.63.71.22 1.36.19 1.87.12.57-.09 1.75-.72 2-1.41.25-.69.25-1.28.17-1.41-.07-.13-.27-.2-.57-.35Z"/><path d="M12.04 2h-.01C6.5 2 2 6.5 2 12.04c0 2.19.71 4.22 1.92 5.87L2.4 22.4l4.63-1.48A9.96 9.96 0 0 0 12.04 22c5.54 0 10.04-4.5 10.04-9.96C22.08 6.5 17.58 2 12.04 2Zm0 18.18c-1.7 0-3.28-.5-4.6-1.37l-.33-.2-2.75.88.9-2.67-.21-.34a8.1 8.1 0 0 1-1.25-4.35c0-4.5 3.66-8.15 8.16-8.15 4.5 0 8.15 3.65 8.15 8.15 0 4.5-3.66 8.05-8.07 8.05Z"/></svg>')
ICON_IG = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.3" cy="6.7" r="1.1" fill="currentColor" stroke="none"/></svg>')
ICON_FB = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M14.5 8.5h2.2V5.6c-.4-.05-1.7-.17-3.2-.17-3.2 0-5.1 1.9-5.1 5.3v2.6H5.7v3.3h2.7V24h3.4v-7.4h2.8l.4-3.3h-3.2v-2.3c0-1 .3-1.5 1.7-1.5Z"/></svg>')
ICON_PHONE = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 16.9v2.6a1.8 1.8 0 0 1-2 1.8 18 18 0 0 1-7.8-2.8 17.6 17.6 0 0 1-5.4-5.4A18 18 0 0 1 3 5.2 1.8 1.8 0 0 1 4.8 3.2h2.6a1.8 1.8 0 0 1 1.8 1.6c.1.9.3 1.7.6 2.5a1.8 1.8 0 0 1-.4 1.9L8.3 10.4a14.5 14.5 0 0 0 5.3 5.3l1.2-1.1a1.8 1.8 0 0 1 1.9-.4c.8.3 1.6.5 2.5.6a1.8 1.8 0 0 1 1.6 1.8Z"/></svg>')
ICON_MAIL = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2.5" y="4.5" width="19" height="15" rx="2.5"/><path d="m3 7 9 6 9-6"/></svg>')
ICON_PIN = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 5.5-8 12-8 12s-8-6.5-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="2.8"/></svg>')
ICON_VIDEO = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2.5" y="6" width="13" height="12" rx="2.5"/><path d="m15.5 10.5 6-3.5v10l-6-3.5"/></svg>')
ICON_CHECK = ('<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m4.5 10.5 3.5 3.5 7.5-8"/></svg>')
# the small circular arrow chip that sits inside every button
CHIP = '<i class="chip" aria-hidden="true"><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7.5 4.5 13 10l-5.5 5.5"/></svg></i>'
ICON_ARROW = CHIP


def head(title, description, active):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="theme-color" content="#FFFBF5">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:image" content="assets/akanksha.jpg">
<link rel="icon" href="assets/logo.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600&family=Mulish:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css?v={VER}">
</head>
<body>
"""


def header(active):
    rows = []
    for href, label in NAV:
        if href in DISABLED:
            rows.append('          <li><a class="is-parked" aria-disabled="true" tabindex="-1">%s</a></li>' % label)
        else:
            cur = ' aria-current="page"' if href == active else ''
            rows.append('          <li><a href="%s"%s>%s</a></li>' % (href, cur, label))
    links = "\n".join(rows)

    return f"""<script>document.documentElement.classList.add('js');</script>
<a class="skip" href="#main">Skip to main content</a>

<header class="site-header">
  <div class="pill">
    <a class="pill__brand" href="index.html">
      <img src="assets/logo.jpg" alt="" width="36" height="36">
      <span>NutraNurture</span>
    </a>

    <button class="pill__toggle" type="button" aria-expanded="false" aria-controls="primary-nav">
      <span class="pill__bars" aria-hidden="true"><i></i><i></i><i></i></span>
      Menu
    </button>

    <nav class="pill__nav" id="primary-nav" aria-label="Primary">
      <ul>
{links}
      </ul>
      <a class="btn btn--primary btn--sm pill__cta is-parked" aria-disabled="true" tabindex="-1">Book a Consultation {CHIP}</a>
    </nav>
  </div>
</header>

<main id="main">
"""


def cta():
    return f"""<section class="band">
  <div class="wrap band__inner">
    <h2>Ready to Start Your Health Journey?</h2>
    <p>Take the first step with a structured, empathetic nutrition assessment &mdash; in person in Ahmedabad, or online from anywhere.</p>
    <div class="btn-row btn-row--center">
      <a class="btn btn--light is-parked" aria-disabled="true" tabindex="-1">Book a Consultation {CHIP}</a>
      <a class="btn btn--ghost-light is-parked" aria-disabled="true" tabindex="-1">Corporate Wellness {CHIP}</a>
    </div>
  </div>
</section>
"""


def footer():
    svc = "".join('<li><a href="%s">%s</a></li>' % (h, l) for h, l in FOOTER_SERVICES)
    info = "".join('<li><a href="%s">%s</a></li>' % (h, l) for h, l in FOOTER_INFO)
    return f"""</main>

<footer class="site-footer">
  <div class="wrap footer-grid">
    <div>
      <h2>Specializations</h2>
      <ul class="footer-links">{svc}</ul>
    </div>

    <div>
      <h2>Information</h2>
      <ul class="footer-links">{info}</ul>
    </div>

    <div class="footer-contact">
      <h2>Contact</h2>
      <p class="footer-name">Akanksha Bhargava</p>
      <p class="footer-role">Clinical Nutritionist &middot; Certified Diabetes Educator</p>
      <p class="footer-addr">Ahmedabad, Gujarat, India</p>
      <p>
        <a href="tel:{PHONE.replace(' ', '')}">{PHONE_PRETTY}</a><br>
        <a href="tel:{PHONE_ALT.replace(' ', '')}">{PHONE_ALT_PRETTY}</a><br>
        <a href="mailto:{EMAIL}">{EMAIL}</a>
      </p>
      <div class="footer-social">
        <a href="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp">{ICON_WA}</a>
        <a href="{INSTAGRAM}" target="_blank" rel="noopener" aria-label="Instagram">{ICON_IG}</a>
        <a href="{FACEBOOK}" target="_blank" rel="noopener" aria-label="Facebook">{ICON_FB}</a>
      </div>
    </div>
  </div>

  <div class="wrap footer-bottom">
    <span>&copy; <span data-year>2026</span> NutraNurture by Akanksha Bhargava</span>
    <span>Indian Dietetics Association &middot; Ahmedabad Dietetics Association &middot; IAPEN</span>
  </div>
</footer>

<a class="wa-float" href="{WA}" target="_blank" rel="noopener">
  {ICON_WA}<span>WhatsApp</span>
</a>

<script src="main.js?v={VER}"></script>
</body>
</html>
"""

# ---------------------------------------------------------------------------
# Everything is parked for now: no call to action navigates anywhere.
# Phone, email and the in-page skip link stay live; they are contact details,
# not CTAs. Flip PARK_ALL to False to switch the whole site back on.
# ---------------------------------------------------------------------------
PARK_ALL = True

import re as _re

_KEEP = _re.compile(r'^(tel:|mailto:|#|index\.html)')


def park_ctas(html):
    """Strip href from every CTA so it renders identically but does nothing."""
    if not PARK_ALL:
        return html

    def fix(m):
        tag = m.group(0)
        if 'is-parked' in tag:
            return tag
        href = _re.search(r'href="([^"]*)"', tag)
        cls = _re.search(r'class="([^"]*)"', tag)
        classes = cls.group(1) if cls else ''
        is_cta = any(c in classes for c in ('btn', 'textlink', 'wa-float'))
        if href and _KEEP.match(href.group(1)) and not is_cta:
            return tag
        if not href and not is_cta:
            return tag

        tag = _re.sub(r'\s*href="[^"]*"', '', tag)
        tag = _re.sub(r'\s*target="[^"]*"', '', tag)
        tag = _re.sub(r'\s*rel="[^"]*"', '', tag)
        if cls:
            tag = tag.replace('class="%s"' % classes, 'class="%s is-parked"' % classes, 1)
        else:
            tag = tag.replace('<a', '<a class="is-parked"', 1)
        return tag.replace('<a', '<a aria-disabled="true" tabindex="-1"', 1)

    return _re.sub(r'<a\b[^>]*>', fix, html)
