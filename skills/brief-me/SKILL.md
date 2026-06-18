---
name: brief-me
description: Use when a trainer asks to be briefed on a customer training engagement — "brief me on [account]", "trainer summary for [account]", "prep me for [account] training". Generates a concise 1–2 page Trainer Summary from Jira (ETT ticket → Drive training proposal), Enterprise Data (Snowflake footprint), Gong, Gmail, Slack (#int_ channel + CSM), and web. Outputs Markdown first (source of truth); card-based Google-Docs-pasteable HTML only on request. Workato-internal, trainer audience only.
metadata:
  version: "2.0"
---

# Brief Me — Workato Trainer Summary

Produces a tight trainer briefing for a named customer training: enough for a trainer to walk in prepared, and no more.

## Working in a Project

**Run this skill inside a Claude Desktop Project named for the engagement** (e.g. `[Account] — [Course] Training`). Multi-source data gathering is expensive without caching; Project instructions cache automatically.

Project Instructions template:
```
Engagement: [Account] — [Course], [Date]
ETT ticket: [link]
Drive folder: [link]
brief-me skill active. Read the working folder for any prior briefing before starting a new pass.
```

## MCP prerequisites

This skill requires the following MCPs to be configured in Claude Code or Cowork:

| MCP | What it provides | BT registry |
|---|---|---|
| Atlassian | Jira ETT ticket | All |
| Google Drive | Training proposal + Drive folder | Everyone |
| Enterprise Data (Snowflake) | Production footprint | Everyone |
| Gong | Call recordings + transcripts | Everyone |
| Gmail | Email timeline | Everyone |
| Slack | #int_ channel + CSM signals | Everyone (needs auth) |

All are BT-managed. To configure missing MCPs in Claude Code: run the `workato-setup` skill or see https://workato.atlassian.net/wiki/spaces/extbt/pages/2510848002/Internal+MCPs+BT+Managed

## Output principles (read first)

- **Length:** short — target **1–2 pages (~700–800 words)**. Cut, don't pad.
- **Format:** **Markdown is the source of truth.** Generate the HTML version **only when the user asks** ("make the HTML"), and build it *from the finished Markdown*.
- **No tables in the deliverable.** Use headings, bold labels, bullet lists, and cards (see `references/output-spec.md`). The HTML uses inline-styled card `<div>`s for Google Docs paste.
- **Evidence only.** Report what the sources support; cite each source inline. If a connector or MCP is unavailable, say so and proceed — never fabricate to fill a gap.
- **Always link back** to the ETT ticket and Google Drive training folder (header and footer).
- **Second sweep (required).** After any scope or fact change, re-scan the entire document for every dependent mention and update them all.

**Output filename:** `[Account] - Trainer Summary.md` (and `[Account] - Trainer Summary.html` only when requested).

---

## Step 1 — Confirm account + locate the ETT ticket

Resolve the exact account in Enterprise Data (`DIM_ACCOUNT`, see `references/data-queries.md`). Find the customer's training ticket in the **ETT** Jira project; see `references/ett-ticket-structure.md` for JQL and the field map. Capture logistics, customer contact + email domain (drives Gmail/Slack searches), and the Drive folder link in `customfield_16230`. Keep the ticket URL for the always-on links.

## Step 2 — Read the training proposal (Google Drive)

From `customfield_16230`, open the Drive folder, find the **training proposal** (and any Discovery/Event-kit docs), and extract the sold scope: outcomes, audience, agenda/modules, format, seats, dates, funding/PS-hours. This is the primary "what they were sold."

## Step 3 — Footprint (Enterprise Data by Workato MCP)

Use the 5-step semantic-layer flow (`start_session` → `get_analyst_context` → `get_semantic_layer_index` → `get_semantic_models` → `execute_sql_query`); see `references/data-queries.md`. Pull real production pipelines, top connectors/recipes, environments. Frame as awareness of their production usage, scoped to what's relevant to the training. Look up connector names in `references/connector-catalog.md`.

## Step 4 — Company background (web; Salesforce optional)

Search the web for the company profile; confirm identity by the contact's email domain. Capture founding, HQ, leadership, products, scale, recent news, and *why automation matters to them*. Collect a few "Learn more" source URLs. If Salesforce MCP is connected, add CRM context; otherwise note its absence.

## Step 5 — Gong

Run the 3-strategy ladder (account-filtered → trainer-participant → open keyword). Capture the training proposal call especially. Extract scope discussed, initiatives, and per-POC context (what each customer stakeholder is working on / asking about). Flag scope discrepancies vs. the proposal.

## Step 6 — Gmail

Search emails from the customer domain and threads involving the CSM/AE/trainers. Build the email timeline for "Latest activity" and confirm the current next action (who owns it) and any OOO that affects scheduling.

## Step 7 — Slack

Read `#int_<customer>` and filter the CSM's recent messages for account-relevant items. Get the CSM's Slack profile link. Pull account signals: support tickets, product/UX pains, asks, edition/upgrade constraints, ownership changes.

## Step 8 — Build the Trainer Summary (Markdown)

Write `[Account] - Trainer Summary.md` following the section structure in `references/output-spec.md`. Apply curriculum edits to the agenda itself (don't just describe them). Remove out-of-scope modules everywhere they appear — run the second sweep. Include trainer product-doc links only for in-scope features.

## Step 9 — HTML on request only

If the user asks for HTML, generate `[Account] - Trainer Summary.html` from the finished Markdown per the card-HTML spec in `references/output-spec.md` (inline styles, no tables, Google-Docs-pasteable).

## Step 10 — Save and present

Save to the working folder and present the Markdown (plus HTML if requested).

---

## Logging

At completion, invoke: `skill-logger brief-me` (if available; skip silently if not).

## Tape

At the end of a session where this skill produced a meaningful output, offer to run `the-tape` if any decisions were made that overrode or extended these standards.

> "Want to capture any decisions to the tape?"

Skip silently if `the-tape` is not installed.
