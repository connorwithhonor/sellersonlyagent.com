# CRMLS IDX / API Inquiry — Status & Strategy

_Last updated: 2026-06-02. Owner: Connor MacIvor (CalDRE #01238257). This note exists so we
never have to re-discover where this work lives. The IDX work itself is NOT code in this repo —
it's an email + paperwork process (CRMLS support ticket **API-127**) plus the lead-gen sites it
will feed._

## Key IDs (CONFIRMED 2026-06-02 from a SYNC MLS listing detail sheet)
- **SYNC Brokerage CRMLS Office ID: `SR207023513`** ← this is the **Trestle "Broker ID"** to enter.
- **SYNC broker-of-record DRE (LO State License): `02031490`** ← fallback for the Broker ID field.
- Connor agent: CRMLS User ID `F210006440`, DRE `01238257`.
- Trestle wizard: Business Type = **Broker**, Multiple Listing Organization = **California Regional MLS**.
- DO NOT USE (old brokerage Realty One Group): Office ID `SRf7001242`, Office DRE `01015471`.
  Also dead: `02113158` (didn't match SYNC).

## Players
- **Matt Coonis** — Licensing Supervisor at **REcore** (recore.net), `licensing@recore.net`,
  909.859.2040. The gatekeeper for the CRMLS API/IDX feed. Friendly and helpful.
- **CoreLogic Trestle** — distributes CRMLS data for the API feed. Broker registers there.
- **Broker of record: Andres Hoyos**, **SYNC Brokerage** (`andres@syncbrokerage.com`).
- **Patrick** (former broker contact, moved on / Texas).
- Ticket: **API-127** ("API for CRMLS"), open since Dec 2024.

## The path to approval (per Matt)
1. Complete the **Broker Participant Data License Order Form & Agreement**
   (https://recore.net/participant-data-license-order-form-and-agreement/). Permitted Use =
   **Broker BBO (back-office)**.
2. Broker (Andres) registers on **CoreLogic Trestle**.
3. Notify Matt → he sends the **WebAPI feed connection invite**.
- First two Trestle feeds are **free** for a CRMLS broker participant.

## Timeline
- **Dec 2024** — Opened API-127. Matt explained the process above.
- **May 2025** — Submitted a CRMLS IDX Request Form for santaclaritaopenhouses.com under
  then-broker Patrick Raach. Matt: that form is for approved IDX vendors; gave 3 options
  (framed links / approved vendor / direct RESO Web API).
- **Brokerage change** → now SYNC Brokerage, broker Andres Hoyos.
- **2026-05-27** — Sent Andres the pre-filled IDX Request Form + 1-page SYNC Broker Brief.
  ✅ **Andres signed via DocuSign the same day** ("SYNC_Broker_Brief_IDX_Authorization.docx").
- **2026-05-28/29** — Reopened API-127 (Loom video). Matt sent updated Order Form link;
  process unchanged.
- **2026-06-02** — Submitted Order Form + Data Licensing Agreement.
  ⛔ **Matt rejected the listed website URLs**: `scvmls.com` and `sfvmls.com` contain "mls",
  which violates **CRMLS Rule 12.20** (can't imply you ARE / operate an MLS).

## The blocker & the rule
**CRMLS Rule 12.20 — Use of the Terms MLS and Multiple Listing Services:** No Participant or
Subscriber shall, through firm name, URLs, email addresses, or website addresses, represent,
suggest, or imply that they are / operate an MLS, or that consumers have direct access to MLS
databases. (It DOES allow saying that authorized info "is available on their websites.")

Related (about on-page display once live, NOT the domain name):
- **19.2.3 Control** — must control the site; reasonable consumer understands it's the broker's.
- **19.2.9 Display Purpose** — IDX listings for display only (search-engine indexing is allowed).
- **19.2.13 Website Identification** — must clearly show brokerage firm (SYNC) + subscriber
  (Connor) in readily visible font/color.

Note: 12.20 is a **CRMLS contract rule, not trademark law.** (Separately, CLAW owns
"TheMLS™" / themls.com — a *different* MLS. Irrelevant to us; "MLS" is generic, so descriptive
use in our copy is fine. Just never brand a site "TheMLS" and never scrape themls.com.)

## The fix (decided 2026-06-02)
Swap the rejected domains for two compliant ones Connor **already owns** (no purchase needed):
- ✅ **santaclaritaopenhouses.com** (already on file w/ CRMLS from 2025)
- ✅ **scvhomebuyer.com**

Reply to Matt was drafted in Connor's voice and **saved as a Gmail draft on the API-127 thread**
(asks Matt whether to resubmit the form or swap URLs on his end; confirms Andres ready for Trestle).
**No full re-paper needed** — only the website-URL field changes; the signed Data Licensing
Agreement body is unchanged. Andres can re-initial via DocuSign in seconds only if Matt asks.

## Strategy — "king of the MLS searches" (12.20-safe)
CRMLS controls the *domain name*, not the *rankings*. Win "Santa Clarita MLS" / "SFV MLS" search
demand on compliant domains by phrasing the promise correctly:
- ✅ Titles/H1: "Santa Clarita **MLS Listings**", "[City] homes **from the MLS**"
- ✅ Body: "search **homes / listings**", "sourced from the MLS"
- ❌ Never: "search the **MLS database**" / "direct access to the MLS"
- ✅ Every page shows **SYNC Brokerage + Connor MacIvor** (19.2.13)

Site roles:
- **santaclaritaopenhouses.com** — SCV open-house + browse; city pages (Valencia, Saugus,
  Newhall, Canyon Country, Stevenson Ranch, Castaic); IDX embed once approved.
- **scvhomebuyer.com** — SCV buyer-journey angle (no overlap).
- **SFV expansion** — own `vannuysopenhouses.com`; recommended new compliant domain
  **sfvhomebuyer.com** (available — mirrors scvhomebuyer.com). Also free: sfvlistings.com,
  sanfernandovalleyhomebuyer.com, sfvhomeforsale.com.

## Open next steps
- [ ] Send the Matt reply (draft is parked in Gmail).
- [ ] After Matt OK: Andres registers in Trestle → Matt sends API invite.
- [ ] Add 19.2.13 broker attribution + non-solicitation footer to both sites before feed goes live.
- [ ] (Optional) Register sfvhomebuyer.com for the SFV play.
- [ ] Keyword research blocked — connected Ahrefs plan lacks Keywords Explorer ("Insufficient
      plan"). Alternative: pull Google Search Console data for existing sites.
