# GO-LIVE Runbook — Marcela Slavik listing microsites

Everything below runs on **your** machine / accounts. This cloud session's network
blocks outbound to Netlify CLI, Cloudflare, and HonorElevate APIs, so these steps
can't be executed from here — but they're copy-paste ready.

Pages are finished + branded (Marcela Slavik · REALTOR® · Radius Agent Realty ·
CalDRE #01074602 · all CTAs → 661-877-1017) and committed to branch
`claude/zealous-curie-sOQ30`.

- `32146-green-hill/`  → **32146.aipropertysite.com**
- `30668-tick-canyon/` → **30668.aipropertysite.com**

**Confirmed infra:** aipropertysite.com is hosted on **Netlify** and its **DNS is
managed inside HonorElevate**, in the "AI Property Site" subaccount
(location `ffl9iZQwLW2OAQ7nvine`). Existing records: `A @ → 75.2.60.5`,
`CNAME www → aipropertysite.netlify.app`.

---

## STEP 1 — Link each (already-created) Netlify site to GitHub

✅ **Both sites are already created** on the **Connor with Honor** team
(`connormacivor`), named to match the DNS targets:

| Site | Becomes | Site ID |
| --- | --- | --- |
| `32146-aipropertysite` | `32146-aipropertysite.netlify.app` | `5a0f141e-4fd3-41a3-895b-47ef6f80a80c` |
| `30668-aipropertysite` | `30668-aipropertysite.netlify.app` | `ce2ad1cd-7a69-4746-a281-c21690f7be60` |

They have no content yet. For **each** site, link it to the repo so Netlify pulls
+ deploys the files (no terminal, no local clone needed):

1. Netlify → open the site → **Site configuration → Build & deploy →
   Continuous deployment → Link repository**.
2. Choose **GitHub** → `connorwithhonor/sellersonlyagent.com` (authorize if asked).
3. **Branch to deploy:** `claude/zealous-curie-sOQ30`
4. **Build command:** *(leave empty)*
5. **Publish directory:**
   - `32146-aipropertysite` → `mkocen-listings/32146-green-hill`
   - `30668-aipropertysite` → `mkocen-listings/30668-tick-canyon`
6. **Save / Deploy.** First deploy runs in ~30s → the `.netlify.app` URL goes live.

(Later, when this branch is merged to `main`, switch each site's production branch
to `main` so pushes keep auto-deploying.)


## STEP 2 — Add each subdomain as a custom domain in Netlify

Netlify → Site A → Domain management → Add domain → `32146.aipropertysite.com`.
Repeat on Site B with `30668.aipropertysite.com`. Netlify will say "awaiting DNS"
— that's Step 3. SSL auto-provisions once DNS resolves.

## STEP 3 — Add the two CNAMEs in HonorElevate

HE → "AI Property Site" subaccount → Settings → Domains & URL Redirects →
**aipropertysite.com** → DNS records → **+ Add Record**:

| Type | Name | Content | TTL |
| --- | --- | --- | --- |
| CNAME | `32146` | `32146-aipropertysite.netlify.app` | Auto |
| CNAME | `30668` | `30668-aipropertysite.netlify.app` | Auto |

(If you used different Netlify site names in Step 1, use those `*.netlify.app`
hostnames as the Content.) Give DNS a few minutes; Netlify flips to "Netlify
certificate" automatically. Done — sites are live with HTTPS.

---

## STEP 4 — AI voice + chat agent (HonorElevate)

The "AI Property Site" subaccount (`ffl9iZQwLW2OAQ7nvine`) is the natural home
since the domain lives there. (mkocen subaccount = `hE5SldwnkkfLd7VjNyVb` if you
prefer to keep Marcela's leads in her own sub — your call.)

**A. Web chat widget** — HE → subaccount → Sites → Chat Widget → copy the embed
snippet. Send it to me and I'll paste it before `</body>` in both `index.html`
files and push. (Or paste it yourself just below the closing `</script>`.)

**B. Conversation AI persona/goal:**

> You are the listing assistant for Marcela Slavik (REALTOR®, Radius Agent Realty,
> CalDRE #01074602). Answer buyer questions about ONE specific home, build
> interest, capture name + phone, and push to book a showing. For anything you
> can't answer, or any motivated buyer, say you'll have Marcela follow up and
> **text/route the lead to 661-877-1017 immediately**. No legal/loan advice. Warm,
> concise, local to Santa Clarita Valley. Always offer to connect them with
> Marcela by call or text.

**C. Knowledge base (paste so answers are accurate):**

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

**D. Routing** — workflow fires an SMS/notification to **661-877-1017** with the
buyer's name, number, and which listing the moment a lead is captured.
