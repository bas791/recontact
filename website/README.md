# Maximum Wash — Commercial homepage redesign

A complete, self-contained redesign of the maximumwash.co.nz homepage,
repositioning Maximum Wash as a professional **commercial** exterior cleaning
company ("One team. Nationwide. No contractors.").

**Note:** the live website's source/CMS was not available in this repository
(and the site itself is blocked by this workspace's network policy), so this
is built as a clean static package — plain HTML/CSS/JS, no build step, no
external dependencies. It can be deployed as-is, or used as the exact spec
for rebuilding the homepage inside the existing CMS (the section markup maps
one-to-one to CMS blocks).

## Files

- `index.html` — the full homepage (semantic HTML, single H1, ordered H2/H3s)
- `assets/css/main.css` — all styling; brand colours are CSS variables at the top
- `assets/js/main.js` — mobile navigation toggle (the only JS on the page)
- `assets/img/*.svg` — labelled photo placeholders (see `IMAGES-NEEDED.md`)
- `IMAGES-NEEDED.md` — exact shot list + outstanding content to confirm
- `../scripts/make_placeholders.py` — regenerates the placeholder images

Open `index.html` directly in a browser to preview.

## Page structure

1. Utility bar (phone, email, secondary **Residential Services** link)
2. Sticky header + commercial-first navigation with quote CTA
3. Hero — "Commercial exterior cleaning, delivered nationwide." + credibility bar
4. Commercial capability — "Built for commercial property."
5. Industries — 8 sector cards
6. Commercial services — 10 service cards
7. Why Maximum Wash — 6 themes (dark section)
8. Nationwide capability — copy + editable region list + NZ map (inline SVG)
9. Project showcase — 6 case-study card templates (clearly flagged placeholders)
10. Process — 5 numbered steps
11. Safety & compliance (dark section)
12. Credibility — stats + placeholder testimonials
13. Final CTA — links to the existing `/contact-us/` form (preserves current
    form handling), mailto and phone
14. Footer + sticky mobile quote bar

## Editing common things

- **Brand colours:** edit the `:root` variables at the top of `main.css`
  (`--accent`, `--navy-900`, etc.).
- **Regions:** edit the `<ul class="region-list">` items and the map dots in
  the inline SVG in `index.html` (`#nationwide` section).
- **Services / industries / projects:** each is a repeated card — copy an
  existing `<article>`/`<a>` block and edit.
- **Stats:** in the `#credibility` section. Anything marked `[confirm]` or
  with the yellow "placeholder" styling must be verified before publishing.
- **Industry card links:** currently point to `#contact`; update each `href`
  when dedicated sector pages exist.

## Facts used (and where they came from)

Verified — safe to publish:
- Regions: Auckland, Hamilton, Tauranga, Wellington, Christchurch (existing site pages)
- 8,000+ properties washed (existing site claim)
- 740+ jobs / 460+ customers in 2024, incl. 160+ commercial & organisation
  clients (this repo's 2024 ServiceM8 export)
- Phone 0800 125 135, email info@maximumclean.co.nz (existing site)

From the brief (confirm before publishing): $10M public liability insurance.

Deliberately **not** used: founding year (the current site contradicts itself
— 2015 vs 2018), revenue figures, team headcount, client names from the
ServiceM8 data (not published without permission), invented testimonials.
