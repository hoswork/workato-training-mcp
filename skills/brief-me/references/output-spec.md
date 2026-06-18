# Trainer Summary — Output Spec (Markdown-first; card HTML on request)

The Markdown is the deliverable and the source of truth. Keep it to **1–2 pages (~700–800 words)**. No tables anywhere — headings, bold labels, bullet lists, and blockquote callouts only.

## Canonical section order

1. **Title + meta header**
   - `# [Account] × Workato — Trainer Summary`
   - Bold subtitle line: `[Course] ([format e.g. 2× Half-Day], [Virtual/On-site])` · trainers · ~seats · region · dates.
   - **Ticket:** [ETT-###](url) · **Training folder:** [Google Drive](url)
   - **Workato team:** CSM [name] ([message on Slack](profile url)) · AE [name] · channel [#int_<customer>](url)
2. **At a glance** — one tinted card: ARR · active recipes · tasks/yr (success %) · agentic phase · prod-active flag.
3. **Latest activity — emails & Slack** — short email timeline (dated bullets, latest flagged), the CSM's recent account-relevant Slack items (dated, linked), then **Next action (owner)** + any OOO. Place this **above Company background**.
4. **Company background** — 3–5 sentences (who, scale, why automation matters), then an italic **"Learn more:"** line of 3–4 source links.
5. **Company POCs** — the customer stakeholders: name — role (email) — what they own / are working on (from Gong). Persona detail (e.g. "advanced builder," likely deepest questions) lives here.
6. **Training approach notes** — 3–5 data-grounded bullets (calibrate to audience, honor the customer's curriculum edits, logistics). End the section with a teal **"The opportunity:"** callout.
7. **What they were sold for training** — italic sources line, then bullets in this order: **Outcomes** → **Audience** → **Scheduling** → **Format & funding**. Then an **Agenda** label and the module groupings (Prework + modules) with the customer's edits **applied**, plus a short "Customer's edits ([date])" sub-list noting what changed/dropped.
8. **Account signals — support & engagement** — amber/red card: support tickets (severity, status), UX pains, asks, edition/upgrade constraints, ownership changes. Sourced from #int_<customer> + ticketing.
9. **Key initiatives** — 3–5 bullets of the strategic programs the training supports; label by source.
10. **Key Workato use scenarios (actual footprint)** — italic intro: "included so you're aware of their production usage … scoped to what's relevant." Bullets for the in-scope pipelines/systems + a lab tip; demote unrelated pipelines to one italic "Other production usage (context only)" line.
11. **Trainer references — product docs** — links for the **in-scope** features only (public docs.workato.com preferred). Remove links for any dropped module.
12. **Footer** — small line repeating the Ticket + Training-folder links.

> Section presence is conditional on evidence: if a source returned nothing (e.g. no Slack channel, no Gong call), keep the section short and say what was searched rather than omitting silently.

## Card HTML (generate only on request, from the finished Markdown)

Self-contained HTML, **inline styles on every element** (a `<style>` block won't survive a Google Docs paste). No tables. Wrapper: `max-width:760px; font-family:Arial,Helvetica,sans-serif; color:#334155; font-size:11pt; line-height:1.5`.

**Brand palette (hex):** TEAL `27989F`, ICE `E6F4F4`, GREY `F1F5F9`, AMBER-text `b45309` on AMBER-bg `FEF3E2`, DANGER `EF4444`, GREEN `10B981`, SLATE `334155`, link `1155cc`, muted `64748b`.

**Patterns:**
- Section heading: `<h2 style="font-size:14pt;color:#334155;border-bottom:2px solid #27989F;padding-bottom:3px;margin:18px 0 8px 0;">`
- Info / opportunity card: `<div style="background:#E6F4F4;border-left:4px solid #27989F;padding:10px 14px;margin:…">`
- Warning / signals card: same div with `background:#FEF3E2;border-left:4px solid #EF4444;` (amber/red).
- Links: `<a href="…" style="color:#1155cc;">`; emails as `mailto:` links.
- Bullets: `<ul style="margin:…;padding-left:20px;"><li style="margin-bottom:5px;">…`.
- Title wordmark as styled text (TEAL account + SLATE "× WORKATO"); **no logo image**.
- Keep background transparent/white; no page padding beyond the wrapper.
