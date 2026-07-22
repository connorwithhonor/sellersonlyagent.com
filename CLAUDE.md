# ☠️ DEAD REPO. DO NOT BUILD OR DEPLOY HERE.

**This is the orphan.** The live site is served from the repo with **no `.com`**:

- ✅ LIVE: `connorwithhonor/sellersonlyagent`
- ☠️ THIS: `connorwithhonor/sellersonlyagent.com`

## Evidence (measured 2026-07-22 against the live homepage)

| repo | index.html | delta vs live | homepage title |
|---|---|---|---|
| `sellersonlyagent` | 65286 | **1875 bytes** | matches live |
| `sellersonlyagent.com` (this) | 80317 | 13156 bytes | different |

## Why your instincts fail here

This is the third instance of the same trap on this account (see
`santaclaritaartificialintelligence.com`, now archived). In that case the DEAD repo
had the NEWER commit date, so "most recently updated" pointed at the wrong repo.
Repo name, title, and recency are all unreliable. **Byte-compare `index.html`
against the live homepage. That is the only check that has ever worked.**

Full context: `claude-memory/scai-repo-topology-trap.md`
