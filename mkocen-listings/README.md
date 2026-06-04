# Mkocen.com Listing Microsites

Two standalone, high-converting single-property landing pages for Marcela Kocen
(Mkocen.com). All buyer traffic is driven to **call or text 661-877-1017**.

Each folder is a fully self-contained Netlify publish root (HTML + `/photos` +
`netlify.toml` + `robots.txt` + `sitemap.xml`). They are intentionally NOT part
of the sellersonlyagent.com site — they deploy as their own Netlify sites on
subdomains of mkocen.com.

| Folder | Listing | Price | Intended subdomain |
| --- | --- | --- | --- |
| `32146-green-hill/` | 32146 Green Hill Dr, Castaic 91384 · MLS SR26106203 | $679,999 | `32146.mkocen.com` |
| `30668-tick-canyon/` | 30668½ Tick Canyon Rd, Canyon Country 91387 · MLS SR26106632 | $699,999 | `30668.mkocen.com` |

## Features
- Mobile-first, dark/light theming matched to each property's mood
- Photo gallery with click-to-zoom lightbox (keyboard + swipe-friendly arrows)
- Sticky **Call** / **Text** bar on mobile; call CTA in the header on desktop
- `tel:` and pre-filled `sms:` links to 661-877-1017 throughout
- Live mortgage payment estimator
- Property facts, feature breakdowns, location, and SEO/JSON-LD schema
- Branded to Marcela Kocen / Mkocen.com with a "list your home" cross-sell

## ⚠️ Before going live (compliance)
Replace the `[DRE — pending]` placeholder in each `index.html` footer with
Marcela's actual CalDRE license number. California requires the license number
on advertised listings.

## Deploy (each folder = its own Netlify site)
Point a new Netlify site's **base/publish directory** at the folder, then add the
custom domain:
- Site A publish dir `mkocen-listings/32146-green-hill` → domain `32146.mkocen.com`
- Site B publish dir `mkocen-listings/30668-tick-canyon` → domain `30668.mkocen.com`

Add the matching `CNAME` records on mkocen.com's DNS:
```
32146  CNAME  <site-a>.netlify.app
30668  CNAME  <site-b>.netlify.app
```
Netlify auto-provisions the SSL certificate once DNS resolves.

## Photo source
Photos were extracted from the MLS PDF (640px originals) and re-encoded to
~1280px web JPGs. If higher-resolution originals exist, drop them into the
`/photos` folders with the same filenames for a sharper hero/gallery.
