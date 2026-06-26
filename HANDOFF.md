# Handoff — The Grown Woman Reset landing page

_Last updated: 2026-06-23_

A single-page marketing site for **The Grown Woman Reset**, a 5-week coaching
program for women 40+ led by Keshia (brand: *Kick'N It w/ Keshia*).

---

## 1. Live site & deploy

- **Public URL (share this):** <https://grown-woman-reset.vercel.app>
- **Vercel project:** `grown-woman-reset` (account `kenpeymac-3022`)
- **Redeploy after changes:**
  ```bash
  cd Website_KWK
  vercel --prod --yes
  ```
- ⚠️ The long hashed deploy URL (`grown-woman-reset-xxxx…vercel.app`) is **behind
  Vercel's login wall (HTTP 401)** — never share that one. Always share the clean
  alias above.
- Clean URLs are on (`vercel.json`), so `/privacy.html` 308-redirects to `/privacy`.
  All legal pages resolve 200 at their clean paths.

## 2. Stack & structure

No build step. Static HTML/CSS/JS. The whole homepage is one self-contained file
with inline `<style>` and `<script>`.

```
Website_KWK/
├── index.html          ← entire homepage (inline CSS + JS)
├── privacy.html        ┐
├── terms.html          ├ legal pages (shared inline styling; noindex)
├── sms-consent.html    ┘
├── favicon.svg
├── vercel.json         ← cleanUrls + asset cache headers
├── README.md           ← deploy / local-preview instructions
├── HANDOFF.md          ← this file
├── scripts/gen_image.py← one-off Gemini image-gen helper (not used at runtime)
└── assets/
    ├── keshia.jpg            ← hero photo (also referenced where the leaning shot is needed)
    ├── keshia-bio.jpg        ← "Meet Keshia" bio portrait (real editorial photo, tulle gown)
    ├── zoom-session.jpg      ← "live" Zoom screenshot in the Program banner laptop
    ├── ebook-cover.png       ← ebook mockup ("PIVOT Like You Mean It")
    ├── logo-kiwk.svg         ← "Kick'N It w/ Keshia" wordmark (nav + footer, CSS-mask recolored)
    ├── logo-grown-woman-reset.svg ← Program-banner logo (CSS-mask recolored)
    └── fonts/                ← optional ISOM Script drop-in (see README inside)
```

Local preview: `python3 -m http.server 8000` then open <http://localhost:8000>.

## 3. Brand / design system

- **Palette:** soft blush page, white cards, deep-plum text, **raspberry** accent
  (headings/script), **bright pink** reserved for buttons, **deep magenta** Program
  banner. All defined as OKLCH custom properties in `:root` in `index.html`.
- **Type:** Playfair Display (display serif) + Pinyon Script (the "reset." flourish)
  via Google Fonts. An optional licensed **ISOM Script** falls back to Pinyon — drop
  files in `assets/fonts/` to enable (see `assets/fonts/README.txt`).
- **Responsive:** fluid `clamp()` type/spacing; breakpoints at 1024 / 860 / 600 /
  430px. Verified 360→1920px, no horizontal scroll.
- Full brand spec: `brand-spec.md` in the **parent** folder (one level up).

## 4. Page sections (in order)

Sticky nav → Hero → Outcomes ("The shift" before/after reveal) → Program banner →
Pricing (4 tiers) → Meet Keshia → Testimonials → Ebook → Join form + FAQ → Final
CTA → Footer.

### Notable interactive / dynamic bits
- **"The shift" reveal** (Outcomes): a before→after wipe. It now **sweeps open
  automatically as you scroll the panel up the page** (and reverses scrolling up),
  so no one misses it. Manual drag / tap / arrow-keys takes over permanently once
  used. Respects `prefers-reduced-motion`.
- **Countdown** (Program banner): counts down to a **real fixed date** —
  `new Date('2026-08-05T00:00:00')` in the JS. **To reuse for the next cohort, change
  that one date string.** Label reads "Enrollment closes · cohort begins August 5".
- **Floating petals:** soft blush petals drift via scroll parallax behind the hero
  and final CTA only. Subtle by design; hidden under `prefers-reduced-motion`.
- **Watermarks:** big faint tone-on-tone brand words — GROWN/WOMAN in the Program
  banner, script "Keshia" in the footer, script "reset" in the Ebook section.
- **Monogram avatars:** hero trust row + testimonials use T/D/M initials (tied to the
  three named member quotes) instead of stock/fake faces.

## 5. ⚠️ Open items before real launch

These are the things standing between "great preview" and "launch":

1. **Lead form → GHL (Go High Level).** Formspree is **NOT** being used (decision
   2026-06-23). The form in `index.html` still has a leftover placeholder action
   `action="https://formspree.io/f/YOUR_FORM_ID"` + a `fetch()` handler — **this
   needs to be replaced with the GHL form embed.** GHL has no simple POST endpoint;
   the plan is to paste in the GHL form's **embed code** (iframe or inline script)
   and remove the Formspree leftover. Until then the form validates and shows a
   success state but sends nowhere.
2. **Checkout / payment.** All four pricing buttons + the ebook button currently just
   scroll to the lead form (`#join` / `#ebook`) — **the site cannot take money yet.**
   Needs a real path (Stripe Payment Links, or a course platform like GHL/Kajabi).
   The pricing copy was softened so it no longer claims a "secure checkout" exists.
3. **Legal pages = boilerplate, not lawyer-reviewed.** `privacy.html`, `terms.html`,
   `sms-consent.html` are solid templates with a `<!-- TEMPLATE -->` note and
   `[bracketed]` placeholders (governing state, mailing address). Have them vetted
   and fill the blanks. They're `noindex` until finalized.
4. **Hero quote wording** is *suggested* copy in Keshia's voice — she should approve
   the exact words (or send her own). It's the card on the hero photo, "— Keshia".
5. **ISOM Script font** (optional) — falls back to Pinyon Script if absent.

## 6. This session's changelog (newest first)

| Commit | Summary |
|--------|---------|
| `746b602` | Center Program banner right column to balance the layout |
| `a806d58` | Remove 'Limited enrollment / 12 seats' block from Program banner |
| `9c6f37f` | Hero quote: make it Keshia's voice, not a misattributed client quote |
| `b802d73` | Refine watermarks: trim banner, add footer + ebook texture |
| `858609e` | Add tone-on-tone branded watermark texture to Program banner |
| `a42fd16` | Add scroll-driven 'shift' reveal + floating-petal parallax |
| `5d1165f` | Make 'The shift' reveal pop: bigger headlines + warm/pale contrast |
| `93f2281` | Polish hero headline: split empathy line from the promise |
| `ec9de94` | Add legal pages + honest pricing copy |
| `0dbf866` | Use real editorial portrait of Keshia for bio (replaces AI-generated) |
| `e0e65d6` | (superseded) AI-generated bio portrait |
| `7e20a87` | Make scarcity real: fixed Aug 5 countdown + honest seat-cap copy |
| `71c0123` | Replace fake avatars with monogram initials (hero + testimonials) |
| `64def33` | Polish: balance Program banner columns |
| `fcf24d8` | Initial commit: Vercel-ready landing page |

**Theme of the session:** took an already-polished export and made it *trustworthy* —
removed AI/funnel "tells" (fake avatars, self-resetting countdown), grounded the
scarcity in real facts (12 seats, Aug 5), swapped in a real founder photo, added
honest legal pages, then layered in texture (watermarks, petals) and motion
(scroll-driven reveal) without sacrificing the calm, premium white space.

## 7. Notes / gotchas for the next person

- **One file.** Editing the homepage = editing `index.html`. CSS and JS are inline.
- **Layout rule:** multi-column sections center the shorter column against the taller
  one (`align-items:center`), except the Join/FAQ grid which is top-aligned because
  the form card is `position:sticky`.
- **Raw AI image outputs** live in `nanobanana-output/` (git-ignored) — not used; the
  bio photo is the real `assets/keshia-bio.jpg`.
- **Vercel auth on deploy URLs:** see §1. Share only the clean alias.
- Brand context for `/impeccable` design work: women 40+, faith-rooted, sisterly;
  honest over hype; avoid trendy/young-skewing, corporate/clinical, scammy-funnel.
