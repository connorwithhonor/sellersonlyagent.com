# GO-LIVE Runbook — Marcela Slavik listing microsites

Everything below runs on **your** machine / accounts. This cloud session's network
blocks outbound to Netlify CLI, Cloudflare, and HonorElevate APIs, so these steps
can't be executed from here — but they're copy-paste ready.

Pages are finished + branded (Marcela Slavik · REALTOR® · Radius Agent Realty ·
CalDRE #01074602 · all CTAs → 661-877-1017) and committed to branch
`claude/zealous-curie-sOQ30`.

- `32146-green-hill/`  → **32146.aipropertysite.com**
- `30668-tick-canyon/` → **30668.aipropertysite.com**

---

## 1) Deploy to Netlify (two sites)

**Easiest — Netlify CLI (run from repo root, on your machine):**
```bash
npm i -g netlify-cli            # if not installed
netlify login

# Site A — Green Hill
netlify deploy --prod \
  --dir="mkocen-listings/32146-green-hill" \
  --message="32146 Green Hill live"
#   (when prompted: Create & configure a new site → your team → name e.g. "32146-aipropertysite")

# Site B — Tick Canyon
netlify deploy --prod \
  --dir="mkocen-listings/30668-tick-canyon" \
  --message="30668 Tick Canyon live"
#   (name e.g. "30668-aipropertysite")
```
Note each site's `*.netlify.app` URL — you'll need it for DNS.

**Alternative — Git-connected (auto-deploy on push):** In Netlify, "Add new site →
Import from GitHub → connorwithhonor/sellersonlyagent.com", then per site set
**Base directory** = the folder above and **Publish directory** = `.`. Pick the
branch you want to track.

---

## 2) DNS — point the subdomains at the Netlify sites

In **Netlify → each site → Domain management**, add the custom domain
(`32146.aipropertysite.com` / `30668.aipropertysite.com`). Then add the records
wherever **aipropertysite.com**'s DNS is managed:

**If aipropertysite.com DNS is in Cloudflare:**
| Type | Name | Target | Proxy |
| --- | --- | --- | --- |
| CNAME | `32146` | `<site-a>.netlify.app` | DNS only (grey cloud) |
| CNAME | `30668` | `<site-b>.netlify.app` | DNS only (grey cloud) |

> Keep proxy OFF (grey cloud) so Netlify can issue its own SSL. Once Netlify shows
> the domain verified, it auto-provisions Let's Encrypt.

**If aipropertysite.com DNS is inside HonorElevate** (like mkocen.com is):
HE → Settings → Domains & URL Redirects → aipropertysite.com → DNS records →
Add Record → same two CNAMEs above.

(Quick CLI version if Cloudflare-managed — replace ZONE_ID + TARGET, token from your
local env, never commit it:)
```bash
for sub in 32146 30668; do
  curl -s -X POST "https://api.cloudflare.com/client/v4/zones/$CF_ZONE_ID_AIPROPERTYSITE/dns_records" \
    -H "Authorization: Bearer $CF_API_TOKEN" -H "Content-Type: application/json" \
    --data "{\"type\":\"CNAME\",\"name\":\"$sub\",\"content\":\"$sub-aipropertysite.netlify.app\",\"proxied\":false}"
done
```

---

## 3) AI voice + chat agent (HonorElevate — mkocen subaccount)

Subaccount location id: `hE5SldwnkkfLd7VjNyVb` (PIT stored in your local env).

**A. Web chat widget on each page**
HE → the mkocen subaccount → Sites → Chat Widget → create/copy the embed snippet.
Paste it right before `</body>` in **both** `index.html` files (look for the
`<!-- LIGHTBOX -->` block; put it just below the closing `</script>`).
Commit + redeploy. (Tell me when you have the snippet and I'll wire it in.)

**B. Conversation AI behavior** — set the bot's persona/goal to:

> You are the listing assistant for Marcela Slavik (REALTOR®, Radius Agent Realty,
> CalDRE #01074602). You answer buyer questions about ONE specific home, build
> interest, capture name + phone, and push to book a showing. For anything you
> can't answer, or any motivated buyer, say you'll have Marcela follow up and
> **text/route the lead to 661-877-1017 immediately**. Never give legal/loan
> advice. Be warm, concise, local to Santa Clarita Valley. Always end by offering
> to connect them with Marcela by call or text.

**C. Knowledge base** — paste the facts so the bot answers accurately:

*32146 Green Hill Dr, Castaic 91384 — $679,999* — 2 bed / 2 bath, 1,046 sqft,
7,504 sqft lot, single-story, built 1986, Hidden Lake Tract. Engineered hardwood,
brick fireplace + custom built-ins, paneled dining room, updated kitchen (double/
convection ovens), family room off kitchen, French doors to covered patio +
fountain, QuietCool whole-house fan, central A/C + heat, primary suite w/ pet
door. Backyard: standalone cottage w/ A/C + cabinetry (she-shed/office), rose
pergola, brick pavers, large lawn, chicken coop, hills view. 2-car attached
garage. No HOA. Wm. S. Hart Union School District. MLS SR26106203. Standard sale.

*30668½ Tick Canyon Rd, Canyon Country 91387 — $699,999* — 2 bed / 1 bath, 1,050
sqft, 9.9 acres (two parcels APN 3211-020-060 & 059), built 1959, fully renovated
2024. Off-grid hilltop, panoramic city-light/hill/mountain views. New roof,
low-E dual-pane windows, new kitchen w/ quartz + ENERGY STAR appliances, bamboo
floors, crown molding. Heat-pump cooling (SEER 16+) + wood-stove heat. Main-floor
primary, walk-in closet, enclosed glass porch. Detached studio w/ in-wall heat
pump (workshop/office/guest). Two fenced horse stalls; hiking trails out the door.
Off-grid: solar electricity, conventional septic, water delivered by truck, Wi-Fi
available. Private dirt-road access, 4WD recommended. **Showings escorted, by
appointment only.** Wm. S. Hart Union School District. MLS SR26106632.

**D. Routing** — set the workflow so a captured lead fires an SMS/notification to
**661-877-1017** (Marcela's cell) with the buyer's name, number, and which listing.

---

## What I still need from you to finish
1. Where **aipropertysite.com** DNS is managed (Cloudflare or HonorElevate)?
2. The **HE chat-widget embed snippet** (so I can drop it into both pages).
3. A thumbs-up on the Netlify site names above (or your preferred names).
