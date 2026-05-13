# Listing Page Workflow

Every Sellers Only Agent listing gets a custom landing page at `sellersonlyagent.com/listings/<slug>/`. This is The Listing System Component #2.

## The example

`/listings/example/` is the canonical template. It is marked with a top banner identifying it as an example and has `meta robots="noindex"` so Google does not index it. Sellers and prospective sellers can be sent to this URL to see exactly what their home's page would look like.

## Creating a new listing page

1. **Copy the example:**
   ```bash
   SLUG="25600-bridgeport-lane"   # use the address as the slug
   cp -r ~/dev/sellersonlyagent.com/listings/example "~/dev/sellersonlyagent.com/listings/$SLUG"
   ```

2. **Edit the new `index.html`:**
   - Remove the example banner at the top (the `<div class="example-banner">` block)
   - Remove the `<meta name="robots" content="noindex, follow" />` line so the real listing IS indexed
   - Update the `<title>`, `<meta description>`, `<meta canonical>`, and Open Graph tags with the real address
   - Replace placeholder content in:
     - The hero (address-line, h1 headline, tagline)
     - The price-bar (price + bed/bath/sqft/lot/year/garage)
     - The photo-grid (swap placeholders for real `<img>` tags using Cloudinary/CDN URLs)
     - The three narrative variants (lifestyle, investor, relocation)
     - The video-row with real embed URLs (replace each `<div class="video-card">` with a `<video>` or `<iframe>`)
     - The facts-grid (MLS #, year built, lot, HOA, taxes, Mello Roos, schools)
     - The two neighborhood panels (real walkable amenities, real commute times)
     - The comp table (real recent sales)
     - The calc-card default values (real price + down payment + rate)

3. **Add the listing-specific JSON-LD schema** in the `<head>`:
   ```html
   <script type="application/ld+json">
   {
     "@context": "https://schema.org",
     "@type": "SingleFamilyResidence",
     "name": "25600 Bridgeport Lane, Stevenson Ranch CA 91381",
     "address": {
       "@type": "PostalAddress",
       "streetAddress": "25600 Bridgeport Lane",
       "addressLocality": "Stevenson Ranch",
       "addressRegion": "CA",
       "postalCode": "91381"
     },
     "numberOfBedrooms": 4,
     "numberOfBathroomsTotal": 3.5,
     "floorSize": { "@type": "QuantitativeValue", "value": 2684, "unitCode": "FTK" },
     "yearBuilt": "2008",
     "offers": {
       "@type": "Offer",
       "price": "1189000",
       "priceCurrency": "USD",
       "availability": "https://schema.org/InStock",
       "seller": {
         "@type": "RealEstateAgent",
         "name": "Connor MacIvor",
         "url": "https://sellersonlyagent.com",
         "telephone": "+16614001720"
       }
     }
   }
   </script>
   ```

4. **Deploy:**
   ```bash
   cd ~/dev/sellersonlyagent.com
   git add listings/$SLUG && git commit -m "Add listing: $SLUG"
   netlify deploy --prod --dir=. --site=18ef654b-b2a8-4b5a-ba57-a3f583912792 \
     --message="New listing: $SLUG"
   git push origin main
   ```

5. **Wire the listing into the system:**
   - Add a row to `~/dev/sellersonlyagent.com/listings/index.html` (active listings hub — TODO build this)
   - Update the seller dashboard tracking (HonorElevate workflow with this listing URL)
   - Add the listing URL to every social post, ad, email, and showing request
   - Run the daily content cadence from `~/dev/connor-palace/_memory/playbooks/multi-platform-shorts-publishing-system.md` referencing this URL

## Photo + media sourcing

Photo URLs should point to a fast CDN, not the GHL `assets.cdn.filesafe.space` host (it serves uncompressed). Options:
- **Cloudinary** — recommended for transformations (auto-format, resize, crop, lazy)
- **Cloudflare R2** via the `cwh-files` worker — see `~/local-memory/claude-memory/cwh-files-worker.md`
- **Netlify built-in CDN** — drop photos in `/listings/<slug>/photos/` and reference relatively

Hero photo: twilight exterior, drone overhead, or wide-angle hero shot.
Photo count: 30 to 60 for full coverage.

## Video sourcing

Three formats per listing:
- 60-second reel for Instagram/TikTok/Shorts
- 3-minute YouTube tour
- 8-minute deep-dive embedded on this page

Host video either on YouTube (unlisted but embeddable) or directly via Cloudinary's video delivery.

## Seller preview workflow

Before the listing goes live, send the seller the `sellersonlyagent.com/listings/<slug>/` URL with the `noindex` tag still on. They preview, request edits, approve, then the `noindex` line is removed in the same commit that takes the photos public.

## Future automation

The next stage of this is a `_template/` directory with a Mustache or Jinja-style template plus a `listing.json` per home, processed by a build script. For now, copy + edit is faster and gives Connor direct control over each page.

---

Built 2026-05-13. The example at `/listings/example/` is the source of truth — when the template needs to change, change it there first, then propagate to active listings.
