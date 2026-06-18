import json

ADDIE_PROMPTS = {
    "01-customer-voice": """---
title: Customer Voice & Proof Point Research
addie_phase: Project Prep
prompt_order: 1
confluence_page_id: 2434007423
confluence_version: 3
confluence_version_date: 2026-05-06
synced: 2026-06-04
source: https://workato.atlassian.net/wiki/spaces/ETT/pages/2434007423
---

**ADDIE Phase:** Project Prep (Pre-Analyze)

**Purpose:** Ground instructional content in authentic customer language, pain points, success stories, and quantifiable outcomes. This prompt transforms abstract learning goals into customer-informed design decisions.

**Position:** This is the **first deliverable** in the ADDIE pipeline. It has no upstream dependencies — run it at the very start of a new course or learning path. Its output feeds directly into Audience Profile, Needs Analysis, Learning Objectives, Detailed Outline, Script Drafting, Knowledge Checks, and Storyboarding.

## When to use:

* **Before everything else.** Run this prompt at the start of a new course or learning path, before Needs Analysis, before Audience Profile, before anything. It produces the customer data foundation that every downstream deliverable builds on.
* **Before Design:** Downstream prompts (Script Drafting, Knowledge Checks) will retrieve this brief and extend it with lesson-specific research. Running Customer Voice first means those prompts start from real data instead of re-running broad research from scratch.
* **Review with SMEs:** Share findings with product team SMEs to validate interpretations before the data flows downstream.
* **Before Knowledge Check generation:** Use confusion patterns and real scenarios to create authentic assessment questions
* **Privacy:** Always anonymize customer details in learning content unless explicitly approved for external use
* **Refresh cadence:** Re-run this research every 6 months or when major product updates occur

### No upstream inputs required

This prompt queries data sources directly. You just need:

* The course/feature topic
* Access to Gong, Salesforce, Highspot, Google Drive, and Slack (via Otto/MCP)

## Prompt

````markdown
You are researching customer perspectives on **[product/feature/capability]** to inform instructional design for Workato Academy. Your goal is to extract authentic customer voice, identify real pain points, document success patterns, and gather quantifiable proof points that will ground learning content in actual business value.

This research brief is the **first deliverable in the ADDIE pipeline** — its output will be retrieved and consumed by every downstream prompt (Audience Profile, Needs Analysis, Learning Objectives, Outline, Scripts, Assessments, Storyboard). Structure your output precisely as specified below so downstream prompts can reference sections by letter.

#### Step 1: Search Customer Conversations

Using Gong, search for customer calls that mention **[product/feature]** from the past 6 months. Look for:
- Discovery calls where customers describe their problems before considering Workato
- Implementation calls where customers work through configuration or adoption challenges
- Success calls where customers describe outcomes and value realized
- Troubleshooting calls that reveal common confusion points or misunderstandings

**Search parameters:**
- Keywords: [product/feature name], [related capabilities], [use case terms]
- Timeframe: Last 6 months (or specify custom range)
- Call types: Discovery, implementation, QBR, troubleshooting
- Target: 10-15 calls minimum for pattern recognition

#### Step 2: Extract Pain Points (Pre-Adoption)

For each relevant call, document:
- **Customer's exact language** describing their problem (use direct quotes)
- **Business impact** they describe (time wasted, errors, manual work, compliance risk)
- **What they tried before** (workarounds, competitor tools, manual processes)
- **Trigger event** that made them seek a solution (new regulation, growth, acquisition, incident)

**Output format:**
```
Pain Point Theme: [Descriptive label]
Customer Quote: "[Exact words from call]"
Business Impact: [Quantified when possible]
Context: [Company size, industry, use case]
Source: [Gong call ID and date]
```

#### Step 3: Extract Success Stories (Post-Adoption)

For customers who successfully adopted the feature, document:
- **Value realized** in their own words (direct quotes)
- **Quantifiable outcomes** (time saved, error reduction, cost savings, speed improvement)
- **Before/after workflows** they describe
- **Surprising benefits** they mention (unintended positive outcomes)
- **What made it successful** (their perspective on why it worked)

**Output format:**
```
Success Story: [Customer name/segment]
Outcome Quote: "[Exact words describing value]"
Metrics: [Quantified improvements]
Use Case: [Specific workflow or business process]
Success Factors: [What made this work]
Source: [Gong call ID and date]
```

#### Step 4: Identify Common Confusion Points

Analyze troubleshooting and implementation calls to find:
- **Concepts customers misunderstand** (what do they think it does vs. what it actually does?)
- **Configuration mistakes** they commonly make
- **Questions they repeatedly ask** across multiple calls
- **Gaps between expectation and reality**

**Output format:**
```
Confusion Pattern: [What customers misunderstand]
Evidence: [Quotes or call references]
Frequency: [How often this appears across calls]
Implication for learning design: [What this means for how we teach]
```

#### Step 5: Query Salesforce for Adoption Metrics

Search Salesforce for accounts with strong adoption of **[feature]**. Pull:
- **Account names** (for potential reference with permission)
- **Industry and size** (for persona relevance)
- **ARR growth** correlated with feature adoption
- **Time-to-value metrics** (days from activation to first meaningful usage)
- **Expansion opportunities** enabled by the feature

**If specific metrics fields exist, query for:**
- Tasks automated per week
- Hours saved per user per month
- Error rate reduction percentages
- Workflow completion time improvements

#### Step 6: Review Existing Proof Points in Highspot

Search Highspot for:
- Customer success stories already documented
- Case studies featuring **[product/feature]**
- Sales deck proof points and statistics
- Competitive win stories mentioning this capability

**Document:**
- What proof points already exist and are approved for external use
- What customer names/logos can be referenced
- What metrics are already validated by Marketing/Sales
- Gaps between what Sales needs and what exists

#### Step 7: Synthesize for Instructional Design

Consolidate all research into the structured output sections below. **Use the exact section letters and headers** — downstream prompts reference them by letter.

---

### Output Deliverable: Customer Voice Research Brief

Begin the document with this metadata header:

```
---
Document: Customer Voice Research Brief
Course/Path: [name]
Topic: [product/feature]
Date: [date generated]
Data sources queried: [list — e.g., Gong (12 calls), Salesforce (account data), Highspot (3 case studies), Slack (#solutions-engineering, #product-x)]
Recommended refresh: [date + 6 months]
---
```

---

#### Section A: Pain Point Summary

3–5 primary pain themes customers express, ranked by frequency.

For each pain point:
- **Theme label:** [Descriptive name]
- **Frequency:** [How many calls/sources mention this — e.g., "7 of 12 calls"]
- **Representative quote:** "[Exact customer words]" — Source: [Gong call ID]
- **Business impact:** [Quantified when possible]
- **Persona relevance:** [Which persona(s) this pain point most affects, if distinguishable]

**Downstream use:** Needs Analysis consumes these to ground the performance gap analysis. Script Drafting uses quotes to open lessons with real customer language. Detailed Outline uses pain themes to sequence content around real problems.

**🔵 Confidence:** [High / Medium / Low] — [Basis: number of sources, consistency of pattern, recency of data. What would change it.]

---

#### Section B: Success Story Library

3–5 compelling customer examples with metrics.

For each story:
- **Label:** [Customer segment or anonymized reference]
- **Before state:** "[Customer's own words describing the problem]" — Source: [ID]
- **After state:** "[Customer's own words describing value realized]" — Source: [ID]
- **Metrics:** [Quantified improvements — time, cost, error rate, etc.]
- **Use case:** [Specific workflow or business process]
- **Success factors:** [What made this work, from the customer's perspective]
- **Approved for external use?** Yes / No / Needs approval — [note any Highspot case study match]

**Downstream use:** Script Drafting uses these as concrete examples in narration. Storyboarding uses them for scenario blocks. Proof points flow into Knowledge Check scenario stems.

**🔵 Confidence:** [High / Medium / Low] — [Basis and what would change it]

---

#### Section C: Customer Language & Use Case Inventory

##### C1: Language Patterns
How customers naturally talk about this topic.

- **Terms they use:** [Customer language] vs. **terms we use:** [Product/marketing language]
- **Metaphors and analogies they make:** [How they explain it to their own teams]
- **How they describe the value:** [Common phrases]
- **Jargon they don't use:** [Product terms that don't resonate or confuse]

##### C2: Use Case Inventory
5–7 real customer workflows or use cases.

For each:
- **Use case label:** [Brief title]
- **Workflow description:** [What the customer actually does]
- **Business value:** [Why it matters to them]
- **Persona type:** [Which persona this represents]
- **Source:** [Gong call ID, Salesforce account, or Highspot asset]

**Downstream use:** Script Drafting uses C1 to match narration tone to how customers actually talk. C2 provides real scenarios for Outline, Scripts, and Knowledge Checks. Audience Profile uses C1 to validate persona descriptions.

**🔵 Confidence:** [High / Medium / Low] — [Basis and what would change it]

---

#### Section D: Misconception & Confusion Inventory

**This is the most heavily consumed section in the pipeline.** Structure each misconception as a discrete, numbered item — downstream prompts (Audience Profile, Learning Objectives, Detailed Outline, Knowledge Checks) each pull from this inventory for different purposes.

For each misconception:

```
D[#]. [Short label]

Misconception: [What customers believe that is incorrect or incomplete]
Correct understanding: [What is actually true — 1-2 sentences]
Why they hold it: [What experience, analogy, or prior product behavior created this mental model]
Frequency: [How often this appears — e.g., "5 of 12 calls", "recurring in #solutions-engineering"]
Severity: [How much damage does this misconception cause if unaddressed? High = blocks task completion or causes errors. Medium = leads to suboptimal usage. Low = minor misunderstanding with limited impact]
Persona relevance: [Which persona(s) most commonly hold this misconception, if distinguishable]
Evidence: [Gong call ID, Slack thread, or SME interview reference]
Learning design implication: [What this means for how we teach — e.g., "Must be addressed before teaching X because the misconception will interfere with learning Y"]
```

After listing all misconceptions, add:

**Misconception threading guide:** For each misconception, note where in the pipeline it should be addressed:
- **Audience Profile:** Mapped to persona in Section 2C
- **Learning Objectives:** Generates a corrective learning objective
- **Detailed Outline:** Placed in a specific lesson/section at the right point in the sequence
- **Knowledge Checks:** Used as a realistic distractor with rationale

**🔵 Confidence:** [High / Medium / Low] — [Basis: number of independent sources per misconception, consistency across calls, SME validation status. Note: flag any misconception supported by fewer than 2 sources as "low confidence — verify with SME."]

---

#### Section E: Proof Point Quick Reference

10–15 validated statistics, metrics, and quotable data points for use in narration, on-screen text, and assessments.

For each proof point:
- **Stat or quote:** [The proof point as it would appear in content]
- **Source:** [Salesforce report / Highspot case study / Gong call ID]
- **Approved for external use?** Yes / No / Needs approval
- **Recency:** [Date of source data]
- **Context needed:** [Any caveats — e.g., "specific to Enterprise segment", "based on self-reported data"]

**Downstream use:** Script Drafting incorporates these into narration. Storyboarding uses them for on-screen text and data callouts. Knowledge Checks use metrics in scenario stems.

**🔵 Confidence:** [High / Medium / Low] — [Basis and what would change it]

---

### Document-Level Confidence Statement

> **🔵 Overall Confidence: [High / Medium / Low]**
> [2–3 sentences: How many data sources were queried. How many calls/accounts/assets were reviewed. Which sections are strongest. Which sections have thin data and need SME validation or additional research. What would increase confidence — e.g., "Section D has only 2 supporting sources for misconceptions D3 and D5 — additional Gong calls or a Slack search in #customer-success would strengthen these."]

---

### Appendix: Source Log

List every data source reviewed with enough detail for downstream prompts and SMEs to verify:

| Source Type | Source ID / Link | Date | What was extracted | Section(s) it informed |
|---|---|---|---|---|
| Gong call | [Call ID] | [Date] | [Brief note — e.g., "Discovery call — pain points, misconceptions"] | A, D |
| Salesforce | [Report/Account] | [Date] | [Brief note] | B, E |
| Highspot | [Asset title] | [Date] | [Brief note] | B, E |
| Slack | [Channel + thread link] | [Date] | [Brief note] | D |
| Drive | [Doc title] | [Date] | [Brief note] | C |

---

Write in clear, professional prose. Use the section headers and letters exactly as specified — downstream prompts reference sections by letter (e.g., "retrieve Customer Voice Section D"). Flag any section where data is thin with **[LOW DATA — needs additional sources]** and explain what's missing.
````

### Downstream consumers

| Consumer | What it retrieves | Which section(s) |
| --- | --- | --- |
| **Audience Profile** | Misconceptions mapped to persona | Section D |
| **Needs Analysis** | Pain point themes, usage baseline, existing content, strategic context | Sections A, E + extends with scoping-specific queries |
| **Learning Objectives** | Misconceptions → corrective objectives | Section D |
| **Detailed Outline** | Misconception placement, pain points for scenario design | Sections A, D |
| **Script Drafting** | Success stories, proof points, customer language, real scenarios | Sections B, C, E + extends with lesson-specific examples |
| **Knowledge Checks** | Misconceptions as distractors, real failure scenarios | Section D + extends with lesson-specific failure modes |
| **Storyboarding** | Proof points for on-screen text, real scenarios for scenario blocks | Sections B, C, E |
""",
    "02-content-audit": """---
title: Content Audit & Gap Analysis
addie_phase: Project Prep
prompt_order: 2
confluence_page_id: 2467004727
confluence_version: 4
confluence_version_date: 2026-05-06
synced: 2026-06-04
source: https://workato.atlassian.net/wiki/spaces/ETT/pages/2467004727
---

**ADDIE Phase:** Project Prep (Pre-Analyze) runs early — parallel with or shortly after Customer Voice

**Purpose:** Prevent redundancy, identify reusable content, understand what already exists, and surface gaps before investing in new content creation. This prompt maps the existing knowledge ecosystem so instructional design decisions are informed by what's already available.

**Position:** Runs at the start of a new course or learning path, alongside Customer Voice and Usage Data. Can run independently, but produces a stronger gap analysis if Customer Voice has already been completed (pain points and use cases help evaluate whether existing content addresses the right problems). Its output feeds Needs Analysis, Audience Profile, Detailed Outline, Script Drafting, and Storyboarding.

### When to use

* **After Customer Voice (preferred) or in parallel.** If Customer Voice has already run, this prompt retrieves pain points and use cases to evaluate existing content against real customer needs — not just topic coverage. If Customer Voice hasn't run yet, this prompt still works, just with a less targeted gap analysis.
* **Before Needs Analysis.** The content inventory and stability assessment feed directly into the Needs Analysis Module Scope Map (content status and stability ratings).
* **Before Detailed Outline.** Reuse opportunities and stability flags inform which lessons can leverage existing content and which topics need careful handling.
* **When consolidating or sunsetting old content.** The redundancy assessment identifies what to deprecate when new content launches.

### Optional upstream artifact

* **Customer Voice Research Brief** — specifically Section A (Pain Points) and Section C2 (Use Case Inventory). If available, Content Audit uses these to evaluate whether existing content addresses the problems and workflows customers actually care about. If not available, Content Audit evaluates content by topic coverage only.

````
You are conducting a comprehensive content audit for **[product/feature/topic]** to inform instructional design decisions for Workato Academy content. Your goal is to map what content already exists across all organizational repositories, assess its quality and relevance, identify gaps, and recommend what to reuse vs. create from scratch.

This content audit is an **early-pipeline deliverable** — its output will be retrieved and consumed by Needs Analysis, Detailed Outline, Script Drafting, and Storyboarding. Structure your output precisely as specified below so downstream prompts can reference sections by letter.

### Step 0: Retrieve Upstream Artifacts (if available)

Before beginning the audit, check whether a **Customer Voice Research Brief** exists for this course. The user will tell you where it lives (file path, Confluence page, or Google Doc).

**If available, retrieve and hold:**
- Section A (Pain Point Summary) — the 3–5 pain themes customers express
- Section C2 (Use Case Inventory) — the 5–7 real customer workflows

**How to use these during the audit:**
- When evaluating existing content (Steps 1–5), assess not just "does content on this topic exist?" but "does existing content address the pain points and use cases customers actually have?"
- In the Gap Analysis (Section B), flag gaps where existing content covers the topic but misses the customer's actual problem or workflow
- Tag any gap analysis finding that was informed by Customer Voice data as "[CV-informed]" for traceability

**If the Customer Voice brief doesn't exist yet:** Proceed with the audit — evaluate content by topic coverage. Note in Section B that gap analysis could be strengthened by running Customer Voice research.

---

#### Step 1: Search Internal Documentation (Google Drive)

Search Drive for existing documentation on **[product/feature/topic]**:
- **Query terms:** "[feature] guide", "[feature] documentation", "[feature] how-to", "[feature] training", "[product] setup", "[product] best practices"
- **File types:** Docs, Slides, PDFs, Sheets (for matrices or decision frameworks)
- **Folders to check:** Product documentation, Solutions Engineering, Customer Success, Academy archives

**For each relevant document found, record:**
- Title and Drive link
- Owner/author
- Last updated date
- Content summary (2–3 sentences: what does it cover?)
- Target audience (internal/external, persona, skill level)
- Format (long-form doc, quick reference, video walkthrough, diagram)
- Quality assessment (accurate? current? well-structured? or outdated/incomplete?)

#### Step 2: Search Sales/Marketing Content (Highspot)

Search Highspot for customer-facing or sales enablement content:
- **Query terms:** Same as Step 1, plus "[feature] pitch", "[product] demo", "[feature] competitive"
- **Content types:** Pitch decks, product sheets, demo videos, battle cards, customer decks

**For each relevant asset found, record:**
- Title and Highspot link
- Content type (pitch, demo, one-pager, etc.)
- Last updated date
- What positioning/messaging does it use? (how is the feature framed for customers?)
- What proof points or examples does it include?
- Quality assessment (approved? current? or needs refresh?)

#### Step 3: Search Internal Discussions (Slack)

Search relevant Slack channels for recent discussions about **[product/feature]**:
- **Channels to check:** #product-[name], #solutions-engineering, #customer-success, #academy-internal, #enablement
- **Query terms:** "[feature]", "[product] release", "[feature] update", "[feature] issue", "[feature] question"
- **Timeframe:** Last 6 months

**Document:**
- Threads discussing **product updates** (new capabilities, deprecations, breaking changes)
- Threads discussing **known issues** or **workarounds**
- Threads where **SMEs answer technical questions** (reveals what's confusing)
- Threads showing **customer feedback** or requests for better documentation/training

**Key insights to extract:**
- Is the product stable or rapidly evolving?
- What are recent changes that existing content may not reflect?
- What do internal teams wish was documented better?
- What technical nuances or edge cases are commonly discussed?

#### Step 4: Review Existing Academy Modules

Start with the **Education Content Inventory** spreadsheet as the primary source of existing Academy courses and modules:
- **Location:** [Google Sheets — Education Content Inventory](https://docs.google.com/spreadsheets/d/1rFV2drpfTBI8JfkSluKKET_GMsQPM-fC2g4_vKf-6Tc/edit?gid=170263460#gid=170263460)
- Read the spreadsheet via Google Drive and filter for courses related to **[product/feature/topic]** — check course titles, descriptions, and topic tags.

**Important:** This inventory may not be fully up to date. After reviewing it, cross-check by searching Confluence (ETT space) and Google Drive for any recently launched or in-development courses that may not have been added to the inventory yet. If you find courses missing from the inventory, flag them in your output so the inventory can be updated.

**For any related modules found (from the inventory or other sources):**
- Module title and link (Docebo link if available, or Confluence project page)
- What learning objectives does it cover?
- What overlap exists with the new module being planned?
- What prerequisite knowledge does it establish that the new module can build on?
- What content could be cross-referenced vs. duplicated?
- **Inventory status:** [In inventory / Missing from inventory — flag for update]

#### Step 5: Assess External Workato Resources

Check public-facing resources:
- **Workato Docs** (docs.workato.com): Official product documentation
- **Community** (community.workato.com): User discussions, troubleshooting threads
- **Blog** (workato.com/the-connector): Thought leadership, use case articles

**Document:**
- What official documentation exists? Is it comprehensive or sparse?
- What community questions/threads show user confusion?
- What blog content could be repurposed or linked?

#### Step 6: Synthesize Findings

Consolidate all research into the structured output sections below. **Use the exact section letters and headers** — downstream prompts reference them by letter.

---

### Output Deliverable: Content Audit & Gap Analysis Report

Begin the document with this metadata header:

```
---
Document: Content Audit & Gap Analysis Report
Course/Path: [name]
Topic: [product/feature]
Date: [date generated]
Upstream artifacts used: [e.g., "Customer Voice Research Brief (dated [X])" or "None — Customer Voice not yet available"]
Sources searched: [list — e.g., Google Drive, Highspot, Slack (#solutions-engineering, #product-x), Academy catalog, Workato Docs, Community]
Recommended refresh: [date + 6 months, or sooner if product is rapidly evolving]
---
```

---

#### Section A: Content Inventory

Full table of all existing assets found across all sources.

| # | Content Asset | Type | Location | Owner | Last Updated | Target Audience | Quality | Pain Points Addressed | Reusable? |
|---|---|---|---|---|---|---|---|---|---|
| A1 | [Title] | [Doc/Deck/Video/etc.] | [Link] | [Author] | [Date] | [Persona / skill level] | [Current / Outdated / Incomplete] | [List pain point themes from CV Section A this addresses, or "Not evaluated" if CV not available] | [Yes / Partial / No] |

**Downstream use:** Needs Analysis consumes this to set "Content status" per module (Exists / Adapt / Net-new). Detailed Outline references specific assets for reuse per lesson.

**🔵 Confidence:** [High / Medium / Low] — [Basis: how thoroughly each source was searched, whether all relevant repositories were accessible. What would change it.]

---

#### Section B: Gap Analysis

For the planned course/module, map what's covered vs. what's missing.

##### B1: Topics with existing coverage
For each topic/objective that existing content addresses:
- **Topic:** [What's covered]
- **Covered by:** [Asset # from Section A]
- **Coverage quality:** Complete / Partial / Outdated
- **Customer relevance:** [If CV available: Does this content address the pain points and use cases customers actually have? Or does it cover the topic from a different angle?] [CV-informed] or [Topic-only assessment]

##### B2: Gaps — topics with no existing coverage
For each topic/objective that no existing content covers:
- **Gap:** [What's missing]
- **Why it matters:** [Impact on learning if this gap isn't filled]
- **Customer relevance:** [If CV available: Does this gap align with a documented pain point or use case?] [CV-informed] or [Not evaluated]
- **Build priority:** High / Medium / Low

##### B3: Gaps — existing content that's outdated or misleading
For each piece of existing content that's no longer accurate:
- **Asset:** [Reference from Section A]
- **What's wrong:** [Outdated info, incorrect procedures, deprecated features]
- **Risk if not addressed:** [What happens if a learner or colleague encounters this?]
- **Recommended action:** Update / Deprecate / Replace with new module

**🔵 Confidence:** [High / Medium / Low] — [Basis and what would change it]

---

#### Section C: Redundancy Risk Assessment

Identify overlap that could cause confusion or duplicate effort.

For each redundancy found:
- **Redundancy type:** Direct overlap / Partial overlap / Conflicting framing
- **Assets involved:** [References from Section A]
- **Risk:** [What goes wrong if both exist — e.g., "Learners encounter conflicting instructions on configuring X"]
- **Recommended resolution:** Consolidate / Deprecate one / Scope boundaries clearly / Cross-reference

**🔵 Confidence:** [High / Medium / Low] — [Basis and what would change it]

---

#### Section D: Reuse Opportunities

Categorize existing assets by recommended action.

##### D1: Reuse as-is
Assets that can be linked or embedded directly without modification.
- **Asset:** [Reference from Section A]
- **Use in new course:** [Where/how — e.g., "Link as prerequisite reading before Module 2"]

##### D2: Adapt / Update
Assets that are 80%+ there but need refresh or reframing.
- **Asset:** [Reference from Section A]
- **What needs changing:** [Specific updates needed]
- **Estimated effort:** Low / Medium
- **Use in new course:** [Where/how]

##### D3: Repurpose
Assets where specific elements (diagrams, examples, proof points, screenshots) can be extracted.
- **Asset:** [Reference from Section A]
- **Element to extract:** [What specifically]
- **Use in new course:** [Where/how]

##### D4: Replace / Deprecate
Assets that should be sunset when the new course launches.
- **Asset:** [Reference from Section A]
- **Why:** [Outdated / superseded / causing confusion]
- **Deprecation plan:** [Archive? Redirect? Delete?]

**Downstream use:** Detailed Outline references D1–D3 when specifying reusable assets per lesson. Storyboarding uses D3 for existing visual assets.

**🔵 Confidence:** [High / Medium / Low] — [Basis and what would change it]

---

#### Section E: Freshness & Stability Assessment

**This section is consumed by every downstream prompt that produces content.** Structure it as a per-topic stability profile so downstream prompts can apply the right flag to each lesson or script section.

##### E1: Overall Product Stability
- **Product/feature:** [Name]
- **Stability status:** Stable / Actively evolving / In beta / Undergoing major redesign
- **Recent changes (last 6 months):** [List significant updates, releases, or deprecations found in Slack and docs]
- **Upcoming changes (if known):** [Roadmap items mentioned in Slack or SME conversations]
- **Documentation currency:** [Is official documentation keeping pace with product changes?]

##### E2: Per-Topic Stability Ratings

For each major topic or capability the course will cover:

```
E2.[#]. [Topic/capability name]

Stability rating: [Evergreen / Moderately Stable / High Maintenance]
  - Evergreen: Core concept unlikely to change. Safe to teach definitively.
  - Moderately Stable: Implementation details may shift, but concepts hold.
    Teach concepts; be cautious with specific UI steps.
  - High Maintenance: Actively changing. Screenshots will go stale.
    Teach principles and patterns; flag specific steps as version-sensitive.

Last verified: [Date of most recent source confirming current state]
Evidence: [What sources inform this rating — Slack threads, release notes, doc update dates]
Known upcoming changes: [If any — "None known" is a valid answer]
Downstream flags:
  - Outline: [Should this topic carry a ⚠️ stability flag in the lesson?]
  - Script: [Should the script prefer concepts over specific UI steps?]
  - Storyboard: [Should screenshots carry version-sensitivity flags in production notes?]
```

##### E3: Maintenance Burden Forecast
- **Estimated update frequency:** [How often will this course need content refreshes — quarterly? Biannually? Only on major releases?]
- **Highest-risk sections:** [Which topics/modules will need updates most frequently?]
- **Maintenance trigger:** [What event should prompt a content review — e.g., "Any release note mentioning [feature]"]

**Downstream use:** Needs Analysis consumes E2 ratings for the Module Scope Map stability column. Detailed Outline applies ⚠️ stability flags to lessons covering Moderately Stable or High Maintenance topics. Script Drafting uses E2 downstream flags to decide whether to write concept-focused or procedure-focused narration. Storyboarding uses E2 downstream flags to set version-sensitivity on screenshots. The future Course Maintenance Genie inherits E2 and E3 for post-publication drift detection.

**🔵 Confidence:** [High / Medium / Low] — [Basis: How many sources confirm each stability rating. How recent is the evidence. What would change it — e.g., "Stability rating for [topic] is Medium confidence — based on Slack discussion from 3 months ago. A quick check with SME would confirm whether the Q3 release changed this."]

---

### Document-Level Confidence Statement

> **🔵 Overall Confidence: [High / Medium / Low]**
> [2–3 sentences: How thoroughly sources were searched. Whether any major repositories were inaccessible. Which sections are strongest. Which sections have gaps — e.g., "Academy catalog search was comprehensive but Highspot returned sparse results — Sales may have content in a different location. Section E stability ratings for [topics X and Y] need SME confirmation."]

---

### Appendix: Source Log

| Source Type | Source / Link | Date Accessed | What was found | Section(s) it informed |
|---|---|---|---|---|
| Google Drive | [Doc title / link] | [Date] | [Brief note] | A, B, D |
| Highspot | [Asset title / link] | [Date] | [Brief note] | A, B, E |
| Slack | [Channel + thread] | [Date] | [Brief note] | E |
| Academy | [Module title] | [Date] | [Brief note] | A, B, C |
| Workato Docs | [Page / section] | [Date] | [Brief note] | B, E |
| Community | [Thread / topic] | [Date] | [Brief note] | B |

---

Write in clear, professional prose. Use the section headers and letters exactly as specified — downstream prompts reference sections by letter (e.g., "retrieve Content Audit Section E2"). Flag any section where data is thin with **[LOW DATA — needs additional sources]** and explain what's missing.
````

## How this prompt connects to the pipeline

| Upstream Source | What Content Audit retrieves | How it's used |
| --- | --- | --- |
| **Customer Voice Section A** (Pain Points) | Optional — retrieved in Step 0 | Evaluates whether existing content addresses real customer pain points, not just topic coverage |
| **Customer Voice Section C2** (Use Cases) | Optional — retrieved in Step 0 | Evaluates whether existing content covers real customer workflows |

### Downstream consumers

| Consumer | What it retrieves | Which section(s) |
| --- | --- | --- |
| **Needs Analysis** | Content status per module, stability ratings, existing content gaps | Sections A, B, E |
| **Audience Profile** | Stability data for prerequisite confidence assessment | Section E |
| **Detailed Outline** | Reuse opportunities per lesson, stability flags per topic | Sections D, E |
| **Script Drafting** | Stability flags — scripts for unstable topics prefer concepts over specific UI steps | Section E |
| **Storyboarding** | Stability flags → version sensitivity on screenshots | Section E |
""",
    "03-usage-data": """---
title: Usage Data-Informed Design Decisions
addie_phase: Project Prep
prompt_order: 3
confluence_page_id: 2446033027
confluence_version: 3
confluence_version_date: 2026-05-06
synced: 2026-06-04
source: https://workato.atlassian.net/wiki/spaces/ETT/pages/2446033027
---

**ADDIE Phase:** Project Prep (Pre-Analyze) runs early — parallel with or shortly after Customer Voice

**Purpose:** Use actual product usage patterns, adoption metrics, and behavioral data to prioritize learning content, identify where users struggle, and sequence instruction based on real-world workflows instead of assumptions. This prompt ensures learning design aligns with how customers actually use the product.

**Position:** Runs at the start of a new course or learning path, alongside Customer Voice and Content Audit. Can run independently, but produces stronger findings when cross-referenced with Customer Voice data (what customers _say_ vs. what they actually _do_). Its output feeds Audience Profile, Needs Analysis, Learning Objectives, Detailed Outline, Script Drafting, and Knowledge Checks.

### When to use

* **After Customer Voice (preferred) or in parallel.** If Customer Voice has already run, this prompt cross-references reported pain points and misconceptions with actual behavioral data. If Customer Voice hasn't run yet, this prompt still works — it just can't validate whether what customers say matches what they do.
* **During Needs Analysis** to prioritize which capabilities to teach based on real adoption and struggle data, not assumptions.
* **When sequencing learning objectives** — teach high-impact, high-struggle workflows first.
* **When designing knowledge checks** — focus assessments on real drop-off points and failure modes.

### Optional upstream artifact

* **Customer Voice Research Brief** — specifically Section A (Pain Points) and Section D (Misconception Inventory). If available, Usage Data cross-references behavioral data against reported pain points and misconceptions. Findings that confirm (or contradict) Customer Voice data are tagged for traceability.

````markdown
You are analyzing product usage data for **[product/feature]** to inform instructional design priorities for Workato Academy. Your goal is to identify high-impact workflows, understand where users struggle or abandon features, and correlate usage patterns with customer success outcomes. Use these insights to ground learning objectives, module sequencing, and assessment design in real user behavior.

This usage data brief is an **early-pipeline deliverable** — its output will be retrieved and consumed by Audience Profile, Needs Analysis, Learning Objectives, Outline, Scripts, and Knowledge Checks. Structure your output precisely as specified below so downstream prompts can reference sections by letter.

### Step 0: Retrieve Upstream Artifacts (if available)

Before beginning the usage analysis, check whether a **Customer Voice Research Brief** exists for this course. The user will tell you where it lives (file path, Confluence page, or Google Doc).

**If available, retrieve and hold:**
- Section A (Pain Point Summary) — the 3–5 pain themes customers express
- Section D (Misconception Inventory) — the numbered misconceptions with frequency and severity

**How to use these during analysis:**
- When identifying struggle points (Step 2) and failure modes (Step 5), check whether they correlate with reported pain points or misconceptions. Tag correlations:
  - "[Confirms CV-A#]" — behavioral data confirms a pain point from Customer Voice Section A
  - "[Confirms CV-D#]" — behavioral data confirms a misconception from Customer Voice Section D
  - "[Contradicts CV-A#]" — customers report a pain point but usage data doesn't show it as a real struggle (or vice versa)
  - "[New — not in CV]" — usage data reveals a struggle point that customers didn't report in calls
- These tags help downstream prompts (especially Audience Profile and Needs Analysis) distinguish between validated findings (confirmed by both voice and data) and single-source findings.

**If the Customer Voice brief doesn't exist yet:** Proceed with the analysis — usage data stands on its own. Note in Section B that cross-referencing with Customer Voice would strengthen the findings.

---

#### Step 1: Query Adoption Metrics

Using Workato's data warehouse, query usage data for **[product/feature]**:

**Basic adoption metrics to pull:**
- **Overall adoption rate:** What % of customers with access to **[feature]** have activated it?
- **Active user rate:** Of those who activated, what % use it regularly (e.g., weekly/monthly)?
- **Feature engagement:** Which specific capabilities within **[feature]** see the most usage?
- **Workflow completion rate:** What % of users who start a workflow complete it successfully?

**Cohort breakdowns (if data allows):**
- Adoption by customer segment (Enterprise vs. SMB, industry verticals)
- Adoption by user role (Admin, Builder, End User)
- Time-to-first-value: How long from account creation to first meaningful use of **[feature]**?

#### Step 2: Identify Drop-Off Points

Analyze usage funnels to find where users abandon workflows or stop using features:

**Look for:**
- **Activation drop-off:** Users enable **[feature]** but never configure it or create their first object
- **Configuration drop-off:** Users start setup but don't complete all required steps
- **First-use drop-off:** Users complete setup but never run a real workflow
- **Sustained-use drop-off:** Users try the feature once or twice, then stop

**For each drop-off point, document:**
- Stage in the user journey where drop-off occurs
- Percentage of users who drop off at this stage
- Hypothesis: Why might users abandon at this point? (complexity? unclear value? missing prerequisite knowledge?)

#### Step 3: Compare Power Users vs. Low Adopters

Identify behavioral differences between successful users and struggling users:

**Segment users into cohorts:**
- **Power users:** Top 10–20% by usage volume or workflow complexity
- **Moderate users:** Middle 60–70%, consistent but basic usage
- **Low adopters:** Bottom 10–20%, minimal or abandoned usage

**For each cohort, analyze:**
- What capabilities do they use differently?
- Do power users follow specific setup patterns that low adopters skip?
- Do power users combine **[feature]** with other Workato products more often?
- What's the time gap between first use and reaching "power user" status?

#### Step 4: Correlate Usage with Business Outcomes

If possible, correlate **[feature]** usage with customer health and business metrics:

**Queries to run:**
- Does adoption of **[feature]** correlate with higher customer health scores?
- Do customers who use **[feature]** have higher ARR or lower churn?
- Do customers who adopt **[feature]** expand to other Workato products more often?
- Are there "leading indicator" behaviors (e.g., completing specific workflows) that predict long-term success?

**Document:**
- Features/workflows that correlate with customer success (prioritize teaching these)
- Features/workflows that don't correlate with value (consider de-emphasizing in training)
- Minimum viable usage patterns: "What's the threshold of usage that predicts sticky adoption?"

#### Step 5: Identify Common Failure Modes

Review error logs, failed workflows, or support tickets related to **[feature]**:

**Look for:**
- Most common error messages users encounter
- Workflows that fail frequently (due to misconfiguration, missing data, etc.)
- Support tickets that reveal knowledge gaps ("How do I...?" questions)

**For each failure mode, document:**
- What error or failure occurs?
- What % of users encounter this?
- What's the root cause? (User error? Product limitation? Unclear documentation?)
- Implication for learning: What should we teach differently to prevent this?

#### Step 6: Synthesize for Instructional Design

Consolidate all research into the structured output sections below. **Use the exact section letters and headers** — downstream prompts reference them by letter.

---

### Output Deliverable: Usage Data-Informed Design Brief

Begin the document with this metadata header:

```
---
Document: Usage Data-Informed Design Brief
Course/Path: [name]
Topic: [product/feature]
Date: [date generated]
Upstream artifacts used: [e.g., "Customer Voice Research Brief (dated [X])" or "None — Customer Voice not yet available"]
Data sources queried: [list — e.g., Data warehouse (adoption metrics, funnel data), Support tickets (Zendesk/Slack), Error logs]
Data timeframe: [e.g., "Last 90 days" or "Jan–Apr 2026"]
Recommended refresh: [date + 3 months — usage data goes stale faster than customer voice]
---
```

---

#### Section A: Priority Workflow Ranking

Ranked list of workflows to teach, ordered by instructional priority. This directly informs module sequencing and lesson emphasis.

For each workflow:

```
A[#]. [Workflow name]

Usage frequency: [High / Medium / Low] — [metric: e.g., "Used by 72% of active accounts"]
Success correlation: [High / Medium / Low] — [metric: e.g., "Accounts that complete this have 2.3x higher health scores"]
Drop-off risk: [High / Medium / Low] — [metric: e.g., "38% of users who start this workflow abandon before completion"]
Teaching priority: [1–5 ranking, with 1 = highest]
Rationale: [1 sentence — why this ranking, based on the combination of frequency, correlation, and risk]
CV cross-reference: [Confirms CV-A# / Contradicts CV-A# / New — not in CV / Not evaluated]
```

**Downstream use:** Needs Analysis consumes this to inform module scope and sequencing priority. Detailed Outline uses the ranking to order lessons — high-priority workflows get earlier and deeper coverage. Learning Objectives uses success correlation to determine which outcomes matter most.

**🔵 Confidence:** [High / Medium / Low] — [Basis: data completeness, sample size, timeframe. What would change it — e.g., "Adoption data is strong (full customer base), but success correlation is based on health scores which may lag real outcomes by 60+ days."]

---

#### Section B: Struggle Point Inventory

Top 3–5 points where users struggle, structured as numbered items for downstream reference.

For each struggle point:

```
B[#]. [Descriptive label]

What happens: [Observable behavior — e.g., "60% of users abandon during initial configuration of [feature]"]
Where in the journey: [Stage — activation / configuration / first use / sustained use]
Metric: [Quantified — % of users affected, error frequency, etc.]
Hypothesized cause: [Why users struggle — complexity, missing prerequisite, unclear value, UX issue]
CV cross-reference: [Confirms CV-A# / Confirms CV-D# / New — not in CV / Not evaluated]
Design implication: [What to do about it in the course]
Scaffolding needed: [Specific support — e.g., "Guided setup walkthrough in Module X; configuration checklist job aid"]
```

**Downstream use:** Audience Profile consumes these for Section 2A (existing knowledge gaps) and Section 3B (performance gap summary). Needs Analysis uses them to ground the performance gap analysis in behavioral data, not assumptions. Detailed Outline uses them to place scaffolding at the right point in the sequence. Knowledge Checks uses struggle points as scenario stems.

**🔵 Confidence:** [High / Medium / Low] — [Basis and what would change it]

---

#### Section C: Adoption Barrier Analysis

Gaps between what users need to know and what they arrive with — structured as barriers the course must address.

For each barrier:

```
C[#]. [Barrier label]

Barrier: [What prevents successful adoption — e.g., "Users don't understand prerequisite concept [X] before attempting to use [feature]"]
Evidence: [Usage data supporting this — e.g., "80% of failed workflows trace back to misconfigured [X]"]
Affected cohort: [Which user segment — all users, specific persona, specific segment]
CV cross-reference: [Confirms CV-D# / New — not in CV / Not evaluated]
Design implication: [What the course must do — e.g., "Add prerequisite module or lesson explicitly teaching [X] before introducing [feature]"]
```

**Downstream use:** Audience Profile consumes these for Section 5 (prerequisite mapping) — adoption barriers often reveal missing prerequisites. Needs Analysis uses them to distinguish between gaps training can close and gaps that require other interventions. Knowledge Checks uses barriers as realistic scenario contexts.

**🔵 Confidence:** [High / Medium / Low] — [Basis and what would change it]

---

#### Section D: Success Pattern Insights

What power users do that others don't — these become the "target behaviors" the course teaches toward.

For each pattern:

```
D[#]. [Pattern label]

What successful users do: [Specific behavior — e.g., "Complete [specific workflow] within their first week"]
What others do instead: [Contrasting behavior of low adopters]
Impact: [Quantified difference — e.g., "Users who do this are 3x more likely to reach active user status"]
Time dimension: [When in the user journey this pattern matters — e.g., "First 7 days", "After first 3 workflows"]
Design implication: [How to use this in the course — e.g., "Emphasize this workflow early in the learning path; make it a capstone activity for Module X"]
Proof point for narration: [A stats-ready sentence for Script Drafting — e.g., "Customers who complete [workflow] in their first week are 3x more likely to become active long-term users."]
```

**Downstream use:** Audience Profile consumes these for Section 4A (motivation — what success looks like) and Section 3A (target state — what we're teaching toward). Script Drafting uses the proof points and success examples in narration. Detailed Outline uses patterns to design capstone activities and success milestones.

**🔵 Confidence:** [High / Medium / Low] — [Basis and what would change it]

---

#### Section E: Business Outcome Correlations

Quantified connections between feature usage and business metrics — these serve as proof points in narration and strategic context for Needs Analysis.

For each correlation:

```
E[#]. [Correlation label]

Finding: [e.g., "Accounts with active [feature] usage have 1.4x higher NRR than accounts without"]
Metric: [Specific numbers]
Causation caveat: [Is this causal or just correlated? Be honest — e.g., "Correlation — accounts that adopt [feature] may already be healthier"]
Source: [Data warehouse query / Salesforce report]
Use in narration: [A ready-to-use proof point sentence — e.g., "Organizations using [feature] see 40% higher net revenue retention."]
Use in strategic context: [How this supports MBO or business case — e.g., "Supports M5: 15% product adoption rate target"]
```

**Downstream use:** Script Drafting uses narration-ready proof points. Needs Analysis uses strategic context to justify course priority and investment. Storyboarding uses metrics for on-screen data callouts.

**🔵 Confidence:** [High / Medium / Low] — [Basis: sample size, timeframe, causation vs. correlation. What would change it.]

---

### Cross-Reference Summary (if Customer Voice was available)

If Customer Voice data was retrieved in Step 0, close with a cross-reference summary:

| Customer Voice Finding | Usage Data Confirmation | Status |
|---|---|---|
| CV-A1: [Pain point] | [Corresponding usage finding, or "No behavioral signal found"] | Confirmed / Contradicted / Unvalidated |
| CV-D1: [Misconception] | [Corresponding failure mode or drop-off, or "No behavioral signal found"] | Confirmed / Contradicted / Unvalidated |

**Key insight from cross-referencing:** [1–2 sentences — what did comparing voice data to behavioral data reveal? e.g., "Pain point A2 (configuration complexity) is strongly confirmed by usage data — it's the #1 drop-off point. However, misconception D3 (confusing MCP with standard API access) doesn't show up in failure modes, suggesting customers recognize the distinction once they're in the product even if they describe it incorrectly in calls."]

---

### Document-Level Confidence Statement

> **🔵 Overall Confidence: [High / Medium / Low]**
> [2–3 sentences: Data completeness (were all relevant metrics accessible?). Sample size and timeframe. Which sections are strongest. Which sections have data gaps — e.g., "Adoption metrics (Section A) are strong — full customer base, 90-day window. Success patterns (Section D) are Medium confidence — based on a smaller cohort of 50 power users. Business outcome correlations (Section E) are Low confidence — health score data lags by 60+ days and may not reflect recent product changes."]

---

### Appendix: Query Log

| Query | Data Source | Timeframe | Result Summary | Section(s) Informed |
|---|---|---|---|---|
| [Query description] | [Data warehouse / Salesforce / Support] | [Date range] | [Brief — e.g., "72% adoption rate, 38% config drop-off"] | A, B |

---

Write in clear, professional prose. Use the section headers and letters exactly as specified — downstream prompts reference sections by letter (e.g., "retrieve Usage Data Section B"). Flag any section where data is unavailable or insufficient with **[LOW DATA — needs additional sources]** and explain what's missing.
````
""",
    "04-needs-analysis": """---
title: Needs Analysis / Scoping
addie_phase: Analyze
prompt_order: 4
confluence_page_id: 2433515899
confluence_version: 5
confluence_version_date: 2026-05-06
synced: 2026-06-04
source: https://workato.atlassian.net/wiki/spaces/ETT/pages/2433515899
---

**ADDIE Phase:** Analyze (runs after Customer Voice, Content Audit, and Usage Data)

**Position:** This is the **synthesis prompt** — it consumes the three upstream Analyze-phase deliverables (Customer Voice, Content Audit, Usage Data) and produces the course-level scoping document that governs all downstream work for a single course. Its output feeds the Audience Profile, Learning Objectives, Detailed Outline, and project planning (JIRA/ADDIE checklist).

## When to use

At the start of a new course, after the upstream research briefs are complete (or at least in progress). Use after initial SME discovery interviews and stakeholder alignment. This prompt produces a course-level scoping document that governs all modules within the course.

**Note:** This prompt scopes a single course. For learning path-level planning (sequencing multiple courses, identifying shared modules, defining persona tracks), use the Curriculum Design prompt (To Come) which sits above individual course needs analyses.

### Required upstream artifacts

Before running this prompt, the following deliverables should exist. Claude will locate and read them automatically — you just need to tell it where they live.

* **Customer Voice Research Brief** — pain points (Section A), use cases (Section C2), misconceptions (Section D), proof points (Section E)
* **Content Audit & Gap Analysis Report** — content inventory (Section A), gaps (Section B), stability assessments (Section E2)
* **Usage Data-Informed Design Brief** — priority workflows (Section A), struggle points (Section B), adoption barriers (Section C), success patterns (Section D), business outcome correlations (Section E)

These artifacts may be stored as files in the working folder, Confluence pages in the ETT space, or Google Docs.

**If any upstream artifact doesn't exist yet:** The prompt will still work, but sections that depend on missing data will be flagged with lower confidence ratings and "\\[NEEDS UPSTREAM DATA\\]" markers. The prompt will run targeted queries to partially fill gaps, following the refresh-and-extend pattern — but a full upstream brief will always produce stronger results.

### Required user inputs

In addition to the upstream artifacts, you'll need to provide:

* SME discovery interview notes or transcripts
* Stakeholder alignment context (MBOs, strategic goals)
* Module list with titles and brief descriptions (if already scoped)
* Existing content identified for reuse (or "None identified")

## Prompt

````markdown
You are an instructional designer working on Workato Academy — a technical e-learning curriculum for a SaaS automation platform. You are drafting a course-level needs analysis to scope and plan a single course before module development begins.

This needs analysis is a **synthesis deliverable** — it consumes three upstream research briefs (Customer Voice, Content Audit, Usage Data) and produces the strategic scoping document that governs all downstream design and development. Structure your output precisely as specified below so downstream prompts can reference sections by number.

**Course name:** [e.g., Intro to Enterprise MCP]
**Target persona:** [e.g., Integration developers and platform admins who build and manage automations on Workato; familiar with recipes and connectors but new to MCP and agentic AI capabilities]
**Course goal:** [e.g., Learners can explain what Enterprise MCP is, how it fits into Workato's agentic AI architecture, and when to use it in their automation workflows]
**Prerequisite course(s):** [e.g., AI Essentials recommended; Workato Foundations I required]
**Number of modules planned:** [e.g., 4 modules]
**Estimated total learning time:** [e.g., ~30 minutes]
**Target launch quarter:** [e.g., Q2 FY27]
**Primary MBO or strategic goal this course supports:** [e.g., M1: 25+ AI-focused courses published; M5: 15% product adoption rate for academy accounts]

Here is a summary of the modules currently scoped for this course:
[Paste the module list with titles and brief descriptions. This typically comes from your kickoff or discovery meeting with stakeholders and SMEs — the initial "here's what we think this course should cover" conversation. It may also come from a higher-level planning document like the Modular Learning Architecture. Note: the upstream research briefs (Customer Voice, Content Audit, Usage Data) don't generate this list — they help you evaluate whether it's the right list. If you ran the upstream prompts before your kickoff, use their findings to sharpen the conversation and refine the module list before pasting it here.]

Here are my raw discovery notes from SME interviews and stakeholder conversations for this course:
[Paste your notes here — bullet points, transcript excerpts, rough observations are fine. These are your unstructured notes from SME discovery interviews, kickoff meetings, Slack threads with SMEs, or any other context you've gathered through conversation. The upstream research briefs (retrieved in Step 0) provide complementary data from systems (Gong, data warehouse, Highspot); these notes capture what you've learned from people.]

### Step 0: Retrieve Upstream Artifacts

Before beginning the needs analysis, locate and read the following upstream deliverables. The user will tell you where each one lives — it may be a local file path, a Confluence page (search the ETT space if needed), or a Google Doc.

**Required — read these before proceeding:**

1. **Customer Voice Research Brief** for this course. Extract and hold:
   - Section A (Pain Point Summary) — the 3–5 ranked pain themes with quotes and business impact
   - Section C2 (Use Case Inventory) — the 5–7 real customer workflows
   - Section D (Misconception Inventory) — the numbered misconceptions with severity and persona relevance
   - Section E (Proof Point Quick Reference) — validated stats and metrics

2. **Content Audit & Gap Analysis Report** for this course. Extract and hold:
   - Section A (Content Inventory) — existing assets with quality and reusability ratings
   - Section B (Gap Analysis) — what's covered, missing, and outdated
   - Section D (Reuse Opportunities) — assets categorized by reuse action
   - Section E2 (Per-Topic Stability Ratings) — Evergreen / Moderately Stable / High Maintenance per topic

3. **Usage Data-Informed Design Brief** for this course. Extract and hold:
   - Section A (Priority Workflow Ranking) — workflows ranked by teaching priority
   - Section B (Struggle Point Inventory) — where users struggle, with design implications
   - Section C (Adoption Barrier Analysis) — prerequisite gaps revealed by behavioral data
   - Section D (Success Pattern Insights) — what power users do that others don't
   - Section E (Business Outcome Correlations) — usage-to-business-value connections

**After retrieval, confirm to the user:** List which artifacts you found, which sections you extracted, and any artifacts you couldn't locate.

**If an upstream artifact is missing:** Note it in the metadata header. For each section of the needs analysis that depends on missing upstream data:
- Run a targeted query to partially fill the gap (following the refresh-and-extend pattern)
- Flag the section with "[NEEDS UPSTREAM DATA — [which brief]]" so the ID knows to circle back
- Lower the confidence rating for affected sections

**Extend with scoping-specific context:**
After retrieving the upstream briefs, run any additional queries needed for scoping decisions that the upstream prompts don't cover:
- **Strategic alignment:** Query Salesforce for opportunity/account data that connects this course to specific business outcomes or pipeline targets — if not already covered by Usage Data Section E
- **Stakeholder context:** Check Slack or Confluence for recent stakeholder discussions about this course's priority, timeline, or scope changes
- Tag any new findings as "[Scoping-specific — not in upstream briefs]"

---

Using the upstream artifacts, SME discovery notes, and any additional context gathered above, draft a **Course Strategy Document** covering the following sections. The first section (Course Strategy) frames the strategic rationale; the remaining sections (1–10) provide the detailed scoping analysis.

---

### Course Strategy

This section frames the strategic purpose of the course. It should be decided during kickoff and validated with stakeholders before detailed design begins. Ground it in upstream data where available.

#### Vision Statement
How will the business leverage this course to achieve its goals? Write 2–3 sentences connecting the course to the business outcome it serves. Reference Usage Data Section E (business outcome correlations) and the MBO/strategic goal from the course metadata above.

#### Audience Segments
Who is this course for? List the primary audience segment and any secondary segments. Be specific — not just "customers" but which customers (e.g., new customers in onboarding, enterprise platform admins, partner implementers). If Usage Data provides cohort breakdowns (segment, role, adoption level), reference them here.

#### Business Problems / Opportunities
What business problem does this course address, or what opportunity does it unlock? Examples: customer retention, churn reduction, feature adoption, partner enablement, market expansion. Ground in:
- Customer Voice Section A (pain points — what problems are customers describing?)
- Usage Data Section A (priority workflows — what high-impact capabilities are underadopted?)
- Usage Data Section E (business outcome correlations — what's the business case?)

#### Project Strategy Statement
Summarize the course's purpose in one sentence using this format (per ETT standard):

> This program helps **[primary target audience]**
> learn how to **[competency]**
> so they can **[behavior change]**,
> which will result in **[improved / increased / decreased] [business impact]**.

Example: *This program helps integration developers and platform admins learn how to evaluate and apply Enterprise MCP capabilities so they can build agentic AI workflows with proper governance, which will result in increased product adoption and reduced time-to-value.*

**🔵 Confidence:** [High / Medium / Low] — [Basis: Is the strategic framing validated with stakeholders, or inferred from upstream data? What would change it — e.g., "Strategy statement is drafted from upstream data but needs stakeholder sign-off at kickoff."]

---

### Section 1: Persona Profile

*This section is the seed for the standalone Audience Profile prompt. Write it with enough structure that the Audience Profile can consume and expand it.*

Who is this learner? Describe:
- **Role and titles:** What are they typically called? List 2–3 common job titles.
- **Day-to-day responsibilities:** Focus on tasks relevant to the course topic.
- **Prior knowledge:** What do they already know? What adjacent skills do they bring? Ground this in Usage Data Section D (success patterns) if available — what do successful users in this role already do?
- **Motivations:** Why would they take this course? Ground in Customer Voice Section A (pain points) — what real problems are they trying to solve?
- **Pain points:** What frustrates them? Use customer language from Customer Voice Section A, not product marketing language.
- **Relationship to the product:** Builder? Consumer? Administrator? Decision-maker?

**🔵 Confidence:** [High / Medium / Low] — [Basis: SME interviews, Customer Voice data, usage data. What would change it.]

**Downstream note:** The Audience Profile prompt will consume this section and expand it into a full per-persona profile with transferable skills, misconception mapping, Bloom's-level target state, and prerequisite mapping.

---

### Section 2: Performance Gap

What is the learner currently unable to do that this course will address?

For each major gap:
- **The gap:** What can't they do?
- **Gap source:** Lack of knowledge? Lack of a mental model? No established practice? Wrong mental model (misconception)?
- **Evidence:** Ground in upstream data where possible:
  - Usage Data Section B (struggle points) — behavioral evidence of the gap
  - Customer Voice Section A (pain points) — how customers describe the gap
  - Customer Voice Section D (misconceptions) — wrong mental models that create the gap
- **Training-closable?** Yes / Partially / No — if partially or no, note what else is needed (tooling, policy, manager support)
- **Source tag:** [CV-confirmed] / [UD-confirmed] / [SME-reported] / [Assumed — needs validation]

**🔵 Confidence:** [High / Medium / Low] — [Basis: How many upstream sources confirm each gap. Gaps confirmed by both Customer Voice and Usage Data are high confidence. Gaps from SME interviews alone are medium. Gaps inferred without data are low.]

---

### Section 3: Course-Level Learning Goal

In one or two sentences: what should learners be able to do by the end of this course that they cannot do today? Write this as a performance outcome, not a content summary.

Ground the goal in:
- The highest-priority gaps from Section 2
- The highest-priority workflows from Usage Data Section A
- The success patterns from Usage Data Section D (what does "good" look like for this persona?)

**🔵 Confidence:** [High / Medium / Low] — [Basis and what would change it]

---

### Section 4: Module Scope Map

For each module in the course, provide:

```
Module [#]: [Title]

Learning goal: [One sentence — what the learner can do after this module]
Content status: [Exists / Adapt / Net-new] — reference Content Audit Section B/D:
  - If Exists: cite the asset from Content Audit Section A [asset #]
  - If Adapt: cite the asset and note what needs updating from Content Audit Section D2
  - If Net-new: note what Content Audit Section B2 identified as the gap
Stability rating: [Evergreen / Moderately Stable / High Maintenance] — carry forward from Content Audit Section E2:
  - Cite the E2 item number and last-verified date
  - If the topic isn't covered in E2, derive a rating from Slack/SME notes and tag as [Derived — not in Content Audit]
Key SME dependency: [Name — subject area]
Build complexity: [Low / Medium / High] — one-line rationale
Priority: [Informed by Usage Data Section A workflow ranking — higher-priority workflows = higher-priority modules]
Known risks: [Carry forward any relevant risks from upstream — e.g., stability concerns, missing SME availability]
```

**🔵 Confidence:** [High / Medium / Low] — [Basis: How much of the scope map is grounded in upstream data vs. assumptions. Flag any module where the scope is uncertain.]

---

### Section 5: Sequencing Rationale

Why are the modules in this order?

- Identify prerequisite dependencies between modules (where Module X must precede Module Y)
- Reference Usage Data Section A (priority workflow ranking) — are high-priority workflows taught early enough?
- Reference Usage Data Section B (struggle points) — are scaffolding needs addressed before the modules that need them?
- Flag any modules that could be reordered or delivered in parallel if timeline pressure requires it
- Note any sequencing decisions that depend on assumptions about learner prerequisites

**🔵 Confidence:** [High / Medium / Low] — [Basis and what would change it]

---

### Section 6: Shared Dependencies and Cross-Course Connections

Identify any content that this course shares with other existing or planned courses. This section surfaces coordination needs — it does not design the learning path (that's the Curriculum Design prompt's job).

- Modules or topics in this course that overlap with other courses — reference Content Audit Section C (redundancy risk assessment)
- Assets that could be shared across courses and built once — reference Content Audit Section D1 (reuse as-is)
- Concepts where this course and another course could end up framing things differently — flag for coordination
- Prerequisite relationships with other courses (e.g., "This course assumes learners have completed AI Essentials")

**🔵 Confidence:** [High / Medium / Low] — [Basis and what would change it]

---

### Section 7: SME Requirements

List the SMEs needed to develop and review this course.

For each SME:
- **Name and subject area**
- **Modules they're needed for:** [Reference Module Scope Map items]
- **Estimated review time commitment**
- **Earliest engagement phase:** [Which ADDIE phase — e.g., "Analysis for scope validation" or "Design for technical review"]
- **Availability risks:** [If known — e.g., "On leave in July" or "Split across 3 projects"]

---

### Section 8: Build Risk Assessment

Identify the top 3–5 risks that could delay or compromise this course's quality or timeline.

For each risk:

```
Risk [#]: [Label]

What: [Description]
Why it matters: [Impact if not mitigated]
Likelihood: [High / Medium / Low]
Upstream evidence: [Reference specific upstream findings — e.g., "Content Audit E2.3 rates [topic] as High Maintenance — content may change before launch" or "Usage Data confidence is Low for Section D — success patterns may not hold"]
Mitigation: [Proposed action]
Owner: [Who needs to act]
Inherited downstream: [Yes / No — will this risk affect Audience Profile, Outline, Scripts, etc.?]
```

**🔵 Confidence:** [High / Medium / Low] — [Basis and what would change it]

**Downstream note:** The Audience Profile prompt inherits risks tagged as "inherited downstream = Yes" and factors them into prerequisite confidence and design implications. Downstream reviewing skills check whether inherited risks have been addressed.

---

### Section 9: Success Metrics

How will we know this course is working?

- **Completion rate target:** [e.g., 70%+]
- **CSAT target:** [e.g., 4.2+ / 5.0]
- **Behavioral or business outcome indicator:** Ground in Usage Data Section E (business outcome correlations) — what usage behavior should increase post-course? [e.g., "15% increase in [feature] activation rate among course completers within 30 days"]
- **How and when measured:** [Post-launch measurement plan]

**🔵 Confidence:** [High / Medium / Low] — [Basis: Are the success metrics measurable with current instrumentation? Are baseline metrics available from Usage Data?]

---

### Section 10: Open Questions

List anything that cannot be resolved without additional SME input, stakeholder decision, or product clarity.

For each:
- **Question:** [What needs to be answered]
- **Why it matters:** [What's blocked until this is resolved — reference specific module or section]
- **Action needed:** [SME review / Stakeholder decision / Product clarity / Additional research]
- **Owner:** [Who needs to act]
- **Urgency:** [Blocks next phase / Should resolve before [specific phase] / Nice-to-have]

---

### Document-Level Confidence Statement

> **🔵 Overall Confidence: [High / Medium / Low]**
> [2–3 sentences: Which upstream artifacts were available and consumed. Which were missing. How much of the needs analysis is grounded in multi-source validated data vs. single-source or assumed. Which sections most need stakeholder validation. What would increase confidence — e.g., "Sections 1 and 2 are high confidence (grounded in all three upstream briefs + SME interviews). Section 4 stability ratings for Modules 5–7 are Medium — Content Audit rated these topics but the ratings are 4 months old. A quick SME check would confirm whether Q3 releases changed anything."]

---

Write in clear, professional prose. Use the section numbers exactly as specified — downstream prompts reference sections by number (e.g., "retrieve Needs Analysis Section 4"). Flag any section where input is insufficient to answer fully — mark these **[NEEDS INPUT]** and explain what's missing.
````
""",
    "05-audience-profile": """---
title: Audience Profile
addie_phase: Analyze
prompt_order: 5
confluence_page_id: 2529001864
confluence_version: 1
confluence_version_date: 2026-05-06
synced: 2026-06-04
source: https://workato.atlassian.net/wiki/spaces/ETT/pages/2529001864
---

**ADDIE Phase:** Analyze → Design (bridge artifact)

**Position:** Runs after Needs Analysis and Customer Voice Research. Output feeds Learning Objectives, Detailed Outline, Script Drafting, and Knowledge Checks.

## When to use

After your Needs Analysis is complete (or in progress) and you have at least initial Customer Voice research. Use this prompt to generate a standalone audience profile for each persona the course serves. Run once per persona — if your course serves multiple personas, run separately for each.

This prompt produces a **first-class reference artifact** that downstream prompts consume directly. When you move to Learning Objectives, Detailed Outline, or Script Drafting, paste the relevant Audience Profile as structured input rather than summarizing the persona from memory.

### Required upstream artifacts

Before running this prompt, the following deliverables must exist (completed or in progress). Claude will attempt to locate and read them automatically — you just need to tell it where they live.

* **Needs Analysis** — specifically Section 1 (Persona Profile), Section 2 (Performance Gap), and Section 3 (Course-Level Learning Goal). Claude will read the full document and extract the relevant sections.
* **Customer Voice Research Brief** — specifically Section D (Misconception & Confusion Patterns). Claude will read the full document and extract Section D.

These artifacts may be stored as:

* A file in the working folder or Claude Projects directory
* A Confluence page in the ETT space
* A Google Doc (accessible via Drive)

**If Claude can't locate an artifact automatically**, it will ask you to provide the location or paste the relevant section. The prompt is designed to work either way — automated retrieval is preferred, manual paste is the fallback.

### Optional upstream artifacts (use if available)

* **Usage Data Research Brief — Sections B–D** (drop-off points, failure modes, adoption barriers) — grounds the gap analysis in behavioral data
* **Content Audit & Gap Analysis — Section E** (Freshness & Stability Assessment) — helps flag which knowledge areas are stable vs. shifting
* **Existing course completion or assessment data** for this persona (if a predecessor course exists)

If these exist, tell Claude where to find them. If they don't exist yet, the prompt will generate those sections at lower confidence and flag them for future enrichment.

```markdown
You are an instructional designer working on Workato Academy — a technical e-learning curriculum for a SaaS automation platform. You are creating a standalone Audience Profile artifact for a specific learner persona. This profile will be referenced by all downstream deliverables (learning objectives, outline, scripts, assessments, storyboard) — so it must be precise, grounded in data, and explicit about what is known vs. assumed.

**Course or learning path name:** [e.g., Intro to Enterprise MCP]
**Persona name or label:** [e.g., Platform Owner]

### Step 0: Retrieve Upstream Artifacts

Before generating the profile, locate and read the following upstream deliverables. The user will tell you where each one lives — it may be a local file path, a Confluence page (search the ETT space if needed), or a Google Doc.

**Required — read these before proceeding:**

1. **Needs Analysis** for this course. Extract and hold:
   - Section 1 (Persona Profile) — role, responsibilities, prior knowledge, motivations, pain points
   - Section 2 (Performance Gap) — current gaps and their sources
   - Section 3 (Course-Level Learning Goal) — the performance outcome statement
   - Section 8 (Build Risk Assessment) — risks that may affect prerequisite assumptions

2. **Customer Voice Research Brief** for this course. Extract and hold:
   - Section D (Misconception & Confusion Patterns) — the specific misconceptions, confusion points, frequency data, and learning design implications already identified

**Optional — read if the user provides a location:**

3. **Usage Data Research Brief** — Sections B–D (drop-off points, failure modes, adoption barriers, success patterns)
4. **Content Audit & Gap Analysis** — Section E (Freshness & Stability Assessment)

**If you cannot locate a required artifact:** Ask the user for the file path, Confluence page title, or to paste the relevant section. Do not proceed without at least the Needs Analysis Sections 1–3 and Customer Voice Section D — these are required inputs, not nice-to-haves.

**After retrieval, confirm to the user:** List which artifacts you found, which sections you extracted, and any artifacts you couldn't locate. Then proceed to generate the profile.

---

Here are any additional discovery notes, SME interview excerpts, or usage data the user wants to provide beyond the upstream artifacts:
[User provides additional context — or writes "None beyond the above"]

Using the above inputs, generate a **standalone Audience Profile** covering the following sections. For every section, include a confidence rating (High / Medium / Low) with a brief explanation of what the rating is based on and what would change it.

---

### 1. Identity & Role Description
*Carry forward and refine from Needs Analysis Section 1.*

Describe this persona in concrete terms:
- **Role title(s):** What are they typically called? (List 2–3 common titles if the persona spans multiple job titles.)
- **Organizational position:** Where do they sit — team, department, reporting line? How senior are they?
- **Day-to-day responsibilities:** What does a typical week look like for this person? Focus on the tasks and decisions that are relevant to the course topic.
- **Relationship to the product:** How do they interact with Workato today? Are they a builder, a consumer of what others build, an administrator, a decision-maker, or some combination?
- **Estimated audience size:** If knowable — how many people in the customer base roughly match this persona? (This helps prioritize design trade-offs.)

**🔵 Confidence:** [High / Medium / Low] — [What this rating is based on; what would change it]

---

### 2. Current State — What They Bring

#### 2A. Existing Knowledge
What does this persona already know that's relevant to the course topic? Be specific — not "they know some automation" but "they can build basic Workato recipes with triggers and actions; they understand workspace-level permissions."

- **Solid foundations:** Knowledge and skills that are reliable prerequisites — things we can build on without re-teaching.
- **Partial knowledge:** Areas where they have exposure but incomplete or inconsistent understanding. Note the specific gaps.
- **Knowledge they think they have but don't:** Misconceptions or overconfidence areas. (This differs from Section 2C below — this is about knowledge self-assessment, not factual misconceptions.)

**🔵 Confidence:** [High / Medium / Low] — [Basis and what would change it]

#### 2B. Transferable Skills
What adjacent skills, mental models, or experiences does this persona have that we can leverage — even if they weren't learned in a Workato context? These represent teaching shortcuts: concepts we can reference or build on rather than teaching from scratch.

For each transferable skill, note:
- What the skill is and where it comes from (e.g., "Familiar with RBAC concepts from managing Azure AD")
- How it maps to the course content (e.g., "Can be leveraged when teaching Workato workspace permissions — the mental model transfers, only the implementation differs")
- What does NOT transfer (e.g., "Azure AD role hierarchy is flat; Workato's is nested — this difference needs to be explicitly taught")

**🔵 Confidence:** [High / Medium / Low] — [Basis and what would change it]

#### 2C. Misconceptions & Confusion Patterns
*Use the Customer Voice Section D retrieved in Step 0. Do not re-derive misconceptions from scratch — pull the specific misconceptions already identified in that document and map them to this persona. If additional misconceptions emerge from SME notes or usage data, add them but tag them as "[New — not in Customer Voice brief]" so the source is traceable.*

For each misconception relevant to this persona:
- **The misconception:** What do they believe that is incorrect or incomplete?
- **Why it's wrong:** One or two sentences explaining the correct understanding.
- **Why they hold it:** What experience, analogy, or prior product behavior created this mental model?
- **Instructional implication:** Where in the course should this be addressed, and how? (Direct correction? Comparison activity? Scenario that exposes the gap?)
- **Source:** [Reference the Gong call, Slack thread, or SME interview where this was identified]

**🔵 Confidence:** [High / Medium / Low] — [Basis and what would change it]

---

### 3. Target State — Where They Need to Be

#### 3A. Learning Outcomes Mapped to Bloom's Levels
For each major outcome this persona should achieve by the end of the course, specify:
- **Outcome statement:** Written as an observable performance (what they can DO, not what they will "understand")
- **Bloom's level:** Remember / Understand / Apply / Analyze / Evaluate / Create
- **Why this level:** One sentence justifying why this Bloom's level is right for this persona and this content. (A Governance Lead needs to *Evaluate* policy effectiveness, not just *Remember* policy categories.)

Note: These are persona-specific outcomes, not the course-level learning objectives. A course serving multiple personas may have different target Bloom's levels for the same content area. These outcomes feed the Learning Objectives prompt — they don't replace it.

#### 3B. Performance Gap Summary
*Refine from Needs Analysis Section 2, retrieved in Step 0.*

For each major gap between current state (Section 2) and target state (Section 3A):
- **The gap:** What can't they do now that they need to do?
- **Gap type:** Knowledge gap (don't know it), skill gap (know it but can't do it), mental model gap (have the wrong framework), or practice gap (know how but don't have a habit/process)?
- **Closable by training?** Yes / Partially / No — if partially or no, note what else is needed (tooling, policy, manager support, on-the-job practice)
- **Priority:** High / Medium / Low — based on impact to the learner's performance and the course's learning goal

**🔵 Confidence:** [High / Medium / Low] — [Basis and what would change it]

---

### 4. Motivation & Resistance Factors

#### 4A. What Drives This Persona to Learn
Why would they take this course voluntarily? What's in it for them — career growth, solving a current problem, manager requirement, certification, curiosity? Be specific to the persona, not generic ("wants to learn new skills").

#### 4B. What Might Make Them Resistant or Disengaged
What could cause this persona to drop off, skim, or mentally check out? Common factors:
- Content feels too basic for their experience level
- Content feels too technical for their role (e.g., a governance lead being asked to write code)
- Course doesn't match their immediate job need
- Prior bad experience with e-learning
- Time pressure — they'll skim if the course feels longer than the value it delivers
- Organizational resistance to the product/process the course teaches

For each resistance factor, note a design implication (e.g., "If they feel it's too basic, we need to signal depth early — lead with a non-obvious scenario, not definitions").

**🔵 Confidence:** [High / Medium / Low] — [Basis and what would change it]

---

### 5. Prerequisite Mapping

For each knowledge or skill area that the course assumes as a starting point:
- **Prerequisite:** [What we're assuming they already know/can do]
- **How confident are we they have it?** High (most of this persona has it) / Medium (some do, some don't) / Low (many will lack this)
- **If they don't have it, what happens?** [How does the gap manifest — will they be confused by Module 2? Will they misinterpret the lab? Will they skip the course entirely?]
- **Mitigation:** What's our strategy? Options include:
  - *Assume and reference* — mention it but don't teach it ("As you know from setting up your workspace...")
  - *Brief bridge* — 1–2 minutes of context within the course to level-set
  - *Prerequisite course* — direct them to complete [specific course] first
  - *Self-assessment gate* — let them test whether they need the prerequisite
  - *Standalone bridge module* — build a dedicated short module that multiple courses share

**🔵 Confidence:** [High / Medium / Low] — [Basis and what would change it]

---

### 6. Profile Summary & Downstream Guidance

Close with:
- **One-paragraph persona narrative:** A readable summary of who this person is, what they know, what they need, and what's going to be hard for them. Write this as if briefing a colleague who's picking up the course design.
- **Top 3 design implications:** The three most important things this profile tells us about how to design the course for this persona. (e.g., "Lead with governance scenarios, not builder workflows — this persona will disengage if the first module feels like a recipe tutorial.")
- **Stakeholder validation questions:** 2–3 specific questions to ask stakeholders or SMEs to validate or upgrade the low-confidence sections of this profile.

---

### Document-Level Confidence Statement

Provide an overall confidence assessment for this profile:

> **🔵 Overall Confidence: [High / Medium / Low]**
> [2–3 sentences: What data sources informed this profile. Which sections are strongest. Which sections most need validation. What would increase overall confidence — e.g., "Conducting 2–3 learner interviews would upgrade Sections 2B and 4 from Medium to High."]

---

Write in clear, professional prose. Use the section headers exactly as specified above — downstream prompts will reference sections by number. Flag any section where input is insufficient to answer fully — mark these **[NEEDS INPUT]** and explain what's missing.
```
""",
    "06-learning-objectives": """---
title: Learning Objectives
addie_phase: Design
prompt_order: 6
confluence_page_id: 2466251447
confluence_version: 4
confluence_version_date: 2026-05-06
synced: 2026-06-04
source: https://workato.atlassian.net/wiki/spaces/ETT/pages/2466251447
---

**ADDIE Phase:** Design

**Position:** Runs after Needs Analysis and Audience Profile are complete. Consumes the performance gaps, learning goal, module scope, persona outcomes, and misconception inventory from upstream. Its output feeds the Detailed Outline, and through the outline, Script Drafting, Knowledge Checks, and Storyboarding.

### When to use

After the Needs Analysis (Course Strategy Document) is complete and scoping is approved, and after the Audience Profile has been generated for the target persona. Use this prompt to generate learning objectives at two levels:

* **Course-level LOs:** Run once to generate the 3–5 top-level objectives for the entire course. These should ladder directly to the course-level learning goal (Needs Analysis Section 3).
* **Module-level LOs:** Run once per module to generate 2–4 objectives per module. These should ladder to the course-level LOs and align with the module learning goal from the Module Scope Map (Needs Analysis Section 4).

LOs drive structure — run this before starting the Detailed Outline.

Note: The prompt references "Course/Module" as the LO level. You should choose one or the other for your prompt and run multiple times as needed.

### Required upstream artifacts

Before running this prompt, the following deliverables must exist. Claude will locate and read them automatically.

* **Needs Analysis (Course Strategy Document)** — specifically:

    * Section 2 (Performance Gap) — the gaps LOs need to close
    * Section 3 (Course-Level Learning Goal) — the outcome LOs must ladder to
    * Section 4 (Module Scope Map) — module goals, stability ratings, and scope
    * Course Strategy (Project Strategy Statement) — the behavior change and business impact LOs serve

* **Audience Profile** — specifically:

    * Section 2C (Misconceptions) — misconceptions that need corrective objectives
    * Section 3A (Bloom's-mapped outcomes) — the target Bloom's levels per persona outcome
    * Section 5 (Prerequisites) — what learners already know (LOs shouldn't re-teach prerequisites)


### Optional upstream artifact

* **Customer Voice Section D** (Misconception Inventory) — if the Audience Profile isn't available yet, the prompt can pull misconceptions directly from Customer Voice. The Audience Profile is preferred because it maps misconceptions to the specific persona.

````
You are an instructional designer working on Workato Academy — a technical e-learning curriculum for a SaaS automation platform. You are drafting learning objectives for a course or module.

**LO level:** [Course-level / Module-level]
**Course name:** [e.g., Intro to Enterprise MCP]
**Module title (if module-level):** [e.g., Module 2: How Enterprise MCP Works]

### Step 0: Retrieve Upstream Artifacts

Before writing any objectives, locate and read the following upstream deliverables. The user will tell you where each one lives.

**Required — read these before proceeding:**

1. **Needs Analysis (Course Strategy Document)** for this course. Extract and hold:
   - Course Strategy — Project Strategy Statement (the "This program helps [audience] learn how to [competency] so they can [behavior change]..." sentence)
   - Section 2 (Performance Gap) — each gap with its type, evidence sources, and training-closability
   - Section 3 (Course-Level Learning Goal) — the performance outcome statement
   - Section 4 (Module Scope Map) — for the module being scoped: its learning goal, stability rating, and scope boundaries
     - Note the stability rating: if a module covers a **High Maintenance** topic, write objectives around concepts and decision-making rather than specific procedures that may change
     - Note "Concepts explicitly out of scope" from the module's scope boundaries

2. **Audience Profile** for the target persona. Extract and hold:
   - Section 2C (Misconceptions) — the numbered misconception items with severity, persona relevance, and instructional implications
   - Section 3A (Bloom's-mapped outcomes) — the target Bloom's levels for each persona outcome
   - Section 5 (Prerequisites) — what the persona is assumed to already know

**After retrieval, confirm to the user:** List which artifacts you found and any you couldn't locate. If the Audience Profile is not available, ask the user whether to proceed with Needs Analysis data only (lower quality) or wait.

---

### Step 1: Generate Learning Objectives

Using the upstream data, draft learning objectives following these rules:

**For course-level LOs (3–5 objectives):**
- Each objective must ladder to the Course-Level Learning Goal (Needs Analysis Section 3)
- Each objective must address at least one documented performance gap (Needs Analysis Section 2)
- The set of objectives should collectively cover the behavior change stated in the Project Strategy Statement
- Use Bloom's levels from Audience Profile Section 3A — don't default to lower levels unless justified

**For module-level LOs (2–4 objectives per module):**
- Each objective must ladder to one or more course-level LOs
- Each objective must align with the module's learning goal from the Module Scope Map
- Each objective must be achievable within the module's time and format constraints
- If the module's stability rating is **Moderately Stable** or **High Maintenance**, prefer objectives that target understanding, evaluation, or decision-making over objectives that target specific procedural recall

**For all objectives:**
- Begin each objective with a specific, measurable action verb appropriate to the Bloom's level
- Write for the persona described in the Audience Profile — use their frame of reference
- Avoid vague verbs: understand, learn, know, be aware of, appreciate
- Each objective should be testable — if you can't imagine a knowledge check question or activity that proves achievement, the objective is too vague

---

### Step 2: Generate Misconception-Driven Corrective Objectives

Review the misconceptions from Audience Profile Section 2C (or Customer Voice Section D if Audience Profile isn't available). For each misconception rated **Medium or High severity** that is relevant to this course/module:

Generate a **corrective learning objective** — an objective specifically designed to replace the wrong mental model with the correct one.

**Format for corrective objectives:**

```
LO [#]c: [Objective statement]

Type: Corrective — addresses misconception [D# from Audience Profile/Customer Voice]
Misconception: [What they currently believe]
Correct understanding: [What they should believe after this objective is achieved]
Bloom's level: [Typically Analyze or Evaluate — correcting misconceptions requires higher-order thinking than simple recall]
Assessment approach: [How to test — e.g., "Scenario presenting the misconception as a plausible option; learner must identify why it's wrong and select the correct alternative"]
```

**Rules for corrective objectives:**
- Don't just add "distinguish between X and Y" objectives mechanically — only generate a corrective LO if the misconception is genuinely relevant to this module's scope
- If a misconception is better addressed in a different module (based on the sequencing rationale), note that instead of forcing a corrective LO here
- Low-severity misconceptions don't need their own objectives — they can be addressed through narration or knowledge check distractors without a formal LO

---

### Step 3: Compile and Validate

For each objective (standard and corrective), provide:

```
LO [#]: [Objective statement]

Bloom's level: [Remember / Understand / Apply / Analyze / Evaluate / Create]
Addresses gap: [Reference Needs Analysis Section 2 gap — e.g., "Performance Gap #2: Cannot configure governance policies"]
Addresses misconception: [Reference misconception item if corrective, or "N/A"]
Ladders to: [Course-level LO # (for module-level LOs) or Course Learning Goal (for course-level LOs)]
Stability note: [If the topic is Moderately Stable or High Maintenance, note how the objective is written to be durable — e.g., "Written as a decision-making objective rather than procedural recall to accommodate UI changes"]
Assessment evidence: [1 sentence — what activity or question would demonstrate achievement. E.g., "Scenario-based question where learner evaluates a governance policy configuration and identifies the gap"]
```

**Validation checks (run these before presenting the final set):**
- [ ] Every documented performance gap (Needs Analysis Section 2) is addressed by at least one LO
- [ ] Every Medium/High severity misconception relevant to this module has a corrective LO or an explicit note about where it's addressed instead
- [ ] No LO targets a prerequisite (something the Audience Profile Section 5 says they already know)
- [ ] No LO targets content explicitly out of scope for this module
- [ ] The full set of LOs, if achieved, would satisfy the Course-Level Learning Goal
- [ ] Bloom's levels match the Audience Profile Section 3A targets — flag any LO where you deliberately chose a different level and explain why

**🔵 Confidence:** [High / Medium / Low] — [Basis: Are the LOs grounded in documented gaps and misconceptions (high), or inferred from module scope alone (medium), or generated without upstream data (low)? What would change it.]

---

### Output Summary

After the full LO set, provide:

**LO-to-Gap Traceability Matrix:**

| LO # | Objective (short) | Gap Addressed | Misconception Addressed | Bloom's Level | Module |
|---|---|---|---|---|---|
| LO 1 | [abbreviated] | Gap #[X] | — | Apply | Course-level |
| LO 2c | [abbreviated] | Gap #[X] | D[#] | Analyze | Module 2 |

**Coverage check:**
- Gaps with no corresponding LO: [list, or "None — all gaps covered"]
- Misconceptions with no corrective LO: [list with justification — e.g., "D4 (low severity) — addressed through narration in Module 3, not a formal LO"]
- LOs with no gap or misconception backing: [list — these may indicate scope creep or an undocumented gap worth adding to the Needs Analysis]

**Downstream note for Detailed Outline:** When building the outline, each lesson should map to one or more LOs from this set. Corrective LOs (marked with 'c') should be placed at the point in the sequence identified in the misconception's instructional implication (from Audience Profile Section 2C). The traceability matrix above is the input the Outline prompt will consume.

Write in clear, professional prose. Flag any objective where you're uncertain about the right Bloom's level or where the gap evidence is thin — mark with **[NEEDS VALIDATION]**.
````
""",
    "07-detailed-outline": """---
title: Detailed Outline
addie_phase: Design
prompt_order: 7
confluence_page_id: 2466218767
confluence_version: 2
confluence_version_date: 2026-05-06
synced: 2026-06-04
source: https://workato.atlassian.net/wiki/spaces/ETT/pages/2466218767
---

**ADDIE Phase:** Design

**Position:** Runs after Learning Objectives are approved. Consumes the LO set, Needs Analysis Module Scope Map, Audience Profile, Content Audit, and Usage Data to produce a lesson-by-lesson blueprint. Its output feeds Script Drafting, Knowledge Checks, Storyboarding, and the reviewing-outlines skill.

### **When to use**

After LOs are approved by stakeholders and you have completed upstream deliverables. Use this prompt to generate a first-draft lesson-by-lesson structure for a single module before building your storyboard. Run once per module — don't try to outline an entire course in one prompt.

Note: The prompt is set up to generate an outline at the module level. Run multiple times for each course module or adjust the language for your needs.

### Required upstream artifacts

Before running this prompt, the following deliverables must exist. Claude will locate and read them automatically.

* **Learning Objectives** — the full LO set for this module, including the traceability matrix (LO-to-gap and LO-to-misconception mappings). Both course-level and module-level LOs are needed.
* **Needs Analysis (Course Strategy Document)** — specifically:

    * Section 4 (Module Scope Map) — this module's learning goal, content status, stability rating, build complexity, and scope boundaries
    * Section 5 (Sequencing Rationale) — prerequisite logic affecting this module's internal lesson order

* **Audience Profile** — specifically:

    * Section 2C (Misconceptions) — the instructional implications for each misconception, including where in the sequence it should be addressed
    * Section 5 (Prerequisites) — mitigation strategies (bridge content, assume-and-reference, prerequisite course, etc.)
    * Section 6 (Design Implications) — the top 3 design implications for this persona


### Optional upstream artifacts (use if available)

* **Content Audit Section D** (Reuse Opportunities) — assets tagged for reuse in this module
* **Content Audit Section E2** (Per-Topic Stability Ratings) — stability flags for topics covered in this module (also available via Needs Analysis Section 4, but E2 has more detail)
* **Usage Data Section A** (Priority Workflow Ranking) — workflows this module covers, ranked by teaching priority
* **Usage Data Section B** (Struggle Points) — points where users struggle with this module's topics, with scaffolding recommendations

````
You are an instructional designer working on Workato Academy — a technical e-learning curriculum for a SaaS automation platform. You are creating a detailed lesson-by-lesson outline for a single module.

**Module title:** [e.g., Module 2: How Enterprise MCP Works]
**Course this belongs to:** [e.g., Intro to Enterprise MCP]

### Step 0: Retrieve Upstream Artifacts

Before building the outline, locate and read the following upstream deliverables. The user will tell you where each one lives.

**Required — read these before proceeding:**

1. **Learning Objectives** for this module. Extract and hold:
   - The module-level LOs (both standard and corrective)
   - The traceability matrix — which gaps and misconceptions each LO addresses
   - The Bloom's level and assessment evidence for each LO
   - The course-level LOs this module's LOs ladder to

2. **Needs Analysis (Course Strategy Document)** for this course. Extract and hold:
   - Section 4 — this module's entry in the Module Scope Map: learning goal, content status, stability rating, build complexity, known risks
   - Section 5 — sequencing rationale: any prerequisite dependencies affecting this module's internal lesson order (e.g., "Lesson on configuring policies must come after lesson explaining the policy model")
   - Section 7 — SME requirements: which SMEs are assigned to this module and what subject areas they cover (use this to populate the "SME input needed" field per lesson)

3. **Audience Profile** for the target persona. Extract and hold:
   - Section 2C — misconceptions relevant to this module, with instructional implications (where and how to address each)
   - Section 5 — prerequisite mitigation strategies relevant to this module (does the outline need bridge content? An assume-and-reference note? A self-assessment?)
   - Section 6 — top 3 design implications (e.g., "Lead with governance scenarios, not builder workflows")

**Optional — read if the user provides a location:**

4. **Content Audit Section D** — reuse opportunities for this module: assets to reuse as-is (D1), adapt (D2), or repurpose elements from (D3)

5. **Content Audit Section E2** — per-topic stability ratings for topics in this module (more detailed than the module-level rating in the Needs Analysis)

6. **Usage Data Section A** — priority ranking for workflows this module covers (higher-priority workflows get deeper treatment and earlier placement)

7. **Usage Data Section B** — struggle points for this module's topics, with scaffolding recommendations (e.g., "add a guided walkthrough before the lab")

**After retrieval, confirm to the user:** List which artifacts you found, which sections you extracted, and any you couldn't locate.

---

### Step 1: Build the Lesson-by-Lesson Outline

Draft a detailed outline for this module. For each lesson:

```
Lesson [#]: [Title]

Learning objective(s): [LO numbers from the LO set — e.g., "LO 2.1, LO 2.2c"]
Content summary: [3–5 sentences describing what is covered. Be specific — not "covers governance policies"
  but "explains the three-tier policy model (workspace, project, recipe), walks through how policies
  inherit and override, and presents a scenario where a misconfigured policy causes an unintended
  automation to run."]
Modality: [e.g., Narrated concept explanation, Scenario-based walkthrough, Interactive lab,
  Knowledge check, Video demo — choose based on what the content requires and the design
  implications from Audience Profile Section 6]
Approximate time: [minutes]

Misconception addressed: [If this lesson addresses a corrective LO, reference the misconception:
  "Addresses misconception D2 (users confuse MCP with standard API access) — lesson uses a
  side-by-side comparison to surface the distinction before teaching MCP-specific configuration."
  If no misconception is addressed in this lesson, write "None."]

Stability flag: [If this lesson covers a topic rated Moderately Stable or High Maintenance
  in Content Audit E2 or Needs Analysis Section 4:
  "⚠️ Stability: [Moderately Stable / High Maintenance] — [topic]. Last verified: [date].
  Script should prefer concepts over specific UI steps. Screenshots will need version check
  before production."
  If the topic is Evergreen, write "Evergreen — no stability concerns."]

Reusable assets: [Reference specific assets from Content Audit Section D:
  "Reuse as-is: [Asset A3 — OAuth configuration diagram from Foundations course]"
  "Adapt: [Asset A7 — API overview doc, needs MCP-specific framing]"
  "Repurpose element: [Extract the 3-step flow diagram from Asset A12]"
  If no reusable assets apply, write "None — net-new content."]

Scaffolding: [If Usage Data Section B identifies a struggle point at this stage:
  "Scaffolding needed: Usage Data B2 shows 60% of users abandon during initial configuration.
  Add guided walkthrough with checkpoint moments before the lab activity."
  If no scaffolding is flagged, write "Standard — no additional scaffolding needed."]

SME input needed: [If this lesson requires SME validation before scripting, note what specifically
  and reference the assigned SME from Needs Analysis Section 7:
  "SME needed: [Name from Section 7, subject area] — Confirm whether the 3-tier policy model is
  still accurate post-Q2 release (stability flag)."
  If no SME input is needed, write "None — content is validated."]
```

---

### Step 2: Place Misconceptions in the Sequence

After drafting the lesson list, review the misconception inventory from Audience Profile Section 2C. For each misconception relevant to this module:

- Confirm it's placed in the right lesson (per the instructional implication from Section 2C)
- Confirm the placement makes pedagogical sense — the misconception should be addressed *after* the correct concept is introduced but *before* the learner needs to apply the correct understanding
- If a misconception from the Audience Profile says "address in Module X" but this outline is for Module Y, note that the misconception is deferred — don't force it into the wrong module

**Misconception Placement Summary:**

| Misconception | Severity | Placed in Lesson | Corrective LO | Approach |
|---|---|---|---|---|
| D[#]: [label] | [H/M/L] | Lesson [#] | LO [#]c | [Brief — e.g., "Side-by-side comparison before config lesson"] |
| D[#]: [label] | [H/M/L] | Deferred to Module [X] | — | [Why — e.g., "Requires understanding of [concept] taught in Module 3"] |

---

### Step 3: Validate and Summarize

**Sequencing rationale:** [2–3 sentences explaining why lessons are ordered this way. Reference:
- Prerequisite logic from Needs Analysis Section 5
- Misconception placement logic (corrective content comes after the concept it corrects)
- Usage Data priority ranking (higher-priority workflows appear earlier)
- Scaffolding placement (struggle points get support before the challenging content)]

**Validation checks:**

- [ ] Every module-level LO is addressed by at least one lesson
- [ ] Every lesson maps to at least one LO — no decorative lessons without a learning purpose
- [ ] Every Medium/High severity misconception relevant to this module is placed in a lesson or explicitly deferred with rationale
- [ ] Stability flags are applied to every lesson covering a Moderately Stable or High Maintenance topic
- [ ] Reusable assets from Content Audit are referenced where applicable — no redundant creation
- [ ] Scaffolding from Usage Data struggle points is placed at the right point in the sequence
- [ ] Prerequisite mitigation strategy from Audience Profile Section 5 is reflected (bridge content, assume-and-reference, etc.) — typically in Lesson 1 or as a pre-module note
- [ ] Design implications from Audience Profile Section 6 are reflected in modality and content choices
- [ ] Total estimated time aligns with the module's time allocation in the Module Scope Map

**LO Coverage Matrix:**

| LO # | Objective (short) | Covered in Lesson(s) | Assessment in |
|---|---|---|---|
| LO [#] | [abbreviated] | Lesson [#] | [Knowledge check / Scenario in Lesson X / End-of-module quiz] |
| LO [#]c | [abbreviated] | Lesson [#] | [Distractor-based question targeting misconception D#] |

**Module summary:**
- Total lessons: [N]
- Estimated total time: [X] minutes
- Net-new content: [N] lessons
- Adapted/reused content: [N] lessons
- Stability-flagged lessons: [N] — [list which ones]
- Misconceptions addressed: [N] — [list which ones]
- Misconceptions deferred: [N] — [list with target modules]

**🔵 Confidence:** [High / Medium / Low] — [Basis: Are lessons grounded in upstream data (LOs, gaps, misconceptions, usage data) or inferred from topic scope alone? Which lessons have thin upstream backing? What would increase confidence — e.g., "Lessons 3–4 cover topics where Usage Data had no struggle point data. SME review would confirm whether scaffolding is needed."]

---

Write in clear, professional prose. Use the lesson format exactly as specified — downstream prompts (Script Drafting, Storyboarding) reference lessons by number and expect these fields. Flag any lesson where scope is uncertain with **[SCOPE TBD — SME INPUT NEEDED]**.
````
""",
    "08-script-drafting": """---
title: Script Drafting
addie_phase: Develop
prompt_order: 8
confluence_page_id: 2466251461
confluence_version: 5
confluence_version_date: 2026-05-13
synced: 2026-06-04
source: https://workato.atlassian.net/wiki/spaces/ETT/pages/2466251461
---

**ADDIE Phase:** Develop

**Position:** Runs after the Detailed Outline is approved. Consumes the per-lesson blueprint from the Outline, retrieves Customer Voice data for proof points and customer language, and extends with lesson-specific examples. Its output feeds Storyboarding, and through the storyboard, production.

### When to use

After the Detailed Outline is approved. Use per lesson — don't try to script an entire module in one prompt. Paste in the lesson outline entry and any reference material so the AI writes from your actual content, not from general knowledge about the topic.

### Required upstream artifacts

Before running this prompt, the following deliverables must exist. Claude will locate and read them automatically.

* **Detailed Outline** — specifically this lesson's entry, including: LOs, content summary, modality, misconception addressed, stability flag, reusable assets, and scaffolding notes
* **Customer Voice Research Brief** — specifically:

    * Section B (Success Stories) — for concrete examples in narration
    * Section C1 (Customer Language Patterns) — for matching narration tone to how customers actually talk
    * Section C2 (Use Case Inventory) — for real scenarios
    * Section E (Proof Points) — for validated stats and metrics to weave into narration


### Optional upstream artifacts (use if available)

* **Audience Profile** — specifically:

    * Section 2B (Transferable Skills) — analogies and mental models to leverage in explanations
    * Section 2C (Misconceptions) — if this lesson addresses a corrective LO, the full misconception detail for scripting the correction
    * Section 4 (Motivation & Resistance) — tone guidance: what engages vs. disengages this persona

* **Usage Data Section D** (Success Patterns) — what power users do that others don't, for "here's what good looks like" narration

```markdown
You are writing narration scripts for Workato Academy — a technical e-learning curriculum for a SaaS automation platform. You write in a professional but conversational voice: clear, direct, jargon-conscious, and always oriented toward what the learner needs to do or decide, not just what they need to know.

**Lesson title:** [e.g., Lesson 2: How MCP Connects AI Models to Your Workflows]
**Module this belongs to:** [e.g., Module 2: How Enterprise MCP Works]
**Course:** [e.g., Intro to Enterprise MCP]

### Step 0: Retrieve Upstream Artifacts

Before writing, locate and read the following upstream deliverables. The user will tell you where each one lives.

**Required — read these before proceeding:**

1. **Detailed Outline** — this lesson's entry. Extract and hold:
   - Learning objective(s) and Bloom's levels
   - Content summary (the 3–5 sentence blueprint for what to cover)
   - Modality (narrated slides, scenario, lab, video — determines writing style)
   - Misconception addressed (if any — which misconception, and the approach specified in the outline)
   - Stability flag (Evergreen / Moderately Stable / High Maintenance — determines whether to write concept-focused or procedure-focused narration)
   - Reusable assets (existing content to reference or adapt)
   - Scaffolding notes (additional support needed at this point in the sequence)

2. **Customer Voice Research Brief** for this course. Extract and hold:
   - Section B (Success Stories) — customer examples with before/after quotes and metrics
   - Section C1 (Customer Language Patterns) — how customers talk about this topic vs. how we talk about it
   - Section C2 (Use Case Inventory) — real workflows to use as scenario foundations
   - Section E (Proof Points) — validated stats, with external-use approval status

   **Check the brief's metadata header:** If older than 6 months, flag to the user.

   **Extend with lesson-specific research (if needed):**
   After retrieving the Customer Voice brief, check whether it contains success stories, proof points, or scenarios specific enough for *this lesson's* topic. If the brief covers the course topic broadly but lacks examples for this specific lesson:
   - Search Gong for 2–3 customer calls mentioning **[this lesson's specific feature/concept]** — look for before/after examples and outcomes
   - Search Highspot for proof points specific to this lesson's topic
   - Tag any new findings as "[New — not in Customer Voice brief]" so the source is traceable
   - If new findings are significant, note them for backfill into the Customer Voice brief

**Optional — read if the user provides a location:**

3. **Audience Profile** — extract and hold:
   - Section 2B (Transferable Skills) — mental models and analogies to leverage. E.g., if the persona is familiar with RBAC from Azure AD, use that as an anchor: "You already know how role-based access works in Azure AD — MCP extends that concept to AI model permissions."
   - Section 2C (Misconceptions) — if this lesson addresses a corrective LO, get the full misconception detail: what they believe, why it's wrong, why they hold it. Script the correction to surface the misconception before replacing it.
   - Section 4A (Motivation) — what drives this persona. Lead with what matters to them.
   - Section 4B (Resistance) — what might cause them to disengage. Avoid those triggers in tone and content choices.

4. **Usage Data Section D** (Success Patterns) — what power users do differently. Use for "here's what successful teams do" narration moments.

**After retrieval, confirm to the user:** List which artifacts you found, any lesson-specific Gong/Highspot research you ran, and any artifacts you couldn't locate.

---

### Step 0.5: Read Sibling Scripts in the Course Folder

Before writing, scan the course's Scripts folder for previously developed lesson scripts. These are **canon** — your script must be consistent with them. This is additive to Step 0: the Outline tells you *what* to write; sibling scripts tell you *how it must fit* with what's already been written.

**Where to look:**
- Default location: the mounted course folder, typically under a `Scripts/` subfolder
- Filename pattern: files containing `Lesson X.Y` and `Script` in the name (any extension: `.gdoc`, `.md`, `.docx`). Separators vary (`:`, `—`, parens around "Script") — match flexibly.
- Include both completed scripts and drafts in revision. If multiple versions exist for the same lesson (e.g., `v2`, `REVISED`), prefer the most recently modified.

**How to read them:**
- Parse the labeled header block at the top of each script. Common fields: Module, Course, Type/Format, Target length, Learning objective, Tone, Persona, Key constraint, Modality. The schema varies slightly across courses — extract what's present rather than expecting a fixed structure.
- Skim the narration for terminology, recurring examples, personas, and analogies that have already been established.

**What to extract and hold:**
- **Established terminology** — terms already defined or used consistently (e.g., "skill" vs. "tool," "control plane," "agent" vs. "assistant"). Match what's there; don't redefine or rename.
- **Recurring examples and personas** — if earlier lessons established a character (e.g., "Maya, the L&D admin") or a scenario (e.g., the offboarding example, the John Smith case), reuse rather than invent parallel ones.
- **Content already covered** — what concepts have been taught. Don't re-explain from scratch; reference and build.
- **Tone calibration** — sentence rhythm, contraction use, level of formality, how technical terms are introduced.
- **Forward references made in earlier scripts** — if a prior lesson promised "we'll cover X later in the course," check whether your lesson is the one that should honor that promise.

**After scanning, report to the user:**
- Which sibling scripts you found (filenames and lesson numbers)
- Key terminology, personas, and examples you'll carry forward
- Any forward references from earlier scripts that this lesson should honor
- Any inconsistencies you noticed (e.g., a term defined two different ways across earlier lessons) — flag for SME resolution, don't silently pick one

If no sibling scripts are found, note that this appears to be the first script in the course and proceed without canonical references.

---

### Step 1: Apply Upstream Context to Script Decisions

Before writing, make these decisions based on upstream data:

**Writing style (from Outline modality):**
- Self-paced text blocks (Text, Accordion, Tabs, Process, etc.): Write for the screen — clear, scannable prose. Learners read at their own pace.
- Video/Multimedia blocks: Write for the ear — contractions, short sentences, natural spoken rhythm.

**Concept vs. procedure (from Outline stability flag):**
- **Evergreen topic:** Free to write specific procedures, name specific UI elements, describe exact steps.
- **Moderately Stable topic:** Lead with the concept and decision framework. Include specific steps but frame them as "currently, you would..." and add a production note flagging which claims need freshness verification before recording.
- **High Maintenance topic:** Write concept-focused narration. Teach the *why* and *when*, not the *exact how*. Reference the product capability without locking into specific UI paths. Add a production note: "⚠️ This section covers a rapidly evolving feature. Verify all product references with SME before recording. Prefer screen recording over screenshots for production — recordings can be re-captured more easily."

**Misconception handling (from Outline misconception field):**
- If this lesson addresses a misconception: Surface it early in the lesson ("You might assume that..." or "A common approach is to..."), then pivot to the correct understanding with a clear explanation of why the misconception doesn't hold. Don't just state the correct answer — explain why the wrong answer feels right and what makes it wrong.
- If no misconception is addressed: Proceed normally.

**Tone (from Audience Profile Section 4):**
- Lead with what motivates this persona (Section 4A)
- Avoid triggers that cause disengagement (Section 4B)
- Match the persona's frame of reference — don't explain things from a builder's perspective to a governance lead, or vice versa

**Analogies (from Audience Profile Section 2B):**
- Use transferable skills as bridges: "If you've managed [familiar concept], think of [new concept] as..."
- Note where the analogy breaks down — transferable skills have limits, and the Audience Profile documents what does NOT transfer

---

### Step 2: Write the Script

Write a full narration script for this lesson. Format as:

**[Slide/Block 1 title]**
[Narration text or on-screen text, depending on modality]

**[Slide/Block 2 title]**
[Narration text or on-screen text]

(continue for each slide/block)

**Guidelines:**
- Write for the ear (video blocks) or for the screen (self-paced blocks) — not both
- Introduce each new concept with a brief "why it matters" before explaining what it is
- Avoid acronyms on first use without spelling them out
- End the lesson with a 1–2 sentence transition that sets up the next lesson
- Do not include stage directions, visual notes, or interaction instructions — narration/text only (those go in the storyboard)

### Callback and forward-reference conventions

When referencing prior or future lessons, use loose, durable phrasing that survives course reorganization. The structural position of any lesson may shift between drafting and publishing — your references should still make sense if Lesson 1.3 becomes Lesson 1.4, or if Module 2 gets resequenced.

**Reference the concept or moment, not the structural position:**
- ✅ "earlier in this module," "in a previous lesson," "as we saw when introducing recipes," "In Module 1, we covered..."
- ❌ "in Lesson 1.3," "in Module 2, Lesson 4," "two lessons ago"

Module-level references are acceptable — they're stable enough to survive most reorganizations. Lesson-number references inside or across modules are not.

**Forward references must point to scripts that exist:**
- Before writing any forward reference, confirm the target lesson has a script in the Scripts folder (verified during Step 0.5).
- If the target script doesn't exist yet, use a soft tease with no lesson identifier: "we'll come back to skill description design later," "more on this in a future lesson."
- If a specific forward reference is critical to the pedagogy and the target script doesn't exist yet, flag it as **[FORWARD REF — UNCONFIRMED]** so the reviewing-scripts skill can catch it.

**Re-activate concepts, don't just point to them.** The best callbacks bring the prior concept back into the learner's head, not just remind them where to find it.
- ✅ "Remember the offboarding example — the AI agent that locked out the wrong John Smith? That cascading failure is exactly what governance prevents."
- ❌ "As we saw in an earlier lesson's offboarding example, governance is important."

### Narration style: Customer-informed, not customer-quoting

Customer Voice data grounds your narration in reality — but the goal is to sound like an **instructor who deeply understands the learner's world**, not a salesperson citing testimonials. Use customer data to inform *what* you teach and *how* you frame it, not as direct quotes or case study references.

**Ground examples in real scenarios, but generalize them for instruction:**
- ✅ "Imagine you're a platform admin reviewing audit logs every week — manually checking which AI recipes ran, what they accessed, and whether anything violated your governance policies. That's the problem MCP's audit framework is designed to solve."
- ❌ "One enterprise customer told us they were spending 8 hours a week reviewing logs..." (sounds like a sales pitch)
- ❌ "Many organizations struggle with log management..." (sounds like marketing copy)

The customer data from Section C2 tells you what scenarios are real. Your job is to teach *from* those scenarios as if they're common knowledge — because for this persona, they are.

**Use proof points to add credibility, but frame them as industry context, not testimonials:**
- ✅ "Teams that implement automated audit workflows typically see troubleshooting time drop by more than half within the first month." [Source: CV-E3]
- ❌ "Our customers report a 60% reduction in troubleshooting time." (sounds like a sales deck)
- ❌ "This can save time and improve efficiency." (too vague to be useful)

**Don't quote customers directly in narration.** Direct quotes ("As one customer told us...") make e-learning sound like a case study webinar. Instead, absorb the insight behind the quote and teach it as a principle or scenario:
- ✅ "The shift here is from reactive firefighting — investigating after something goes wrong — to proactive policy enforcement, where guardrails prevent problems before they happen."
- ❌ "As one platform admin described it: 'This changed how we think about automation governance. We went from reactive firefighting to proactive policy enforcement.'"

The customer's insight is the same in both versions — but the first teaches it, and the second sells it.

**Match customer language from Section C1:**
- Use the terms customers use, not product marketing terms — the Customer Voice brief documents both
- When introducing a product term that differs from customer language, bridge it: "What you might think of as [customer term] is what Workato calls [product term]."
- Avoid jargon the brief flags as unused by customers — if they don't say it, don't teach with it

**Always cite sources in script notes (never in narration):**
- Include Customer Voice section/item references (e.g., [CV-B2], [CV-E5]) and Gong call IDs so the ID and SMEs can verify accuracy
- For any lesson-specific examples found during the extend step, include the tag: [New — not in Customer Voice brief, Gong call ID: XXX]
- The learner should never know you're drawing from customer data — the narration should feel like expert instruction, not research findings

---

### Step 3: Add Production Notes

After the script, add:

**Production notes for this lesson:**

- **Stability:** [Carry forward the stability flag from the Outline. If Moderately Stable or High Maintenance, list specific claims or product references that need freshness verification before recording. E.g., "Verify the 3-tier policy model is still current — Needs Analysis Section 8 flagged Q3 release risk."]
- **Misconception handling:** [If a misconception was addressed, note it for the reviewing-scripts skill: "This lesson addresses misconception D2. The correction is scripted in Slide 3 using a side-by-side comparison. Reviewers should verify the correct understanding is still accurate."]
- **Customer voice sources used:** [List all CV references used in the script — e.g., "CV-B2 (success story), CV-C1 (language pattern), CV-E3 (proof point), CV-E7 (proof point)"]
- **Lesson-specific research:** [List any new findings from the extend step — e.g., "Found 2 additional Gong calls specific to this lesson's topic: [call IDs]. New example used in Slide 2 tagged as [New — not in CV brief]."]
- **Scaffolding implemented:** [If the Outline flagged scaffolding needs, note how they were addressed in the script — e.g., "Usage Data B2 flagged configuration drop-off. Added guided walkthrough framing in Slides 2–3 with checkpoint language."]
- **Analogies used:** [List transferable skill bridges used — e.g., "Used Azure AD RBAC analogy from Audience Profile Section 2B in Slide 1. Noted where the analogy breaks down (nested vs. flat hierarchy) in Slide 3."]

**Estimated narration time:** [word count ÷ 150 words/min for narration, or reading time estimate for self-paced blocks]

**🔵 Confidence:** [High / Medium / Low] — [Basis: Is the script grounded in upstream data (outline, customer voice, audience profile) or written from general knowledge? Are proof points validated? Are stability-flagged sections verified? What would increase confidence — e.g., "Proof point in Slide 4 is from a 5-month-old Gong call — SME should confirm the metric is still accurate."]

---

Write in clear, professional prose appropriate to the modality. Flag any slide where content is uncertain with **[NEEDS SME VERIFICATION]** and explain what's in question.
```
""",
    "09-knowledge-checks": """---
title: Knowledge Checks & Quiz Questions
addie_phase: Develop
prompt_order: 9
confluence_page_id: 2467692837
confluence_version: 7
confluence_version_date: 2026-05-27
synced: 2026-06-04
source: https://workato.atlassian.net/wiki/spaces/ETT/pages/2467692837
---

**ADDIE Stage:** Develop

**Position:** Runs after lesson scripts are drafted (or after the Detailed Outline is approved, if writing assessments before scripts). Consumes Learning Objectives (with Bloom's levels), misconception data (threaded from Customer Voice through Audience Profile and Outline), and Usage Data struggle points. Its output feeds Storyboarding (for knowledge check blocks) and the reviewing-scripts/storyboards skills.

### **When to use**

After lesson content is drafted or the Detailed Outline is complete for a module. Use to generate a first-draft question set — always review and edit for accuracy before including in a course. Works best when you have the lesson outline and/or script available so questions are grounded in what was actually taught.

#### Required upstream artifacts

Before running this prompt, the following deliverables must exist. Claude will locate and read them automatically.

* **Learning Objectives** — the module-level LOs with Bloom's levels, traceability matrix, and assessment evidence notes. Bloom's level determines question complexity; corrective LOs (tagged with 'c') generate misconception-based distractors.
* **Detailed Outline** — the module's lesson-by-lesson blueprint, specifically:

    * LO coverage matrix (which LOs are covered in which lessons)
    * Misconception placement summary (which misconceptions were addressed and where)
    * Content summaries per lesson (what was taught — questions should test this, not outside knowledge)


### Optional upstream artifacts (use if available)

* **Customer Voice Section D** (Misconception Inventory) — the full misconception detail: what they believe, why it's wrong, why they hold it. Used to build distractors that reflect real wrong answers, not fabricated ones.
* **Usage Data Section B** (Struggle Points) — where users actually fail, with metrics. Used to build scenario stems grounded in real failure patterns.
* **Usage Data Section C** (Adoption Barriers) — prerequisite gaps that cause real-world mistakes. Used for scenario context.
* **Audience Profile Section 2C** (Misconceptions) — persona-specific misconception mapping with severity ratings. Helps prioritize which misconceptions deserve their own questions vs. appearing as distractors in other questions.
* **Lesson scripts** (if drafted) — paste the narration or on-screen text for the lessons being assessed. Questions should test what was taught, in the way it was taught.
* **Storyboards** (if drafted) — used in optional Step 2.5 to cross-check against in-module KC blocks and avoid duplicate questions.

### Rise 360 Question Types — Reference

The prompt below assumes the assessment will be delivered in Articulate Rise 360. Different Rise question blocks support different feedback patterns, and this directly affects how the question and its feedback should be written.

| Rise block | Best for | Feedback behavior | Constraints |
| --- | --- | --- | --- |
| **Multiple Choice** | Single-correct scenario or recall | Per-option feedback (1 correct + 3 incorrect, one per distractor) OR single binary | 4 options max in practice |
| **Multiple Response** (multiselect) | Testing 2+ related concepts in one question | Binary only — 1 correct (exact match required) + 1 incorrect (any other combo) | No partial credit; no per-option feedback. The incorrect message must teach the principle regardless of which specific mistake the learner made |
| **Matching** | Vocabulary-to-concept, scenario-to-category | Single completion feedback | Best with 3–4 pairs; gets cramped on mobile beyond that |
| **Sorting** | Categorizing 4–6 items across 2–4 buckets | Per-attempt or completion feedback | Confirm mobile layout for ≥6 items |
| **Fill-in-the-Blank** | Terminology or specific phrasing recall | Single correct/incorrect | Brittle — accepts only exact matches by default |

`````markdown

````
You are an instructional designer creating assessment questions for Workato Academy — a technical e-learning curriculum for a SaaS automation platform.

**Module title:** [e.g., Module 2: How Enterprise MCP Works]
**Course:** [e.g., Intro to Enterprise MCP]
**Assessment type:** [e.g., End-of-module knowledge check — 3–5 questions; not a certification exam]
**Question format:** [Specify per question. Rise 360 supports: Multiple Choice (1 correct, 3 distractors) / Multiple Response (multiselect, 2+ correct out of 4) / Matching (pair items across columns) / Sorting (items into categories) / Fill-in-the-Blank. Match the format to the cognitive task; scenario-based where possible.]
**Pass criteria:** [Default: gated, ≥80% first-attempt correct (Workato Academy standard). Override only if the KC is formative / not gated.]

### Step 0: Retrieve Upstream Artifacts

Before writing any questions, locate and read the following upstream deliverables. The user will tell you where each one lives.

**Required — read these before proceeding:**

1. **Learning Objectives** for this module. Extract and hold:
   - Each module-level LO with its Bloom's level
   - Corrective LOs (tagged 'c') — these target specific misconceptions and should generate misconception-based questions
   - Assessment evidence notes — the LO prompt's suggestion for how to test each objective
   - The traceability matrix — which gaps and misconceptions each LO addresses

2. **Detailed Outline** for this module. Extract and hold:
   - LO Coverage Matrix — which LOs are covered in which lessons
   - Misconception Placement Summary — which misconceptions were addressed, in which lessons, using what approach
   - Content summaries per lesson — what was actually taught (questions must stay within this scope)

**Optional — read if the user provides a location:**

3. **Customer Voice Section D** (Misconception Inventory) — the numbered misconceptions with:
   - What customers believe (the wrong answer → distractor)
   - Why they hold it (helps write plausible distractor rationale)
   - Severity rating (High/Medium misconceptions get their own questions; Low misconceptions appear as distractors in other questions)

4. **Usage Data Section B** (Struggle Points) — where users actually struggle, with:
   - What happens (the failure → scenario stem)
   - Hypothesized cause (the knowledge gap → what the question tests)
   - Percentage affected (helps calibrate question difficulty — if 60% of users struggle with this, it's a core question, not an edge case)

5. **Usage Data Section C** (Adoption Barriers) — prerequisite gaps that cause real mistakes. Used for scenario context that feels authentic.

6. **Lesson scripts** (if available) — paste or point to the narration/on-screen text for the lessons this assessment covers. Questions should test what was taught, using similar framing and terminology.

7. **Storyboards** (if available) — used in optional Step 2.5 to check for in-module KCs on the same content.

**Extend with lesson-specific failure modes (if needed):**
After retrieving the upstream artifacts, check whether you have enough real failure scenarios and misconceptions to build all distractors. If the upstream data is thin for specific lessons:
- Search Gong for troubleshooting calls about **[this module's specific topic]** — look for mistakes customers make
- Search Slack (#solutions-engineering, relevant product channels) for repeated questions about this topic
- Tag any new findings as "[New — not in upstream briefs]"

**After retrieval, confirm to the user:** List which artifacts you found and any you couldn't locate.

---

### Step 1: Map Questions to LOs and Bloom's Levels

Before writing questions, create a question plan:

| Question # | LO Assessed | Bloom's Level | Rise Block Type | Misconception Used | Source for Distractors |
|---|---|---|---|---|---|
| Q1 | LO 2.1 | Apply | Multiple Choice | — | Usage Data B2 (config failure) |
| Q2 | LO 2.2c | Analyze | Multiple Response | D2 | Customer Voice D2 |
| Q3 | LO 2.3 | Apply | Multiple Choice | D4 (as distractor) | Usage Data B3 |

**Rules for the question plan:**
- Every module-level LO should be assessed by at least one question
- Corrective LOs (tagged 'c') must generate a question that specifically tests whether the learner has replaced the misconception with the correct understanding
- Bloom's level determines question complexity:
  - Remember/Understand → Direct questions (but avoid pure definition recall — even these should require some application)
  - Apply → Scenario-based: "Given this situation, what should you do?"
  - Analyze → Diagnostic: "This workflow is failing. Based on the symptoms, what is the most likely cause?"
  - Evaluate → Judgment: "Which approach would be most effective for this governance scenario, and why?"
- Rise block type should match the cognitive task — see the Rise 360 Question Types reference. Multiple Response is efficient when testing 2+ related concepts in one question but provides only binary feedback; if per-option teaching is critical, prefer Multiple Choice.
- Higher-priority struggle points (from Usage Data Section B) should appear in earlier questions

---

### Step 2: Write Questions

Generate [number] knowledge check questions. For each question provide the structure below. **Learner-facing content (stem, options, correct answer, feedback) sits at the top of each question; review-only metadata (LO, misconception, Rise block type, LO connection, sources, ID notes) is grouped at the bottom under a clear divider** so the CD can see at a glance what ships in Rise vs. what's internal.

```
Q[#]: [Question stem]

A. [Option text]
B. [Option text]
C. [Option text]
D. [Option text]

Correct answer: [Letter(s)]

Learner-facing feedback (write according to the Rise block type's feedback structure — see Rise 360 Question Types reference):

[For Multiple Choice — per-option feedback:]
- Correct ([Letter]): [Teach the principle the option tests. 1–2 sentences.]
- Incorrect ([Letter]): [Explain why this option is wrong and what concept the learner should re-anchor on. 1–2 sentences.]
- Incorrect ([Letter]): [Same as above for this distractor.]
- Incorrect ([Letter]): [Same as above for this distractor.]

[For Multiple Response — binary feedback only:]
- Correct feedback (triggers only when the learner selects the EXACT correct set — no more, no less): [Affirm the principle being tested, naming the correct options and the key idea each represents.]
- Incorrect feedback (triggers for every other combination — missing one correct, picking a distractor, picking only one of the correct options): [Teach the underlying principle regardless of which specific mistake the learner made. Name both correct answers and the misconception each distractor reflects.]

[For Matching / Sorting — single completion feedback:]
- Correct completion: [Affirm the pattern the learner just demonstrated.]
- Incorrect: [Teach the principle that should guide the matches/sorts.]

— — — Review metadata (not learner-facing) — — —

LO assessed: [LO number and Bloom's level]
Misconception targeted: [D# if this is a corrective question, or "None"]
Rise block type: [Multiple Choice / Multiple Response / Matching / Sorting / Fill-in-the-Blank]
LO connection: [One sentence noting how this question tests the LO. For ID/SME review only — not learner-facing.]

Sources:
- Scenario stem based on: [CV-C2 item #, Usage Data B# or C#, or "Lesson content"]
- Distractor A based on: [CV-D#, Usage Data B#, or "Common misconception from Gong/Slack"]
- (etc.)

ID notes (optional — flags only): [Use only to flag distractor sourcing concerns, feature/positioning verification needs, or other internal review items. Do NOT restate why the answer is correct — that lives in the learner-facing feedback.]
```

---

### Step 2.5 (optional): Cross-check against existing in-module KCs

**Use this step when:** writing an end-of-course or capstone KC, OR when the module's storyboards already include knowledge check blocks on the same lessons.

For each question, check whether an in-module KC in the storyboards already tests the same concept. If so, note how this question differs:
- Different scenario / context?
- Different Bloom's level (e.g., Understand vs. Apply)?
- Different misconception or distractor focus?
- Different cognitive task (matching vs. discrimination)?

If a question is too close to an existing in-module KC, revise it to add new evidence rather than repeat the test. Document the deconfliction logic in a brief note under each affected question so a future reviewer can see the rationale.

---

### Writing guidelines

**Scenario stems — grounded in reality, generalized for instruction:**
- Use real customer scenarios from Customer Voice Section C2 and Usage Data Section B as foundations, but generalize them (same principle as Script Drafting — teach from the scenario, don't cite the customer)
- ✅ "A platform admin has configured an MCP connection for their AI agent, but the agent is returning errors when trying to access recipe data. The audit log shows the connection authenticated successfully."
- ❌ "One of our customers reported that their MCP connection was failing..." (sounds like a support ticket, not an assessment)

**Distractors — based on real mistakes, not random wrong answers:**

Good distractors are based on real mistakes customers make. Every distractor should pass the "would a real learner choose this?" test.

- ✅ "Check the data source permissions at the account level" — This is what many users try first (from Usage Data B2), but the actual issue is at the connection level. The distractor is plausible because the learner hasn't yet internalized the permission hierarchy.
- ✅ "Increase the rate limit threshold" — This seems logical if you misunderstand the error as a rate limit issue (misconception D3), but the root cause is authentication scope.
- ❌ "Delete all data and start over" — No real learner would choose this. It's filler, not a distractor.
- ❌ "Configure the workflow to fail intentionally" — Obviously wrong. Wasting an option slot.

**Distractor quality checklist:**
1. Each distractor should be traceable to a real mistake — from Customer Voice Section D, Usage Data Section B, or lesson-specific Gong/Slack research
2. Each distractor should be plausible to someone who hasn't mastered the learning objective
3. The feedback for why it's wrong should teach something valuable — not just "this is incorrect"
4. Distractors should be similar in length and detail to the correct answer
5. **Distractors must not reinforce a misconception on the way to being wrong.** A distractor that uses inaccurate framing (e.g., "the agent's training data" when the correct mechanism is "context") teaches the wrong mechanism even when learners pick a different answer. Every option should be accurate on its own terms.
6. **Option text should not telegraph the answer.** Don't include product definitions or description glosses next to product names if the stem already implies the answer by describing the function. Keep option text terse; teach in the feedback.

**General rules:**
- Avoid "all of the above" and "none of the above" options
- Do not use negative phrasing in question stems (e.g., "Which of the following is NOT...")
- Questions should test application and judgment, not recall of definitions or trivia
- Write in plain language — the question stem should never be harder to read than the content it's assessing
- Distractors should be similar in length and detail to the correct answer so they don't stand out
- **Calibrate against the ≥80% first-attempt pass criterion.** Distractors must be plausible to someone who hasn't mastered the LO, but the correct answer must be clearly right to a learner who has internalized the lesson content. Avoid trick questions, ambiguous "correct" answers, or distractors that are technically defensible alternatives. First-attempt correct on a gated KC is the design target, not a stretch goal.

---

### Step 3: Validate and Summarize

**Assessment Coverage Matrix:**

| LO # | Objective (short) | Assessed by Q# | Bloom's Level Matched? | Misconception Tested? |
|---|---|---|---|---|
| LO 2.1 | [abbreviated] | Q1 | ✅ Apply → scenario | — |
| LO 2.2c | [abbreviated] | Q2 | ✅ Analyze → diagnostic | D2 ✅ |

**Validation checks:**
- [ ] Every module-level LO is assessed by at least one question
- [ ] Every corrective LO generates a question that specifically targets the misconception
- [ ] Question complexity matches the LO's Bloom's level (no recall questions for Apply-level LOs)
- [ ] Every distractor is traceable to a real mistake (upstream source cited)
- [ ] No question tests content outside what was taught in this module's lessons
- [ ] No question tests prerequisite knowledge (from Audience Profile Section 5) — only what this module taught
- [ ] Scenario stems reflect realistic situations, generalized for instruction (no customer citations in question text)
- [ ] Each question specifies its Rise block type
- [ ] Feedback structure matches the Rise block type's capabilities (per-option for Multiple Choice; binary for Multiple Response; single completion for Matching/Sorting)
- [ ] For Multiple Response questions, the incorrect feedback works for any wrong combination — not just the most likely one
- [ ] No distractor reinforces a misconception, even one outside the question's scope
- [ ] The question set is calibrated for ≥80% first-attempt correct on a gated KC. No trick questions, no ambiguous correct answers, no distractors that are technically defensible alternatives to the right answer.
- [ ] Per-question template structure followed — learner-facing content at top, review metadata grouped below the divider

**Distractor source summary:**

| Source Type | Count | Examples |
|---|---|---|
| Customer Voice misconceptions (D#) | [N] | D2, D4 |
| Usage Data struggle points (B#) | [N] | B2, B3 |
| Usage Data adoption barriers (C#) | [N] | C1 |
| Lesson-specific research (Gong/Slack) | [N] | [New — call IDs] |
| Inferred (no upstream source) | [N] | [Flag these — they should be the minority] |

**🔵 Confidence:** [High / Medium / Low] — [Basis: Are distractors grounded in real misconceptions and failure data (high), or inferred from topic knowledge (medium), or fabricated without upstream data (low)? Which questions have the weakest distractor sourcing? What would increase confidence — e.g., "Q4 distractors are inferred — a quick Slack search in #solutions-engineering for [topic] would validate or replace them."]

---

Write clearly and precisely. Flag any question where the distractor sourcing is weak with **[DISTRACTOR SOURCING — NEEDS DATA]** so the ID knows to strengthen it before publishing.
````
`````
""",
    "10-storyboarding": """---
title: Storyboarding
addie_phase: Develop
prompt_order: 10
confluence_page_id: 2510192874
confluence_version: 8
confluence_version_date: 2026-05-28
synced: 2026-06-04
source: https://workato.atlassian.net/wiki/spaces/ETT/pages/2510192874
---

**ADDIE Stage**: Develop

**Position:** Runs after Script Drafting (and optionally after Knowledge Checks, if assessment blocks are included in the storyboard). Consumes the lesson's script and production notes, Detailed Outline per-lesson metadata, and Learning Objectives. Its output is the final production blueprint — the handoff to Content Development for Rise 360 build, and (for lessons with Video / Multimedia / Custom Needed visuals) the source for the **Mockup Companion** prompt that produces a visual reference deck for the video editor.

### When to use

After a lesson script is approved (or after both the script and knowledge checks are approved, if the lesson includes assessment blocks). This prompt translates approved content into a block-by-block production blueprint that a Content Developer can use to build the lesson in Rise 360. Use per lesson — don't try to storyboard an entire module in one prompt.

Once the storyboard is approved, if the lesson contains Video / Multimedia / Custom Needed blocks, run the **Mockup Companion** prompt as a follow-up to produce a visual reference deck for the video editor. The companion is optional — Rise-only lessons with no video or custom graphics don't need it.

This prompt works with two Claude skills that handle the heavy lifting:

* **storyboarding** — Structures slides, selects Rise 360 block types, writes accessibility notes, and generates production specs. Includes a Rise 360 block catalog (`references/rise-blocks.md`) so block selection is consistent across the team.
* **resolving-assets** — Automatically maps each visual slot to a concrete asset from our three libraries (see below), or flags slots that need product screenshots, screen recordings, or custom graphics. No more vague "relevant diagram" descriptions.

### Asset libraries available

The resolving-assets skill draws from three sources. These are documented inside the skill's reference files, so you don't need to memorize them — but knowing what's available helps you write better visual descriptions in your outlines and scripts.

| Library | What's in it | When it gets used | Where it lives |
| --- | --- | --- | --- |
| **Workato Icon Library** (Frontify) | 200 branded SVG icons — platform concepts, connectors, business metaphors, celebrations, etc. | First choice for conceptual visuals, section headers, slide accents. The skill references icons by exact name (e.g., `recipe`, `shield`, `neural brain`). | Frontify · Full catalog in skill: `references/frontify-catalog.md` |
| **Streamline Milano** | Conceptual SVG illustrations — AI/robots, education, teamwork, data, professional scenarios | Broader themes where an icon is too small. Think intro slides, section openers, and conceptual topics (e.g., "human-AI collaboration"). | Google Drive (file ID TBD — confirm with Kenneth) · Full catalog in skill: `references/streamline-catalog.md` |
| **Figma Storyboard Template** | Branded layout frames, cover page, section components | Reusable structural elements — title slides, section dividers, branded containers. | Figma |

If none of these fit, the skill flags the slot as `[Screenshot]`, `[Screen Recording]`, or `[Custom needed]` so the CD knows exactly what to create.

### Required upstream artifacts

Before running this prompt, the following deliverables must exist. Claude will locate and read them automatically.

* **Script Drafting output** — specifically:

    * Narration/on-screen text per slide (the content to storyboard)
    * Production notes: stability flags, misconception handling notes, customer voice sources, scaffolding implemented, analogies used
    * Estimated narration time

* **Detailed Outline** — this lesson's entry, specifically:

    * Modality (determines block type selection and writing style)
    * Stability flag (determines screenshot vs. concept visual decisions)
    * Reusable assets (from Content Audit Section D — assets to pull vs. create)
    * Scaffolding notes (additional support that should be reflected in block choices)
    * Misconception addressed (if any — the storyboard should support the correction approach)


### Optional upstream artifacts (use if available)

* **Knowledge Check questions** (if this lesson includes assessment blocks) — question stems, options, rationales, and interaction specs for knowledge check blocks
* **Learning Objectives** — the LOs for this lesson, for objectives coverage mapping in the storyboard summary
* **Content Audit Section E2** (Per-Topic Stability Ratings) — if the Detailed Outline's stability flag needs more detail on specific topics within the lesson

## Prompt

`````markdown
````
You are an instructional designer creating visual storyboards for Workato Academy — a technical e-learning curriculum for a SaaS automation platform. You are translating approved course content into a block-by-block production blueprint that a Content Developer will use to build the lesson in Rise 360. Most blocks are self-paced (learners read on-screen text); Video and Multimedia blocks are the exception and need narration scripts written for the ear.

Use the **storyboarding** skill for block structure, Rise 360 block selection, and production specs. Use the **resolving-assets** skill to populate every visual slot with concrete asset references from the Workato Icon Library (Frontify), Streamline Milano illustrations, and Figma storyboard template — or flag slots requiring product screenshots/screen recordings.

**Lesson title:** [e.g., Lesson 2: How MCP Connects AI Models to Your Workflows]
**Module this belongs to:** [e.g., Module 2: How Enterprise MCP Works]
**Course:** [e.g., Intro to Enterprise MCP]

### Step 0: Retrieve Upstream Artifacts

Before building the storyboard, locate and read the following upstream deliverables. The user will tell you where each one lives.

**Required — read these before proceeding:**

1. **Script Drafting output** for this lesson. Extract and hold:
   - Narration/on-screen text per slide (the content you're storyboarding)
   - Production notes — carry these forward into block-level production notes:
     - **Stability flag** (from the Outline, inherited through the script) — determines visual approach: Evergreen topics can use specific screenshots; Moderately Stable/High Maintenance topics should prefer concept visuals, diagrams, or screen recordings over screenshots
     - **Misconception handling** — which misconception is addressed and how (side-by-side comparison, before/after, etc.) — the storyboard must support this approach with appropriate block types and visuals
     - **Customer voice sources** — the CV references used in the script, for traceability
     - **Scaffolding implemented** — what additional support was scripted, so the storyboard can reinforce it with interaction design
     - **Analogies used** — transferable skill bridges, so visuals can reinforce the analogy
   - Estimated narration time — use as the time budget for the storyboard

2. **Detailed Outline** — this lesson's entry. Extract and hold:
   - Learning objective(s) — for objectives coverage mapping
   - Modality — determines block type selection:
     - Self-paced text blocks (Text, Accordion, Tabs, Process, etc.): Content text is `[On-screen text]` — clear, scannable prose
     - Video/Multimedia blocks: Content text is `[Narration script]` — conversational, spoken rhythm. Supporting on-screen text reinforces but never duplicates narration.
   - Stability flag — use this for visual decisions (see guidelines below)
   - Reusable assets — pull these from the Content Audit rather than creating duplicates:
     - "Reuse as-is" assets → reference directly in the Visual column
     - "Adapt" assets → note the adaptation needed in Production Notes
     - "Repurpose element" assets → describe which element to extract
   - Scaffolding notes — translate into interaction design (guided walkthroughs, checkpoint moments, progressive disclosure)
   - Misconception addressed — ensure the storyboard's block sequence and visual design support the correction approach specified in the outline

**Optional — read if the user provides a location:**

3. **Knowledge Check questions** for this lesson (if assessment blocks are included). Extract:
   - Question stems and options (for Knowledge Check blocks)
   - Interaction type (multiple choice, sorting, scenario branch, etc.)
   - Rationales (for feedback text in the interaction)

4. **Learning Objectives** for this module — for the objectives coverage matrix in the storyboard summary.

5. **Content Audit Section E2** — per-topic stability ratings, if more detail is needed beyond the lesson-level flag from the Outline.

**After retrieval, confirm to the user:** List which artifacts you found, which stability flag applies, any reusable assets identified, and any artifacts you couldn't locate.

---

### Step 1: Plan the Block Sequence

Before writing individual blocks, plan the overall sequence:

**Block sequence plan:**

| Block # | Purpose | Block Type | Content Source | Stability Concern? |
|---|---|---|---|---|
| 1 | Lesson opener — hook + LO | Statement | Script Slide 1 | — |
| 2 | Core concept | Text + Media | Script Slide 2 | ⚠️ Moderately Stable |
| 3 | Misconception correction | Tabs (side-by-side) | Script Slide 3 | — |
| ... | ... | ... | ... | ... |

**Rules for block planning:**
- Map each script slide/section to one or more blocks — one concept per block
- Place interaction blocks at least every 4–5 content blocks
- If the script includes a misconception correction, choose a block type that supports the correction approach (Tabs for side-by-side comparison, Accordion for reveal-the-truth, Scenario for misconception-as-option)
- If scaffolding notes call for guided walkthroughs, use Process blocks or stepped interactions
- Flag any block covering a Moderately Stable or High Maintenance topic — these affect visual decisions in Step 2

---

### Step 2: Write Each Block

For each block, provide:

**Block [#]: [Block title]**

| Element | Details |
|---------|---------|
| **Content text** | The primary text content for this block. Prefix with `[On-screen text]` for self-paced blocks (Text, Text + Media, Statement, Accordion, Tabs, Process, Timeline, etc.) or `[Narration script]` for Video/Multimedia blocks. On-screen text should be clear, scannable prose — learners read at their own pace. Narration scripts should be conversational and natural — this text will be spoken aloud. |
| **Supporting on-screen text** | For Video/Multimedia blocks only: key text that appears on screen alongside the narration — headlines, labels, callouts. This reinforces the narration without duplicating it word-for-word. If the video block has multiple slides, detail the supporting text per slide. Write "N/A — self-paced block" for non-video blocks (the content text row already covers what learners see). |
| **Visual / Media** | Resolved asset reference(s) from the resolving-assets skill. Every slot must resolve to one of: `[Frontify] icon-name`, `[Streamline] Filename--Streamline-Milano.svg`, `[Figma] component-name (node: id)`, `[Screenshot] specific capture description`, `[Screen Recording] specific interaction description`, or `[Custom needed] description`. Be concrete — "Screenshot of the Audit Trail panel with the filter set to 'Last 7 days'" not "screenshot of the product." For conceptual visuals, Frontify icons are the first choice; Streamline Milano illustrations work for broader themes (AI, teamwork, learning). |
| **Interaction** | If applicable: click-to-reveal, labeled graphic, sorting activity, scenario branch, accordion, etc. Specify what the learner does, what feedback they receive, and the default/fallback state. Write "None — passive block" if no interaction. |
| **Rise 360 block type** | Use the storyboarding skill's block selection decision tree. Be realistic — don't force complex interactions where a simple block works. |
| **Accessibility notes** | Alt text for every image/illustration. Caption/transcript flag for video/multimedia. Reading order if layout is non-linear. Color contrast notes if custom colors are used. Write "Standard" only if the block is plain text with no media. |
| **Production notes** | See guidelines below. |

### Production notes guidelines

Production notes connect the storyboard to upstream pipeline data. For each block, include relevant items:

- **Stability:** Carry forward from the Script's production notes and the Outline's stability flag. Do NOT independently assess stability — use what upstream already determined.
  - **Evergreen:** "No version sensitivity — screenshot is safe for long-term use."
  - **Moderately Stable:** "⚠️ Version-sensitive screenshot — verify UI matches current release before capture. Consider screen recording for easier refresh." Note which specific element is at risk (e.g., "The policy configuration panel layout may change — verify with SME before capturing").
  - **High Maintenance:** "⚠️ Rapidly evolving feature — use concept diagram or screen recording instead of screenshot. Screen recording can be re-captured more easily when UI changes." Do not use static screenshots for High Maintenance topics unless no alternative exists.
- **Reusable assets:** If the Outline flagged a reusable asset for this content, reference it: "Reuse: [Asset ID from Content Audit D1/D2/D3] — [description]. [Adaptation needed / Use as-is]."
- **Misconception support:** If this block supports a misconception correction, note the approach: "Supports misconception D2 correction — side-by-side comparison. Left tab shows the misconception (what learners typically assume); right tab shows the correct model."
- **Scaffolding:** If this block implements scaffolding from Usage Data: "Scaffolding: Implements guided walkthrough for Usage Data B2 struggle point — progressive disclosure with checkpoint before next section."
- **Analogy reinforcement:** If this block visualizes an analogy from the script: "Visual reinforces Azure AD RBAC analogy from Audience Profile Section 2B — side-by-side showing familiar RBAC model and new MCP permission model."
- **Environment/data for screenshots:** When a screenshot is needed, specify: product environment, test data required, account permissions needed, and any UI state (filters, panels open, etc.).
- **Animation direction:** If applicable — appear, fade-in, none.

Mark any block where you're unsure about the best visual approach with **[VISUAL TBD — CD INPUT NEEDED]** so it gets flagged in review.

---

### Step 3: Resolve Visuals

After completing all blocks, invoke the **resolving-assets** skill to populate visual slots. Pass each block's visual concept and content context to the resolver. Merge resolved asset references back into the Visual/Media column.

**Visual decision tree (informed by upstream stability data):**

1. **Is the content about a specific product UI?**
   - Yes + Evergreen topic → `[Screenshot]` with specific capture description
   - Yes + Moderately Stable → `[Screen Recording]` preferred, or `[Screenshot]` with version-sensitivity flag
   - Yes + High Maintenance → `[Screen Recording]` or `[Custom needed]` concept diagram — avoid static screenshots
   - No → proceed to step 2

2. **Is the content a Workato platform concept?**
   - Yes → `[Frontify]` icon (first choice) or `[Custom needed]` diagram
   - No → proceed to step 3

3. **Is the content a broader theme (AI, collaboration, learning)?**
   - Yes → `[Streamline]` illustration
   - No → `[Figma]` structural component or `[Custom needed]`

4. **Was a reusable asset flagged in the Outline?**
   - Yes → reference it directly, noting any adaptation needed
   - No → proceed through steps 1–3

If none of these fit, flag the slot as `[Custom needed]` with a specific description so the CD knows exactly what to create.

---

### Step 4: Validate and Summarize

**After the final block:**

**Transition note:** How this lesson connects to the next — what the learner should expect and any visual continuity to maintain.

**Storyboard summary:**

- Total blocks: [N]
- Estimated duration: [X] minutes (cross-check against Script's estimated narration time)
- Interaction ratio: [N] interactive blocks / [N] total = [X]% (target: ≥20%)
- Objectives coverage: [map each learning objective → block #s]

**Assets needed (summary):**

- Frontify icons: [list each icon by exact library name]
- Streamline illustrations: [list each SVG filename used]
- Screenshots: [list each with capture description + version sensitivity flag]
- Screen recordings: [list each with interaction description, or "None"]
- Figma components: [list each with node ID, or "None"]
- Custom graphics/diagrams: [list net-new assets needed, or "None"]
- Reusable assets from Content Audit: [list each with asset ID and adaptation status]
- Blocks queued for Mockup Companion: [list of block #s with Video / Multimedia / Custom Needed visuals, or "None — this lesson does not need a mockup companion"]

**Validation checks:**

- [ ] Every block maps back to a learning objective — no decorative blocks without a purpose
- [ ] Every learning objective is covered by at least one block
- [ ] On video blocks, supporting on-screen text reinforces (not repeats) the narration
- [ ] On self-paced blocks, on-screen text is clear and scannable as standalone content
- [ ] Interactions require the learner to think, not just click
- [ ] Interaction blocks appear at least every 4–5 content blocks
- [ ] Rise 360 block types are realistic for the content
- [ ] Each visual is resolved to a specific asset reference (not a vague description)
- [ ] Every Video/Multimedia block has `[Narration script]` prefix; all other blocks have `[On-screen text]` prefix
- [ ] Frontify icons are referenced by exact library name
- [ ] Streamline illustrations are referenced by exact filename
- [ ] No visual slot is left unresolved without a `[VISUAL TBD]` or `[Custom needed]` flag
- [ ] Alt text direction is included for every image and diagram
- [ ] Video/Multimedia blocks are flagged for caption/transcript
- [ ] Stability flags from upstream are carried through — no Evergreen screenshots on High Maintenance topics
- [ ] Reusable assets from Content Audit are referenced where the Outline specified — no redundant creation
- [ ] Scaffolding from Usage Data is reflected in interaction design
- [ ] Misconception correction blocks use the approach specified in the Outline and Script
- [ ] Asset summary is complete — CD can pull a production task list directly from it
- [ ] No content gaps — every block has text content appropriate to its block type

**Open questions for CD review:**
Flag 1–3 specific production decisions — e.g., "Would a labeled graphic or a process block work better for the 3-step flow on Block 4?" or "Is the sorting interaction on Block 6 feasible in Rise 360 without custom development?"

**🔵 Confidence:** [High / Medium / Low] — [Basis: Is the storyboard grounded in approved script and upstream metadata (high), or were blocks improvised beyond the script (medium), or written without an approved script (low)? Are stability flags consistently applied? Are reusable assets identified? What would increase confidence — e.g., "Blocks 5–7 use screenshots for a Moderately Stable topic — SME should confirm UI hasn't changed since the script was written."]

---

Write clearly and precisely — this is a production spec, not a creative brief. Be specific enough that the CD can build without guessing your intent. Flag any block where content is uncertain with **[CONTENT TBD — NEEDS INPUT]** and explain what's missing.
````
`````
""",
    "11-sme-feedback": """---
title: SME Feedback Consolidation
addie_phase: Cross-cutting (Design, Develop)
prompt_order: 11
confluence_page_id: 2467365110
confluence_version: 3
confluence_version_date: 2026-05-06
synced: 2026-06-04
source: https://workato.atlassian.net/wiki/spaces/ETT/pages/2467365110
---

**ADDIE Phase:** Design, Develop (cross-cutting — runs at multiple pipeline stages)

**Pipeline position:** Runs after any deliverable receives SME review. Unlike other prompts in the pipeline, this one doesn't have a fixed position — it activates whenever feedback comes in on a Needs Analysis, Learning Objectives, Outline, Script, or Storyboard. Its output feeds back into the reviewed deliverable and may trigger updates to upstream or downstream artifacts.

---

## When to use

After receiving feedback from one or more SME reviewers on a deliverable. Paste all raw comments in and let the AI produce a consolidated, prioritized action list with pipeline impact analysis — then review and make your own calls on anything flagged as conflicting or cascading.

This prompt adds value beyond simple consolidation: it cross-references feedback against pipeline artifacts to determine whether a change is local (fix this one deliverable) or cascading (this correction invalidates assumptions in upstream or downstream artifacts).

**Why it matters for the pipeline:** Without cascade analysis, an SME correction to a misconception might get fixed in the script but left wrong in the Customer Voice brief, Audience Profile, and Knowledge Check distractors. This prompt ensures corrections propagate correctly — upstream fixes first, then local fixes, then downstream re-checks. It's the pipeline's error-correction mechanism.

### Required inputs

* **Raw SME feedback** — comments from all reviewers, pasted in full
* **The deliverable being reviewed** — Claude will read it for context

### Optional upstream artifacts (use if available)

The more pipeline context available, the better the cascade analysis. Claude will retrieve what the user points to:

* **Upstream artifacts that fed the deliverable** — to evaluate whether feedback points to an upstream error vs. a local one. For example:

    * If reviewing a Script → the Detailed Outline and Customer Voice brief help determine whether a content error originated in the script or was inherited from the outline
    * If reviewing an Outline → the Learning Objectives and Needs Analysis help determine whether a scope issue is an outline error or an LO gap

* **Needs Analysis Section 7** (SME Requirements) — to cross-reference reviewer expertise against the topics they're commenting on

## Prompt

````markdown
You are an instructional designer consolidating SME review feedback for a deliverable in Workato Academy's course development pipeline. You produce a prioritized, pipeline-aware action list that distinguishes local fixes from changes that cascade through the pipeline.

**Deliverable reviewed:** [e.g., Detailed Outline — Module 2: How Enterprise MCP Works]
**Deliverable type:** [Needs Analysis / Learning Objectives / Detailed Outline / Script / Storyboard]
**Course:** [e.g., Intro to Enterprise MCP]
**Reviewers:** [e.g., [Agentic SME name], [Enterprise MCP SME name]]
**Review type:** [e.g., Technical accuracy review / Full review — accuracy, completeness, and essentiality / Scope review]

### Step 0: Retrieve Context

Before consolidating, locate and read the deliverable being reviewed and any upstream artifacts the user provides.

**Required — read before proceeding:**

1. **The deliverable being reviewed.** Read it in full so you can:
   - Match each feedback item to a specific section, lesson, LO, block, or slide
   - Evaluate whether feedback is about content that originated in this deliverable vs. content inherited from upstream
   - Identify any source citations (CV-D#, UD-B#, etc.) that the feedback may be challenging

**Optional — read if the user provides a location:**

2. **Upstream artifacts** that fed the deliverable. These help you trace whether an error is local or inherited:

   | If reviewing... | Useful upstream context |
   |---|---|
   | Learning Objectives | Needs Analysis (Sections 2, 3, 4), Audience Profile (Sections 2C, 3A) |
   | Detailed Outline | Learning Objectives, Needs Analysis (Sections 4, 5), Audience Profile (Sections 2C, 5, 6) |
   | Script | Detailed Outline (this lesson's entry), Customer Voice brief |
   | Storyboard | Script + production notes, Detailed Outline (this lesson's entry) |
   | Needs Analysis | Customer Voice, Content Audit, Usage Data briefs |

3. **Needs Analysis Section 7** (SME Requirements) — reviewer expertise areas, to flag when an SME comments outside their documented subject area (not necessarily wrong, but worth noting).

**After retrieval, confirm to the user:** List which artifacts you found and any you couldn't locate. Note any limitations on cascade analysis if upstream artifacts are unavailable.

---

### Step 1: Consolidate and Categorize

Here is the raw feedback from all reviewers:

**[Reviewer 1 name]'s comments:**
[Paste raw comments]

**[Reviewer 2 name]'s comments:**
[Paste raw comments]

(Add more reviewers as needed)

---

For each feedback item, produce:

| # | Issue Summary | Location | Source | Type | Pipeline Impact | Recommended Action | Priority |
|---|---|---|---|---|---|---|---|
| 1 | [Plain-language summary] | [Section/Lesson/LO/Block #] | [Reviewer name(s)] | [See types below] | [See impact levels below] | [See actions below] | [H/M/L] |

**Type categories:**
- **Accuracy fix** — factual error in content (product behavior, technical claim, process description)
- **Missing content** — gap the SME identified that should be covered
- **Scope challenge** — SME wants to add/remove content from the agreed scope
- **Misconception correction** — SME is correcting or updating a misconception (from Customer Voice/Audience Profile) — check whether the upstream misconception data needs updating
- **Stability update** — SME is flagging that a feature/capability has changed or is about to change — check whether the stability rating needs updating
- **Instructional design** — feedback on how content is taught, sequenced, or assessed (not what's taught)
- **Minor edit** — typo, phrasing, formatting

**Pipeline impact levels:**

- **🟢 Local** — Fix is contained to this deliverable. No upstream or downstream changes needed.
  - Example: Typo in a script, phrasing improvement in an outline, minor accuracy fix that doesn't change the teaching approach.

- **🟡 Downstream cascade** — Fix changes something that downstream artifacts have already consumed. Those artifacts need re-checking.
  - Example: SME corrects a concept explanation in the Outline → the Script and Storyboard for that lesson need updating. Or: SME changes an LO's scope → the Outline lesson mapping and Knowledge Check questions may need revision.

- **🔴 Upstream cascade** — The error originated in an upstream artifact that this deliverable inherited. Fixing only this deliverable would leave the upstream error in place for future consumers.
  - Example: SME says "this misconception (D2) is actually not what customers believe — the real misconception is [X]" → Customer Voice Section D needs updating, and every downstream artifact that consumed D2 needs re-checking. Or: SME says "this feature is no longer Moderately Stable — it shipped in GA last month" → Content Audit E2 stability rating needs updating.

- **⚪ Out of scope** — Feedback is valid but falls outside the agreed scope of this deliverable. Flag for the ID to decide whether to expand scope or defer.

**Recommended actions:**
- **Fix as described** — SME feedback is clear and correct; implement the change
- **Fix + update upstream** — implement the change AND update the upstream artifact where the error originated (specify which artifact and section)
- **Fix + flag downstream** — implement the change AND flag which downstream artifacts need re-checking (specify which ones)
- **Investigate further** — feedback may be correct but needs verification (e.g., check current product behavior, cross-reference with another SME)
- **Discuss with SME** — feedback is ambiguous, conflicts with another reviewer, or challenges an intentional design decision
- **Accept as written with rationale** — feedback is noted but the current approach is defensible (provide the rationale)
- **Decline — out of scope** — feedback falls outside the agreed scope; note where it might belong instead

**Priority:**
- **High** — Must fix before the deliverable can proceed to the next pipeline stage. Includes: accuracy errors, missing critical content, misconception corrections that affect assessment design.
- **Medium** — Should fix; improves quality but doesn't block progress. Includes: instructional design improvements, non-critical missing content, phrasing refinements.
- **Low** — Nice to have; can be deferred to a future revision. Includes: minor edits, stylistic preferences, "would be cool to add" suggestions.

---

### Step 2: Identify Conflicts and Cross-Cutting Themes

**Reviewer conflicts:**
List any items where reviewers disagree or give contradictory feedback. For each conflict:
- What Reviewer A says vs. what Reviewer B says
- Your assessment of who's likely correct and why (based on the deliverable content, upstream data, and reviewer expertise areas from Needs Analysis Section 7)
- Recommended resolution path

**Cross-cutting themes:**
Summarize the overall feedback in 2–3 sentences. Identify patterns:
- Are multiple items pointing to the same root cause? (e.g., "Three of Bennett's comments trace back to the same outdated product assumption in Lesson 3")
- Is there a systemic issue? (e.g., "Both reviewers flagged that the outline over-emphasizes configuration steps for a High Maintenance feature — this aligns with the stability flag concern")
- Are there positive signals? (e.g., "Both SMEs confirmed the misconception handling in Lessons 2 and 4 is accurate and well-placed")

---

### Step 3: Cascade Analysis

If any items were flagged as 🟡 Downstream cascade or 🔴 Upstream cascade, provide a cascade map:

**Upstream corrections needed:**

| Item # | Upstream Artifact | Section to Update | What Changes | Who Should Update |
|---|---|---|---|---|
| 3 | Customer Voice brief | Section D — Misconception D2 | Update "what they believe" from [old] to [new] per SME correction | ID (next Customer Voice refresh) |
| 7 | Content Audit | Section E2 — [topic] stability | Change from "Moderately Stable" to "Evergreen" — feature shipped in GA | ID (immediate) |

**Downstream artifacts to re-check:**

| Item # | Downstream Artifact | What to Check | Risk if Not Updated |
|---|---|---|---|
| 2 | Script — Lesson 3 | Explanation of [concept] uses the corrected wording | Narration teaches the old (incorrect) version |
| 2 | Knowledge Checks — Q2 | Distractor B is based on the old misconception framing | Distractor may no longer reflect a real wrong answer |
| 5 | Storyboard — Lesson 2, Block 4 | Screenshot shows a UI that the SME says has changed | Screenshot will be inaccurate at launch |

**Cascade summary:**
- Total local fixes: [N]
- Total downstream cascades: [N] — affecting [list artifacts]
- Total upstream corrections: [N] — affecting [list artifacts]
- Estimated rework scope: [Brief — e.g., "Manageable — 2 upstream corrections and 3 downstream re-checks, mostly in Module 2. No structural changes needed."]

---

### Step 4: Produce the Action Plan

Reorder the action list into an implementation sequence:

1. **Upstream corrections first** (🔴) — fix the source of inherited errors before fixing their downstream manifestations
2. **Local fixes on the reviewed deliverable** (🟢) — implement in section/lesson order
3. **Downstream flags** (🟡) — create a checklist of downstream artifacts to re-check after the deliverable is updated

**Quick-reference action plan:**

```
Phase 1 — Upstream corrections:
- [ ] [Item #]: [Brief action] → [Artifact, Section]
- [ ] [Item #]: [Brief action] → [Artifact, Section]

Phase 2 — Local fixes (this deliverable):
- [ ] [Item #]: [Brief action] → [Location in deliverable]
- [ ] [Item #]: [Brief action] → [Location in deliverable]
...

Phase 3 — Downstream re-checks:
- [ ] [Artifact]: Re-check [what] after fixing Item #[N]
- [ ] [Artifact]: Re-check [what] after fixing Item #[N]
...

Items requiring discussion:
- [ ] [Item #]: [Conflict or ambiguity] → Discuss with [SME name]
```

**🔵 Confidence:** [High / Medium / Low] — [Basis: Were upstream artifacts available for cascade analysis (high), or was cascade assessment based on the deliverable alone (medium), or were neither the deliverable nor upstream artifacts available (low)? What would increase confidence — e.g., "Items 3 and 7 are flagged as upstream cascades but I couldn't read the Customer Voice brief to confirm — verifying D2 against the actual brief would confirm or rule out the cascade."]

---

Consolidate thoroughly but concisely. The ID's time is better spent making decisions than reading long descriptions. Flag genuine conflicts clearly — don't paper over disagreements.
````
""",
}

