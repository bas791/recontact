# Adding the commercial homepage to the existing WordPress site

Every button and link on the page now points at real pages on
maximumwash.co.nz (contact form, commercial hub, service pages, region
pages), so it behaves as part of the site wherever it's installed.

## Where the links go

| Element | Destination |
|---|---|
| All quote / portfolio / contact CTAs (hero, nav, final section, mobile bar) | `/contact-us/` — the existing form, so enquiries flow through the current setup |
| All 8 industry cards | `/commercial-parent/` — the existing commercial hub page |
| Footer: Commercial Building Washing | `/auckland/commercial-building-washing/` |
| Footer: Gutter Clearing & Flushing | `/auckland/commercial-gutter-cleaning/` |
| Footer: Roof Treatments & Washing | `/commercial-roof-cleaning/` |
| Footer: Rope Access Cleaning | `/hamilton/commercial-abseiling/` |
| Footer: Exterior Window Cleaning | `/commercial-parent/` (no dedicated page found — update when one exists) |
| Footer region links | `/auckland/`, `/hamilton/`, `/tauranga/`, `/wellington/`, `/christchurch/` |
| Residential Services (top bar + footer) | `/` (current homepage) |
| Nav items (Services, Industries, Projects…) | Jump to sections on this page |

To change any destination, search `index.html` (or `page-commercial.php`)
for the label text and edit its `href`.

## Install as a real WordPress page (recommended)

You get a normal page in the WordPress admin — it appears in menus, can be
set as the site's front page, and keeps this design under any theme.

1. **Upload the assets.** Using FTP or the hosting File Manager, copy the
   `assets` folder to:
   `wp-content/uploads/maximumwash-commercial/assets`
   (final result: `.../uploads/maximumwash-commercial/assets/css/main.css` etc.)
2. **Add the template to the theme.** Copy `wordpress/page-commercial.php`
   into the **active theme's folder** (Appearance → Theme File Editor shows
   its name, e.g. `wp-content/themes/your-theme/`). If the site uses a child
   theme, put it there so theme updates don't delete it.
3. **Create the page.** Pages → Add New → title it "Commercial". In the page
   settings sidebar under **Template**, choose **"Commercial Homepage"**.
   Publish. Leave the content area empty — the template supplies everything.
4. **View it** at `/commercial/` (the page's slug). Add it to the main menu
   via Appearance → Menus.
5. **Make it the site homepage (when ready):** Settings → Reading → "Your
   homepage displays: A static page" → select "Commercial". The current
   homepage remains available to link as Residential.
6. **Analytics:** paste the GA/GTM snippet into the marked
   `<!-- ANALYTICS -->` block near the top of `page-commercial.php`
   (the template bypasses the theme's header, so it won't inherit the tag).

## Alternative: static folder (no WordPress changes)

Extract the zip into a `commercial/` folder inside `public_html` — the page
is then live at `/commercial/` with zero WordPress involvement. Same links,
same behaviour; it just won't appear in the WP admin or menus.

## Notes

- A few footer links use region-specific service pages (Auckland/Hamilton)
  because those are the confirmed existing URLs — swap them if national
  service pages are created.
- The template deliberately skips the theme's header/footer so the design
  can't be broken by theme CSS. The trade-off: plugins that auto-inject
  scripts (analytics, chat widgets, cookie banners) won't load on this page
  — paste anything needed into the ANALYTICS block.
