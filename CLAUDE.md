# sellersonlyagent.com

## Deploy — Cloudflare Pages (MIGRATED off Netlify; Netlify retired 2026-07-01)

- **Host:** Cloudflare Pages project **`sellersonlyagent`**, account `8d19fd09c66903840c347da43306673e` (connormacivor@gmail.com), production branch `main`, **DIRECT UPLOAD** (not git-connected).
- **Deploy is MANUAL.** `git push` saves to GitHub but does **NOT** deploy the live site. To publish:
  1. Ensure git is a COMPLETE mirror of live — every live sitemap URL resolves to a local file (posts are a mix of flat `blog/<slug>.html` and folder `blog/<slug>/index.html` + `hero.jpg` + `og.png`) and every referenced local asset exists. CF Pages deploy = full-site atomic REPLACE, so a partial/stale tree WIPES live.
  2. Stage (exclude internal files) and deploy:
     ```
     rsync -a --exclude=.git --exclude=.github --exclude=CLAUDE.md --exclude=README.md ./ /tmp/soa-deploy/
     CLOUDFLARE_ACCOUNT_ID=8d19fd09c66903840c347da43306673e \
       wrangler pages deploy /tmp/soa-deploy --project-name=sellersonlyagent --branch=main --commit-dirty=true
     ```
  Full procedure + anti-wipe checklist: `claude-memory/sellersonlyagent-deploy-topology.md`.
- **RETIRED 2026-07-01:** the old Netlify pipeline is gone — removed `.github/workflows/deploy.yml` + `netlify.toml`. Old Netlify site `18ef654b-b2a8-4b5a-ba57-a3f583912792` (`sellersonlyagent.netlify.app`) is a dormant orphan; it no longer serves the domain and can be deleted in the Netlify dashboard.
- **Never deploy a partial or stale clone.** See `claude-memory/connor-deploy-safety.md`.
