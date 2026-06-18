# ETT Training Ticket Structure (Jira)

Customer training requests live in the **ETT** project — "Education and Training Team Help Desk" (a Jira Service Desk, `cloudId` = `workato.atlassian.net`). Do **not** confuse this with **ETTP** ("Education and Training Team Projects"), which holds internal content-development tasks, not customer engagements.

The relevant issue type is **`[ETT] Instructor Led Training`**. Each ticket is a structured intake form; the customer's training folder (with the proposal deck) is linked in a custom field.

## Finding the customer's ticket

```
project = ETT AND issuetype = "[ETT] Instructor Led Training" AND (description ~ "[Account]" ORDER BY created DESC)
```

If the account custom field is queryable in the environment, also try `cf[11014] ~ "[Account]"`. If multiple tickets match, prefer the most recent with a populated Drive folder field. Always confirm the match by reading the account field and contact email.

> Fetch the matched ticket with `fields: ["*all"]` and `expand: renderedFields`. The output can be large — extract just the fields below.

## Field map (verified on ETT-588, Circle)

Custom-field IDs can drift across instances — treat these as the expected layout and **verify by value**, not blind trust.

| Field ID | Meaning | Example (ETT-588) |
|----------|---------|-------------------|
| `customfield_16230` | **Training folder — Google Drive link** (proposal lives here) | `https://drive.google.com/drive/folders/1nCL3wwcdfQ0za7mU5ENd4iVYEAdhfBPc` |
| `customfield_11014` | Account / company name | `Circle` |
| `customfield_11015` | Customer contact name | `Michael Murphy` |
| `customfield_11016` | Customer contact email | `michael.murphy@circle.com` |
| `customfield_11008` | Seat count / attendees | `12` |
| `customfield_11009` / `description` | Training needs free-text (audience, topics, goals) | Foundations, MCP, Agent Studio, Decision models; IT Genie / IT-Admin Genie |
| `customfield_15115` | Training start date/time | `2026-06-08T09:00:00` |
| `customfield_15116` | End | `Friday 5:00 PM` |
| `customfield_15118` | Timezone | `EDT` |
| `customfield_16267` | Region | `AMER-EAST` |
| `customfield_11020` | Delivery format | `Virtual` |
| `customfield_11048` | Training type | `Customized Training` |
| `customfield_15081` | Funding / engagement type | `Private - Paid` |
| `customfield_11038` | Approvers | Mary Gabriola, Ryan Koh, Samuel Seetoh |

The **contact email domain** (e.g. `@circle.com`) is the customer domain — use it for the Gmail and Slack searches.

## From ticket to proposal

1. Read `customfield_16230` → Google Drive **folder** ID (the trailing path segment, e.g. `1nCL3wwcdfQ0za7mU5ENd4iVYEAdhfBPc`).
2. `list_folder_items` on that folder (`corpora: allDrives`, include files). Identify the **training proposal** — typically a Google Slides/PDF/Docs file whose name contains "Proposal", "Training", or the account name.
3. Read it with `get_file_content`. Extract the **sold training scope**: topics/modules, format, day/session count, audience, seat count, dates, pricing/PS-hours conversion, and any commitments.
4. If the folder has no clear proposal, list everything and use the most proposal-like document; note the ambiguity. If `customfield_16230` is empty, fall back to Gong + ticket free-text and state that no Drive proposal was found.
