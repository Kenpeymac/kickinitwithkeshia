ISOM Script font (optional brand flourish)
==========================================

The headings and the "reset." script flourish look for a font called
"ISOM Script". It is NOT included in this repo (we don't have a license file
for it here), so the site automatically falls back to Pinyon Script — which
looks great and is loaded from Google Fonts.

If you have the licensed ISOM Script font files, drop them in THIS folder:

    assets/fonts/ISOM-Script.woff2   (preferred — smallest/fastest)
    assets/fonts/ISOM-Script.otf     (fallback)

No code changes needed — the site will pick them up automatically on the next
deploy. A .woff2 is ideal; if you only have a .otf or .ttf, you can convert it
for free at https://cloudconvert.com/otf-to-woff2 .