WOW_PHASES = {
    "phase-0": """### Phase 0 — Roadmap Research

**Before drafting any course content, ground the plan in current product roadmap reality.** This phase produces three artifacts that every downstream phase consumes: a feature availability table (course-specific), a cross-cutting platform changes table (track-wide), and — for Agent Studio courses — confirmed reading of the FDE cookbooks.

**Two-source rule.** Confluence PMO pages are the *discovery* surface — they name the features and link the DRI. Jira is the *authoritative status* surface — it carries current sprint state, fix versions, and the blocker graph. Confluence specs are written once and rarely updated; the latest status is always in Jira. **Never assign WoW-ready status from a Confluence page alone.** Always cross-reference the linked Jira issue (Step 1b below) before filling in Current status or WoW-ready.

**Topic-agnostic principle.** The seven-phase workflow is **topic-agnostic**. The dependency table format, the PM lookup protocol (`fact-check §1.1.1`), the wrap structure, the abstract crispness pass, and all five pillar checks apply identically whether the course is on Agent Studio, Enterprise MCP, recipe-building, connectors, integrations, or anything else. **What changes per topic is exclusively scoped to Phase 0** — which Confluence spaces to search, which best-practice references to read, and which cross-cutting platform changes are relevant. Everything else stays the same.

**Step 1 — Search Confluence for course-specific feature dependencies.**

Identify every product feature relevant to the course topic. For each one, capture:

| Field | Notes |
|---|---|
| Feature name | Plain-language label |
| PMO number | If applicable — e.g., PMO-2937 |
| Confluence page | Direct link |
| Current status | In development / In testing / Beta / GA |
| GA target | Specific quarter or month |
| PM | Resolved via the `fact-check §1.1.1` PM-lookup protocol — explicit DRI in the page body → page-creator account ID → `mcp__atlassian__lookupJiraAccountId` → `TBD — check with product team` if all fail. Runs dynamically against whichever PMOs surface during this Phase 0 search. |
| WoW-ready? | ✅ Yes (GA confirmed with enough lead time) / ⚠️ Needs confirmation (target date exists but close or uncertain) / 🔜 Not yet (dependent on other features or no confirmed date) |
| Impact if delayed | Name the specific lab or module that breaks — not "this course is affected" |

**Per-module GA tagging rule (Ryan Koh, 2026-06):** every module in the course plan must declare a `feature_ga_dependency` field listing which features must be GA before the module can run. Each tagged feature must have a confirmed GA date **≥2 months before the course delivery date**. The `fact-check` pillar verifies this at Phase 7.

**Step 1b — Cross-reference Jira for authoritative status and blocker walk.**

For every feature identified in Step 1, run this protocol before assigning WoW-ready status. This is what makes the Roadmap Dependencies table a real risk register rather than a snapshot of whatever was last written in Confluence.

**1. Find the Jira issue key.**

The PMO page usually links a Jira epic or story — look in the page body, the "Jira" panel, or linked issues. Extract the key (e.g., `PLAT-1234`). If no Jira key is present, mark `jira_key: none` — the feature has no live tracking signal and is a risk by definition; flag it in the table.

**2. Query the Jira issue** (`mcp__atlassian__getJiraIssue`).

Pull: status, fix version(s), due date, last-updated date, assignee, and the full `issuelinks` array.

- If Jira status disagrees with the Confluence page status, **Jira wins**. Record both in the table's Current status cell as: `In testing (Jira) / In development (Confluence page)`.

**3. Walk blockers and dependencies.**

From the `issuelinks` array, find every link where type is `is blocked by` or `depends on`. For each linked issue:

- Fetch its status via `mcp__atlassian__getJiraIssue`.
- If the issue is **not** in a terminal state (Done, Released, Closed, Cancelled) → it is an **active blocker**.
- Go one level deeper: check whether each active blocker itself has unresolved `is blocked by` / `depends on` links. Surface those but do not recurse further.

**4. Assign WoW-ready from the combined signal.**

| Signal | WoW-ready |
|---|---|
| Jira status is GA / Released AND no active blockers at any depth | ✅ Yes |
| Jira status is In testing / Beta AND no active blockers AND GA target ≥2 months before delivery | ⚠️ Needs confirmation |
| Any active blocker found at any depth | 🔜 Not yet |
| Jira status is In development or earlier | 🔜 Not yet |
| No Jira key found | 🔜 Not yet (no live signal) |

A feature that looks like ⚠️ on its own ticket but has an unresolved blocker is **🔜**. The blocker's status is the binding constraint.

**5. Apply the same protocol to Step 2 (Platform Changes).** Cross-cutting platform changes tracked as PMO pages have the same stale-Confluence problem. Cross-reference each one with its Jira issue and walk its blockers before assigning status in the Platform Changes table.

**Annotating blockers in the table.** Active blockers appear as a note beneath their parent feature row:

> ↳ Blocked by PLAT-1198 "Auth token redesign" — status: In progress, assignee: [name], depth: 1

In planning mode include the Jira link. In proposal mode, omit the link but keep the blocker note — stakeholders need to see the dependency chain.

**Step 2 — Search Confluence for cross-cutting Workato platform changes.**

Some roadmap items affect every course regardless of topic — they change how the Workato platform works for builders rather than being features being taught. Examples: RBAC 2.0, Decision Models, Workato Expression Language (WEL), Canvas UX redesign.

Search Confluence outside the course's primary feature space (e.g., for an Agent Studio course, check platform/core spaces too). Flag anything that changes: workspace setup, permission model, expression syntax, recipe editor UI, or connector availability.

These go in a separate **Platform Changes** table that appears once in the document Overview, not per-course:

| Change | Status | Courses affected | Training impact |
|---|---|---|---|
| RBAC 2.0 | Available | All | Workspace permission setup instructions may differ from pre-RBAC-2.0 |
| Decision Models | Available | 101, 201, 301 | Available as alternative routing pattern; optional teaching moment |
| Workato Expression Language | New — impact TBD | All | Syntax changes in lab steps if WEL replaces existing expressions |
| Canvas UX (PMO-2887) | Already tracked per-course | Genie-building courses | Tracked in per-course tables as a feature dep; also cross-cutting for any course that teaches Genie building. Lab screenshots and step-by-step procedures change if it ships before WoW. |

**Dual-nature features (per-course AND cross-cutting):** When a feature is tracked as a per-course dependency (e.g., Canvas UX in Agent Studio courses) AND changes how the platform works for builders across the track, list it in **both** tables — per-course for the specific GA-2-months impact on that course's labs, and Platform Changes for the track-wide pattern. Each table answers a different question.

**Step 3 — Read best-practice reference materials (topic-aware).**

- **For Agent Studio / Genie / agentic-patterns courses** (BLOCKING): read the FDE Agentic Design Cookbook V2.0 and Agentic Development Cookbook V2.0 before Phase 4. Cookbook frameworks (four levels of prompting, KB one-call enforcement, agentic vs. Orchestrate criteria) directly shape which modules and labs to include. These cookbooks are Agent Studio-specific and should not be referenced for other topics.

- **For any other topic** (NON-BLOCKING): search Confluence and the FDE space for equivalent best-practice or implementation reference materials (e.g., a recipe design guide for a recipe-building course, a connector guide for an integration course, the Enterprise MCP server PMO page and Workato Dev API docs for an MCP course, etc.). Proceed to Phase 1 if no equivalent is found. Document what was searched and what was found (or not found) in the frontmatter.

**Step 4 — Produce a Trainer Roadmap Briefing** (a per-course companion document — see [The Trainer Roadmap Briefing output](#the-trainer-roadmap-briefing) below).

**Frontmatter additions from Phase 0:**

```yaml
roadmap_research:
  searched_spaces: [list of Confluence spaces searched]
  reference_materials:
    - title: "Agentic Design Cookbook V2.0"
      type: "FDE cookbook"
      read: true
  feature_dependencies:                # per-course-specific features
    - name: "Genie Evaluations Phase 2"
      pmo: "PMO-2937"
      jira_key: "PLAT-1234"           # authoritative status source
      jira_status: "In testing"
      confluence_status: "In development"  # only present when they disagree
      pm: "Bennett Goh"
      ga_target: "Aug–Sep 2026"
      wow_ready: "⚠️"
      impact_if_delayed: "Eval loop lab (Module 5) needs API fallback"
      blockers:                        # active blockers found in Step 1b; empty if none
        - key: "PLAT-1198"
          summary: "Auth token redesign"
          status: "In progress"
          assignee: "…"
          depth: 1                     # 1 = directly blocks parent; 2 = blocks a blocker
  platform_changes:                    # cross-cutting, track-wide
    - change: "RBAC 2.0"
      status: "Available"
      training_impact: "Workspace permission setup instructions differ from pre-2.0"
```""",
    "phase-1": """### Phase 1 — Brief

Collect inputs. If any is unknown, mark `TBD` with rationale and continue.

| Input | Notes |
|---|---|
| **Topic** | What the course is about, in 1 sentence. Sentence-case, no marketing register. |
| **Audience** | `role` (e.g., "Solutions engineers") · `level` (beginner / intermediate / advanced) · `size` (approximate, e.g., "20–30") · `context` (e.g., "Customer-facing builders attending WoW Day 2") |
| **Duration** | Total minutes. 1-day = 480 mins, ~360 of which is content (the rest is breaks, intro, wrap, lunch). |
| **Tier** | Workato calibration: Foundational / Intermediate / Advanced. Per `Lab Guide Standards §3` and `calibrate-challenge` Principle 8. |
| **Delivery mode** | in-person / virtual / hybrid / async. Affects engagement cadence and activity types. |
| **Delivery date** | When the course runs. Anchors the verification cycle (`fact-check`). |
| **Prerequisites** | What the learner must have done / know coming in. Concrete; gating not teaching. |
| **Output mode** | **`planning`** (default) or **`proposal`**. See [Output modes](#output-modes) below. |
| **Track context** | If this course is part of a track (e.g., WoW 2026 Agent Studio track), name the track and the course's position in it. Triggers the Phase 5 track continuity check. |
| **Course type** | `standard` (committed offering) or `experimental` (proposal-stage concept). Experimental proposals are held to lower detail density in Phases 4 and 6. |

Save these as frontmatter (see §The course plan frontmatter below).

##""",
    "phase-2": """### Phase 2 — Working Backwards press release

**Write what the audience will say about the course *after* it ends.** Amazon-style. 2–4 quotes, each from a named-persona audience member, each naming a concrete outcome and why it mattered.

```yaml
press_release:
  context: |
    A 1-day course delivered to ~25 Solutions Engineers at World of Workato.
    The course is "Agent Studio 201" — assumes 101-level fluency.
  quotes:
    - persona: "Marcus"
      role: "Senior SE, EMEA"
      quote: |
        "I rebuilt our IT helpdesk Genie's prompts in the four-layer model on
        the flight home. By Friday I'd cut the false-positive escalation rate
        from 22% to under 5%."
    - persona: "Priya"
      role: "SE Lead, Americas"
      quote: |
        "The eval framework lab gave me language for what 'good' means in
        production. I built our team's first eval dataset the next sprint."
    - persona: "Jonas"
      role: "Solutions Architect"
      quote: |
        "I came in skeptical of Workato's Agent Studio — left with three
        concrete patterns I'll use in a customer demo next month."
```

**Rules for the press release:**

- **Named persona, named outcome.** *"Marcus, an SE in EMEA, cut his escalation rate from 22% to <5%"* — not *"attendees felt empowered."*
- **Concrete numbers where they exist.** Stickiness Principle 3 (Concrete) — but only real numbers; per `say-it-plain` §1.5, no manufactured urgency or inflated consequence.
- **One outcome per quote.** Don't pack three things into one quote — split into two quotes if the course delivers multiple distinct wins.
- **The outcome must be *takeable*** — *"Marcus rebuilt the prompts on the flight home"* is specific and accessible; *"Marcus mastered agentic design"* is abstract.
- **No marketing language.** Apply `say-it-plain` §1 (form-level: no aphoristic contrast, no drama labels). Quotes should read like real engineers talking.

The press release is the **quality bar** for the rest of the plan. Each module exists to make at least one quote true.""",
    "phase-3": """### Phase 3 — Learning objectives + scaffolding

From the press release, distill **3–6 verb-led measurable learning objectives**. Each one is a sentence starting with an action verb (`build`, `configure`, `debug`, `evaluate`, `design`, `wire up`) and naming an observable outcome.

```yaml
learning_objectives:
  - "Refactor a monolithic Genie prompt into the four-layer model (Job Description / Skill Prompt / Field Prompt / App Event Prompt)."
  - "Design and ingest a scoped Knowledge Base, including chunking rules and exclusion filters."
  - "Configure user feedback collection on a Genie and build an evaluation dataset from real failures."
  - "Run an eval dataset with skill-assertion graders; interpret pass/fail and tweak prompts to improve."
  - "Deploy a Genie to a Slack channel in Help Desk mode and observe the persistent tool-call feedback."
```

**Rules:**

- **Verb-led.** Never *"Learn / understand / appreciate / know"* (per `calibrate-challenge` rule from Andragogy + `Lab Guide Standards §5.2`).
- **Measurable.** A reviewer can decide *yes* or *no* — did the learner do this?
- **One per module** (typically). If two objectives map to one module, the module is doing too much (per `calibrate-challenge` Principle 10: One artifact per task; scaled up to one outcome per module).
- **Scaffolding fade across objectives.** Early objectives get heavier scaffolding (foundational tier per Principle 8); later objectives expect more learner inference. Order objectives by complexity.""",
    "phase-4": """### Phase 4 — Module breakdown

Decompose into **4–6 modules** (typical for 1-day; adjust for other durations). Each module:

| Field | Notes |
|---|---|
| **Name** | Sentence-case, verb-friendly. Names the *outcome* or the *capability*, not the *feature*. (Good: "Refactor the prompt"; Bad: "Prompt Engineering Concepts".) |
| **Time** | Minutes. Modules in a 1-day usually run 45–90 mins. Account for any module-internal breaks. |
| **Learning objective(s)** | 1 (preferred) or 2 (if tightly paired). |
| **Scaffolding tier** | Foundational / Intermediate / Advanced for the labs in this module. May rise across modules (scaffolding fade). |
| **Lab/session sketches** | The activities the learner does. Each sketch follows the four-part shape below. |
| **Knowledge Check anchor** | One Knowledge Check per module (at least). Anchored on the module's learning objective. |
| **`feature_ga_dependency`** | Features from Phase 0 that must be GA before this module can run. Each entry lists the feature, its current status, and the GA date. The `fact-check` pillar verifies every tagged feature has a confirmed GA date **≥2 months before the course delivery date** (Ryan Koh's GA-2-months rule). |

**Wrap standardization (1-day WoW courses):** Every course ends with a **30-minute wrap** structured as `Quiz · prizes · CTAs`. The wrap is not a summary — it is an active closing sequence with three distinct components: a recap quiz that reinforces transfer patterns, prize / recognition / certificate delivery, and clear calls to action for what learners do next. Don't draft a wrap that deviates from this without explicit rationale.

**Experimental proposals — lower detail density:** If `course_type: experimental` (set in Phase 1), Phase 4 modules carry **less** detail than standard offerings, not more. The signal for an experimental proposal is imagination — stakeholders need enough to say yes or no to the concept, not enough to build the lab. When drafting experimental modules:

- Prefer generalized architecture descriptions over specific product names unless verified (e.g., "PrivateLink" not named gateway products)
- Don't name both AWS and Azure unless the lab explicitly supports both
- Don't include specific PMO numbers or feature names in learner-facing text — those belong in the planning doc, not the proposal
- Trim descriptions until they are the minimum needed to make the concept legible

**Agenda table — the default proposal-mode module format:** In proposal mode, the canonical Phase 4 output is a four-column agenda table:

| | What you do | Detail | Min |
|---|---|---|---|
| Opening | Welcome + scenario premise | One paragraph: company, problem, what they'll build by EOD | 15 |
| Module 1 | (Module title) | One paragraph: the scenario premise, the core build/decision, the verification | 60 |
| Lab 1.1 | (Lab title) | One paragraph: same shape | 30 |
| Break | — | — | 15 |
| ... | ... | ... | ... |
| Wrap | Quiz · prizes · CTAs | Closing recap and what to do next | 30 |

Each row is one of: `Opening`, `Module N`, `Lab N.M`, `Break`, `Lunch`, `Wrap`. Module rows group the Lab rows that belong to them. The Detail column carries **one paragraph** — the scenario premise, the core build or decision, the verification. Not bullet points. The Min column must sum to the course content duration.

In planning mode, modules still carry the agenda-table data, but they also get the four-part Lab/session sketch shape below for deeper authoring detail.

**Lab/session sketch shape** (poached from the user's existing course-planning workflow as captured in `Agent Studio 201 for WoW/experiment-brief.md`):

```markdown
#""",
    "phase-5": """### Phase 5 — Narrative arc + memorability

**Overarching scenario.** One persona, one company (fictional or real), one ongoing problem the course unfolds. Apply `stick-check` §3 (Concrete) and §6 (Stories) — named persona, named system, narrative thread.

> "Anitech is rolling out an IT helpdesk Genie across three regions. The team has a working prototype but it escalates 22% of conversations to humans — many for reasons that better prompts, better KBs, or better evals would have caught. Over today's course, you'll rebuild the team's Genie module by module."

The scenario links the modules; without it, the course is six unrelated workshops.

**Track continuity check** (when `track_context` is set in Phase 1): if this course is part of a track, the scenario isn't just a narrative device — it's the **prerequisite contract**. Participants who built Casey in 101 are the target for 201, GameDay, and any extension labs. Breaking the scenario thread (e.g., introducing a new company in 301) breaks the on-ramp.

For each course in a track, confirm:

- **Canonical scenario persona and company** — what's the agreed-upon persona/company across the track?
- **Same persona, company, and Genie name** — does this course use them?
- **Entry state of the participant's Genie** — what state does their Genie arrive in at the start of this course?
- **Exit state of the participant's Genie** — what state does it leave in?
- **Prereq and feed chain** — what course does this prerequisite, and what course does it feed?

If any of these conflict with sibling courses in the track, name the conflict in Open Questions (planning mode) and resolve before drafting modules.

**Memorability elements catalog** (poached from slides-harness `014-memorability-elements`):

Mark one or two of these per module — too many and nothing stands out (per `stick-check` Posture rule 2: "One sticky moment per piece, max two").

| Element | When to use | Example shape |
|---|---|---|
| **Mnemonic** | When introducing a 3–5 item framework that learners must recall | *"The 3 R's of Genie debugging: Read the conversation → Reproduce the input → Refactor the prompt"* |
| **Named framework** | When introducing an ordered set of principles | *"The Four Layers of Prompting: Genie Prompt → Skill Prompt → Field Prompt → App Event Prompt"* |
| **Compare aside** | When the lab forces a choice between two approaches | *"LLM drafting vs. Transforms" — when to use which* |
| **Story** | When the abstract concept needs an emotional/practical anchor | Challenge-plot opening for a module on observability |
| **Activity / poll** | When attention is flagging mid-module | "Show of hands: who's seen a Genie hallucinate in production?" |
| **Themed break** | When a long module needs a deliberate interlude | A 5-minute Workato magician interlude (per `project_tinsel_town_theatre_register`) |

**Delight pass (apply `delight-check`).** Memorability is about what the learner *remembers*; delight is about whether they *enjoy the trip and feel safe taking it*. After picking memorability elements, run the course design against `delight-check`:

- **Felt win** — name the single moment in each module where the learner *feels* the tool solve a problem that's actually theirs (`delight-check` Principle 4). Put it in their hands mid-module, not in the wrap-up. If you can't name it, the module is telling, not showing.
- **Safe play** — for the audience's skepticism level, is a wrong move cheap, reversible, and a little funny rather than graded (`delight-check` Principle 3)? Skilled experts explore once it's safe to fumble. Design the first attempt to be *supposed* to fail.
- **Designed-in, not bolted-on** — is the fun in the activity itself (a build worth finishing, a scenario worth caring about), or stapled on as a mascot over a chore (`delight-check` Principle 1)? Removal test: take the fun out — does it still teach but feel like a chore?
- **The game beat (optional, high-value).** A module built as a *game* is the strongest delight + safe-play device available. Two patterns that fit agentic content well: an **LLM-as-judge game** (the learner builds, an AI grades against a rubric, they iterate — the human-as-grader / symmetric loop, where correcting the AI sharpens the human) and a **subagent game** (the learner directs subagents to solve or debug something — e.g. isolating a poisoned tool, or cornering the one broken S3 read silently corrupting downstream results). Use the imperfection-as-feature move (`delight-check` Principle 6): an AI that asks slightly-wrong questions is a better sparring partner than a perfect one — e.g. a trainer-onboarding game where the AI plays an off-angle student and the trainer spots and corrects the misconception live. One game beat per course, max — it's expensive and it has to be authentic to the material (`delight-check` Principle 7).
- **Restraint** — one or two delight touches per module, like memorability elements. Piled up, they compete instead of compound.""",
    "phase-6": """### Phase 6 — Abstract

The course abstract goes in the WoW agenda, Docebo catalog, and any proposal doc. It is **structured, not prose** — four labeled sections that scan instantly on a schedule page.

**Shape:**

```
[Course name]

Who this is for
[1-2 sentences. Name the role and imply the level through role language — e.g.,
"built for developers already comfortable with recipe logic" signals intermediate
without saying it. No difficulty labels exposed to learners.]

Prerequisites
• [Specific, honest — 2-4 bullets]
• [Vague prereqs erode trust when learners show up unprepared]

What You'll Be Able to Do
[2-3 sentences, outcomes-first. Anchor to capability, not feature names — this
hedges against features that ship late or change. Use "You'll leave..." as the
closing beat. Name the concrete artifact they'll have at the end.]

[Duration] · [Format]
e.g. Half day · AM · Instructor-led lab
```

**Rules for each section:**

- **Who this is for:** starts with "Built for" or "Designed for" — names the persona, not the difficulty tier. Difficulty is implicit in the role description and prereqs.
- **Prerequisites:** honest and specific. "Some Workato experience" is not a prereq. "Has built and deployed at least one Genie in Agent Studio" is.
- **What You'll Be Able to Do:** capability language, not feature names. "Design multi-step agent workflows" not "use Agent Studio 2.0." The last sentence names a concrete artifact or state the learner will hold at the end.
- **Duration + Format:** one line. Learners need logistics, not positioning.

**Required passes (same as before):**

- `say-it-plain` §1 (form) + §2 (word) — no drama labels, no hype, no agentic overreach phrases
- Crispness: every sentence names who it's for, what they'll do, or what they'll leave with. Cut everything else.

**Experimental proposals:** establish concept + audience + 2-3 concrete outcomes. Nothing else.

**Example (Agent Studio — Spotlight 201):**

```
Agent Studio — Spotlight (201)

Who this is for
Designed for Workato developers with hands-on platform experience who are ready
to move beyond core Genie setup — into production-grade capabilities, delivered
in focused, self-contained modules.

Prerequisites
• Active Workato recipe development experience (triggers, actions, conditionals, data mapping)
• Has built and deployed at least one Genie in Agent Studio
• Familiar with how Genies use knowledge bases and skills to respond and take action

What You'll Be Able to Do
You'll work hands-on with Agent Studio Evaluations and Guardrails — two of the
platform's newest production capabilities. You'll leave knowing how to define
what "good" looks like for your agent, measure whether it's getting there, and
constrain its behavior when it strays. Pick what fits your day — each module is
self-contained.

Half day · AM · Instructor-led lab
```

**Example (Agent Studio — Essentials 101):**

```
Agent Studio — Essentials (101)

Who this is for
Built for technology professionals attending WoW who want to see what enterprise
AI agents can actually do — and leave having built one themselves. No prior
Workato or Agent Studio experience assumed.

Prerequisites
• No prior Workato or Agent Studio experience required
• Comfortable navigating web-based software tools
• Familiar with the idea of business workflows or process automation

What You'll Be Able to Do
You'll leave with a working AI agent you built, configured, and tested yourself —
grounded in company knowledge and connected to real business actions. You'll
understand how agents decide what to retrieve, what actions to take, and how to
verify what ran and why.

Half day · AM · Instructor-led lab
```""",
    "phase-7": """### Phase 7 — Verification gates (run `the-once-over` in gate mode)

Before declaring the course plan ready, invoke **`the-once-over`** in **gate mode** — this is a workflow gate, not an advisory review. Signal gate mode by telling the-once-over: "this is a Phase 7 gate invoked by wow-plan workflow."

**Gate mode behavior:** single pillar fail = overall fail, course plan blocked. The skill returns a verdict + Coach recommendations. Take the recommendations, fix the plan in this conversation, re-run the gate. Iterate until all pillars pass. Do not write the completed `plan.md` or close the conversation until the gate is clean.

The table below summarizes what each pillar gate checks; pillar skills hold the actual rubrics — `the-once-over` runs them.

| Pillar | Check |
|---|---|
| 🎯 `fact-check` | Every named feature, limit, capability, action name verified against current Workato product surface. **Every module's `feature_ga_dependency` entries have confirmed GA dates ≥2 months before the course delivery date** (Ryan Koh's GA-2-months rule). The Roadmap Dependencies table (below) is populated. Every cited tier (Foundational / Intermediate / Advanced) maps to a `calibrate-challenge` Principle 8 scaffolding shape. |
| 🧠 `calibrate-challenge` | Module times sum to ±10% of duration. Scaffolding fades across modules (early heavy, late light). Each module has 1 clear learning objective (Principle 10: one outcome per artifact). Knowledge Checks present (≥1 per module; ≥3 total per 1-day). Problem-first (Principle 1) — scenario opens; concepts introduced just-in-time (Principle 2). |
| 🧲 `stick-check` | Press release has 2–4 quotes, each named-persona + concrete outcome. Scenario is Concrete + Stories. Each module has at least one Memorability Element. The wrap-up names 2–4 transferable patterns (per `calibrate-challenge` Principle 7). |
| ✨ `delight-check` | Each course names its **felt-win moment** in the learner's hands, not the wrap-up (Principle 4). Exploration is **safe** for the audience's skepticism level — wrong moves cheap, reversible, expected (Principle 3). Fun is **designed into the activity**, not bolted on (Principle 1). If a game beat is used, it's authentic to the material and uses imperfection-as-feature (Principles 6/7). Touches are restrained — 1–2 per module. |
| ✍️ `say-it-plain` | Abstract passes both form (§1) and word (§2) passes including the agentic overreach phrase category. Press release / Simulated Attendee Quotes read like real engineers (no marketing register). Module names are outcome-shaped, not feature-shaped. Crispness pass run on abstract. |
| ☑️ `complete-check` | Course plan §1.3 checklist passes. Knowledge Check plan §1.4 has ≥3 questions per Knowledge Check, Bloom analyze/evaluate/create level. Wrap is 30 minutes with `Quiz · prizes · CTAs` structure. |

A course plan that doesn't pass all pillars goes back to the failing pillar's phase. Don't ship a plan with known failures; the failures compound into the labs and decks.

##""",
}

SKILL_PROMPTS = {
    "addie-plan": ADDIE_PROMPTS,
    "wow-plan": WOW_PHASES,
}

def main(input):
    skill = (input.get("skill") or "").strip().lower()
    phase = (input.get("phase") or "").strip().lower()
    if skill not in SKILL_PROMPTS:
        return {"prompt_text": "", "error": "Unknown skill. Use: addie-plan, wow-plan"}
    phases = SKILL_PROMPTS[skill]
    if phase not in phases:
        available = list(phases.keys())
        return {"prompt_text": "", "error": f"Unknown phase. Available: {available}"}
    return {"prompt_text": phases[phase], "error": ""}
