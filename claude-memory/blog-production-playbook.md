# Blog Production Playbook — Connor's Daily Content Machine

_Purpose: turn Connor's daily raw material (transcripts, YouTube-binge brain-dumps, voice notes)
into fully optimized, PUBLISHED posts — the same high standard every time, with no last-mile choke.
The operational version runs as the **`/blogify`** slash command (`.claude/commands/blogify.md`).
This file is the human-readable canon + reasoning._

## The problem this solves
Connor produces ≥1 piece/day and fires it off fast. Historically the work **stalls before it goes
live** ("the posting is choked on and does not go up"). This system removes the bottleneck: Connor
dumps raw input → Kain routes, writes, optimizes, and ships via a safe additive PR → Connor approves.

## The flow (one transcript in → full package out)
0. **Route** to the best site (see router).
1. **Distill** 3–5 real hooks from the dump — titles & content anchor to these (never generic).
2. **Titles** (5, clickbait-but-true) + clean keyword **URL slug**.
3. **Write** with all four optimization layers (below).
4. **Schema** JSON-LD (Article + FAQPage + BreadcrumbList + RealEstateAgent + VideoObject).
5. **Media**: 🍌 Nano Banana (Gemini) prompts for HERO (16:9) + SOCIAL/OG (1200×630) + alt + filenames;
   responsive **video embed** slot + VideoObject.
6. **Meta**: title tag, meta description, canonical, OG/Twitter.
7. **Social repurpose pack**: X, FB, IG, LinkedIn, GBP — all linking back to drive site traffic.
8. **Publish** additively (anti-choke protocol) on a branch → PR → merge → deploy.
9. **Report** so Connor approves in ~30 seconds.

## The four optimization layers
- **SEO** — keyword in title/H1/URL/first 100 words/H2/alt; semantic variants; internal links to
  related posts + a money page; one authority outbound; scannable structure.
- **AEO** (Answer Engine) — "Quick Answer" TL;DR up top + FAQ section = snippet/answer-box bait.
- **AIEO/GEO** (AI/Generative engines) — declarative, entity-rich, quotable sentences attributed to
  Connor by name; keep `llms.txt` updated so ChatGPT/Perplexity/Gemini/Google AI cite the site.
- **Geo-local** — Santa Clarita + neighborhoods + zips + "near me"; LocalBusiness/RealEstateAgent schema.

## Title & URL rule
Titles: curiosity + benefit + specificity + local, **built from the distilled hooks**, clickbait-
leaning but TRUE. URL slug: short, keyword-rich, HONEST (clean URLs protect trust + SEO — the title
carries the click, not the URL).

## SITE ROUTER (which site gets the post)
| Signal | Destination |
|---|---|
| Buyer intent + Santa Clarita | santaclaritaopenhouses.com (buyer-intel) / scvhomebuyer.com |
| Seller intent + Santa Clarita | sellersonlyagent.com / scv123.com |
| San Fernando Valley | sfvsellersonlyagent (sellers) / SFV buyer site (future) |
| AI / business / automation | honorelevate / darkopsai / scvbots |
Tie-break: best topical-authority match; note the runner-up for Connor to override.

## SITEMAP-AWARE LINKING (internal + cross-site — "all entwined")
Read `sitemap.xml` + `blog/index.html` first to inventory every page, then:
- Relevance-matched internal links with descriptive, keyword-rich anchor text (matches the TARGET's
  topic — never "click here").
- Pillar/cluster linking for topical authority.
- ONE inbound link inserted into the 1–3 most relevant existing posts (only permitted edit to an
  existing post; single link, shown in diff).
- One money/lead-page link with descriptive anchor.
- **Cross-site network effect:** interlink Connor's properties (buyer ↔ seller, SCV ↔ SFV) with natural
  anchors to compound authority + exposure across the whole ecosystem; keep canonicals clean, no
  duplicate content.
- Add new `<url>` + `<lastmod>` to sitemap. Anchor text doubles as an AEO/AIEO/GEO relationship signal.

## ANTI-CHOKE PUBLISHING PROTOCOL (never wipe the archive)
- New post = **+1 new file**. Index update = **INSERT one card** (never regenerate index).
- Also additive: one `sitemap.xml` <url>, one `llms.txt` entry, optional homepage feature.
- Work on a branch → PR → report diff as "+N files, +M lines."
- **HARD GUARDRAIL:** if the diff changes >2 existing files or alters any existing post file, STOP and
  flag. Existing posts stay byte-identical. git history = instant rollback if ever needed.

## Growth extras (attention / fame / wealth)
E-E-A-T author box every post · topic clusters (pillar + supporting posts interlinked) for topical
authority · internal link equity → money/lead pages · repurpose each post into a video script + email
blast + social (one transcript = a week of content) · lead-capture CTA on every post.

## Access reality
Auto-publish works only for repos in-session. Now: sellersonlyagent.com ✅ · santaclaritaopenhouses.com
(repo exists, must be added) · scvhomebuyer.com (no repo yet — create it). If routed site is
inaccessible, produce the full package as drop-in files and tell Connor to add the repo.

## How to run it
Connor: type **`/blogify`** then paste the transcript (and any social update). Kain executes the flow,
opens a PR, and reports back. Connor reviews the diff + runs the two image prompts + pastes the video
embed → merge → live.
