# sellersonlyagent.com

## Deploy — git is canonical (since 2026-05-21)
- **Netlify ID:** 18ef654b-b2a8-4b5a-ba57-a3f583912792
- **Deploy mechanism:** auto-deploy from this repo's `main` branch via `.github/workflows/deploy.yml`. Push = deploy.
- **Snapshot-API uploads are FORBIDDEN.** See `claude-memory/connor-own-sites-git-canonical.md`.
- **Build config:** `netlify.toml` at repo root. HTML post-processing disabled.

See `claude-memory/connor-own-sites-git-canonical.md` for the full policy.

## Memory — Talie Knutson / With Heart Marketing (client)
### Chat widget build ("Joy") — HonorElevate (GHL) + Netlify
- **One bot, named "Joy"**, built in **HonorElevate (GHL)**. **Text/typing only — NO voice** (Talie confirmed on the call).
- **Three placements, three different intros**: (1) main site, (2) blog homepage, (3) individual blog article.
- **Blog = on GHL/HonorElevate** (versions 2 & 3 publish there). **Main site = Netlify** (version 1 = embed snippet).
- **Netlify site = DIRECT DEPLOY (no git repo). BE CAREFUL** — live deployed files are source of truth; inject only the widget snippet before `</body>`, snapshot/back up first, never clobber existing content.
- Avatar: NOT the default stock brunette; generate fresh, Talie picks. Slight response delay so it feels human.
- **Recaps must be per-location**: Talie wants a recap of each interaction labeled by WHICH placement it came from (main / blog-home / article). This is why we build 3 separate widgets (each tags its own source) rather than one generic widget.

### Weekly report mechanics (learned from the Friday Recon process)
- Cadence: **"Friday Recon" → "WHM Weekly Report" PDF** saved to Drive `/Current Honor Elevate Clients/Talie Knutson/Weekly Traffic Reports/`. Style: 700pt wide, navy/gold, **no em dashes** (grep-verified), 6-week trend table.
- Data pulled: **HE Blog Analytics** (GHL location `SjX08lFAklJvmyrEqmyY`) — pageviews, published-post count, device split, brand categories (Clarity/Rise/Root/Reveal/Alignment/Consistency/Connection/Health&Wellness/Radiate), top-10 ranked posts. Plus **Netlify production deploy** state (project `whm03092026`, siteId `a50b93c7-1ae8-464b-94dd-ee1a8fe47c85` → withheart-marketing.com).
- HE blog numbers are **browser-scraped visually** (canvas-rendered, not in DOM, no API). Recon runs on Mac-V (browser control + Netlify MCP). NOT reproducible from a plain Claude Code web session.
- **CONFLICT to resolve**: historically GSC/GA4 were skipped per Talie's "no Google data" rule. Talie asked for GA on 2026-06-01; Connor asked for GSC on 2026-06-04. That reverses the rule — confirm Talie is OK with Google data in the report, and connect GSC/GA (not currently connected in Windsor).

### Weekly recap report ("Friday recap") — what the report must include
- **Include Google Search Console intel** in the report (added 2026-06-04 per Connor). Query/page impressions, clicks, positions.
- **Include Google Analytics metrics** — site visits + user flow (where people go). (From 2026-06-01 call.)
- **Drop the CTA-button line** from the per-article template — Talie already adds her own CTA twice (mid + end of each article), so it's redundant. (From 2026-06-01 call.)
