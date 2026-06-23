# The Grown Woman Reset — Kick'N It w/ Keshia

Landing page for *The Grown Woman Reset*, a 5-week guided program for women 40+.
Single-page, fully responsive, zero build step — just static HTML, CSS, and a
little vanilla JavaScript.

## Structure

```
Website_KWK/
├── index.html        ← the entire site (inline CSS + JS)
├── favicon.svg
├── vercel.json       ← caching + clean URLs for Vercel
├── .gitignore
└── assets/
    ├── keshia.jpg              ← hero + bio portrait (optimized from 15 MB → ~950 KB)
    ├── zoom-session.jpg        ← "live" Zoom screenshot in the Program banner
    ├── ebook-cover.png         ← ebook mockup
    ├── logo-kiwk.svg           ← "Kick'N It w/ Keshia" wordmark (nav + footer)
    ├── logo-grown-woman-reset.svg
    └── fonts/                  ← optional ISOM Script brand font (see README inside)
```

## The lead form (Formspree)

The "Reset Starter" form posts to **Formspree** with no page reload. Before the
form will deliver email, you must connect your own Formspree endpoint:

1. Create a free account at <https://formspree.io> and add a new form.
2. Copy your form ID (it looks like `xrgjqlwz`).
3. In `index.html`, find the form tag and replace the placeholder:

   ```html
   <form id="leadForm" action="https://formspree.io/f/YOUR_FORM_ID" method="POST" novalidate>
   ```

   …changing `YOUR_FORM_ID` to your real ID.
4. Redeploy. Submissions now arrive in your Formspree inbox / forwarded email.

Until then the form validates and shows the success state, but mail won't be sent.

## Deploy to Vercel

**Option A — drag & drop:** zip this folder (or just upload it) at
<https://vercel.com/new>. No framework, no build command needed.

**Option B — CLI:**

```bash
npm i -g vercel        # once
cd Website_KWK
vercel                 # preview deploy
vercel --prod          # production
```

**Option C — Git:** push this folder to a GitHub repo and "Import Project" in
Vercel. Framework preset: **Other**. Build command: *(none)*. Output dir: `.`.

## Local preview

It's a static file — open `index.html` directly, or:

```bash
cd Website_KWK
python3 -m http.server 8000   # then visit http://localhost:8000
```

## Notes

- Responsive breakpoints: 1024 / 860 / 600 / 430 px, with fluid `clamp()` type
  and spacing throughout — validated 360 → 1920 px wide, no horizontal scroll.
- The countdown timer and "seats remaining" are front-end only (cosmetic urgency).
- Footer links for Privacy / Terms / SMS Consent are placeholders (`#`) — point
  them at real pages before launch.
