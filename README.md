# NutraNurture — Akanksha Bhargava

Static website for a clinical nutrition practice (Ahmedabad + online).
Plain HTML, one stylesheet, one small script. No build step, no framework, no
dependencies. Upload the folder to any host — Netlify, Vercel, cPanel, S3,
GitHub Pages.

## Pages

| File | Purpose |
|---|---|
| `index.html` | Home — hero, credentials, two care paths, six areas of care, four-step process, philosophy, experience, testimonials |
| `about.html` | Biography, qualifications, internships, research and community work |
| `services.html` | The four-step journey, four programmes, consultation formats |
| `corporate.html` | Corporate wellness and pharma/hospital partnership offerings |
| `stories.html` | Client testimonials and the Google Reviews link |
| `contact.html` | Contact details and the inquiry form |
| `styles.css` | The whole design system |
| `main.js` | Mobile menu, header shadow, fade-in, inquiry form (133 lines) |
| `assets/` | `logo.jpg`, `akanksha.jpg` |

## Run locally

```bash
python3 -m http.server 4173
```

Then open http://127.0.0.1:4173

## Design

The palette is sampled directly from `assets/logo.jpg`:

| Role | Colour | Where it comes from |
|---|---|---|
| Primary | `#BE2A1C` brick red | the figure and the wordmark |
| Secondary | `#5EA11D` leaf green (`#3E6D13` for text) | the leaves |
| Accent | `#F0A81C` wheat gold | the grain and fruit |
| Ground | `#FFFBF5` / `#FBF3E8` warm cream | the logo's own background |
| Ink | `#2A1F1A` warm near-black | — |

Type is chosen to echo the hand-lettered wordmark: **Lora** for headings and
pull-quotes (a warm calligraphic serif, used in italic for eyebrows and the
tagline voice) over **Mulish** for body copy (rounded, friendly, very legible).

Shapes follow the logo too — circular portraits, pill buttons, 16–24px radii,
and leaf-shaped bullets instead of dots.

### Imagery

The site ships with two real images: the logo and one photograph of Akanksha.
They are used in the nav, the footer, the home hero and the About page.

Everywhere else that needed a picture, `assets`-free **SVG illustrations drawn
in the logo's style** fill the gap (see the generator at
`scratchpad/art.py` if you want to edit them):

- a **wreath of leaves and berries** ringing the hero portrait, echoing the mark
- three **circular illustrations** in the "Real Food. Real Routines." row — a
  plated meal, a cooking pot with wheat, and a growing sprout

These are placeholders in the honest sense: they are on-brand, but real
photographs would be stronger. See "Photographs to supply" below.

### What the site deliberately does NOT do

These were removed because they get in a visitor's way:

- No scroll hijacking — the page scrolls exactly as the browser intends.
- No preloader — content is visible immediately.
- No custom cursor, no page-transition animation, no pinned horizontal section.
- No animated number counters — the figures are plain text in the HTML, so they
  are correct even if the script never runs.

What remains is a short fade-up as sections enter view, which is disabled
entirely under `prefers-reduced-motion: reduce`. With JavaScript switched off
the site still renders and reads completely.

### Usability details worth keeping

- The mobile menu button is labelled **Menu**, not a bare hamburger.
- The headline and booking button come before the portrait on phones.
- Every button and form field is at least 50px tall.
- Body text is `#4A4E73` on white (7.6:1) and the indigo accent is 8.6:1 — both
  pass WCAG AA comfortably.
- Focus rings are visible on every interactive element for keyboard users.
- A "Skip to main content" link is the first thing a screen reader reaches.
- Optional form fields are marked *(optional)* rather than starring the required
  ones.

## Photographs to supply

Send these and I will drop them straight in — the slots are already laid out:

| Slot | What works best |
|---|---|
| Home — "Real Food. Real Routines." ×3 | Square photos: a plated Indian meal, a home kitchen or market produce, and a consultation in progress |
| Home — client stories ×3 | Optional headshots, or leave the initials treatment |
| About — research & community ×3 | Camp, workshop or seminar photographs |
| Corporate — the six offering cards | A webinar screen, an on-site desk, a health-camp table |
| Consultations — the two formats | One in-clinic photo, one video-call screenshot |

Square or 4:5 crops, 1200px on the long edge, JPG. Drop them in `assets/` and
tell me the filenames.

## Before going live — three things to fill in

1. **Social links.** Instagram and Facebook are `href="#"` placeholders in the
   top bar and footer of every page:

   ```bash
   grep -n 'href="#"' *.html
   ```

2. **The inquiry form has no backend.** It opens the visitor's email client
   pre-filled and addressed to `akanksha.bhargava81@gmail.com`, so nothing is
   lost. To post it to a real service instead, set `FORM_ENDPOINT` near the
   bottom of `main.js` — the fetch path is already written.

3. **Two numbers to confirm.** The source document said "20+ years" in one place
   and "over 15 years" in another; the site uses **20+** everywhere. The home
   page also states **1000+ clients counselled**, which is the document's
   "counselled thousands of clients" written as a figure. Change either if you
   would rather not state them.

## Editing note

`styles.css` and `main.js` are linked with a `?v=8` cache-busting query. Bump it
in all six HTML files whenever you change either file, or returning visitors
will keep the old cached copy:

```bash
sed -i '' 's/?v=8/?v=8/g' *.html
```
