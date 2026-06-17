# standards-desk — Claude context

Standards Desk MCP server. Three tools: pillar discovery, rubric fetch, and static checker. The calling agent does LLM reasoning client-side using the rubrics; Workato handles the mechanical checks.

## MCP server prompt (injected at registration)

> **Before running any checks:**
>
> 1. Check memory for a saved `standards_desk_audience` value. If found, use it silently — do not ask again.
> 2. If not in memory, ask once:
>    > "Which role best describes you? (I'll remember this for future sessions)"
>    > - **Training** — workshop trainers, World of Workato, ILT
>    > - **Education** — Workato Academy, async e-learning, ETT
>    > - **Workato** — all other Workato employees (default)
> 3. Save the answer to memory as `standards_desk_audience` so it persists across sessions.
> 4. Use the value as the `audience` parameter on all tool calls. **Default is `workato` if unspecified or unknown.**

## Tools

### 1. `list_pillars(audience?: string)`
Returns metadata for all available pillars — names, descriptions, what each checks for. Pass `audience` to see which variants apply. Lightweight discovery, no artifact needed.

```
list_pillars(audience?: "training"|"education"|"workato"  // default: "workato")
→ [{ name, description, checks_for, has_variant: bool }]
```

### 2. `get_rubrics(pillars?: string[], audience?: string)`
Returns full rubric markdown for each requested pillar, scoped to the audience variant. Omit `pillars` to get all. The calling agent uses these for client-side LLM reasoning.

```
get_rubrics(pillars?: string[], audience?: "training"|"education"|"workato"  // default: "workato")
→ { pillar: rubric_markdown }
```

### 3. `run_static_checks(artifact: string, pillars?: string[], audience?: string)`
Runs mechanical static checks for the requested pillars using the audience-appropriate rule set. Omit `pillars` to run all applicable pillars for that audience.

```
run_static_checks(artifact: string, pillars?: string[], audience?: "training"|"education"|"workato"  // default: "workato")
→ { pillar: { findings: finding[], pass: bool } }
```

### Audience variants per pillar

| Pillar | training | education | workato |
|---|---|---|---|
| `say-it-plain` | Full rules + training carve-outs | Full rules + ETT carve-outs | Stripped (no internal carve-outs) |
| `fact-check` | Workshop focus (GA dates, FDE cookbooks, WoW delivery) | Course focus (Rise 360, async) | Not applicable |
| `calibrate-challenge` | ILT / workshop calibration | e-learning calibration | Not applicable |
| `team-style-guide` | Training team conventions | ETT conventions | Not applicable |
| `stick-check` | Universal | Universal | Universal |
| `delight-check` | Universal | Universal | Universal |

### Available pillars

| Name | What it checks |
|---|---|
| `say-it-plain` | Jargon, hype, marketing-speak |
| `fact-check` | Feature GA dates, product claims, PM attribution |
| `stick-check` | Stickiness principles, concrete examples, narrative |
| `calibrate-challenge` | Difficulty calibration, prerequisite assumptions |
| `delight-check` | Delight principles, engagement, game beats |
| `team-style-guide` | Workato training team style conventions |

## Typical agent flow

```
1. Ask user for role → "training" | "education" | "workato"
2. list_pillars(audience)                                    → discover applicable pillars
3. get_rubrics(["say-it-plain", "fact-check"], audience)    → fetch audience-scoped rubrics
4. run_static_checks(artifact, [...], audience)             → audience-appropriate findings
5. Agent reasons client-side using rubrics + findings       → synthesis
```

## Recipe architecture

```
standards-desk Workato project
  ├── list_pillars.recipe           → returns pillar metadata (hardcoded)
  ├── get_rubrics.recipe            → loops over requested pillars, returns markdown
  │     └── each pillar sub-recipe returns its rubric string
  ├── run_static_checks.recipe      → dispatcher: loops over requested pillars
  │     ├── say_it_plain_checker.recipe
  │     │     ├── Snippet 1: rules dict + rubric markdown (embedded)
  │     │     └── Snippet 2: checker logic (re + string ops)
  │     ├── fact_check_checker.recipe
  │     ├── stick_check_checker.recipe
  │     ├── calibrate_challenge_checker.recipe
  │     ├── delight_check_checker.recipe
  │     └── team_style_guide_checker.recipe
  └── standards_desk.mcp_server
```

## Per-pillar recipe pattern (snippet structure)

**Snippet 1 — Rules + rubric (data layer, update when pillar changes):**
```python
def main(input):
    return {
        "rubric": """...(full pillar markdown)...""",
        "rules": {
            "banned_phrases": ["seamlessly", "robust", ...],
            "regex_patterns": [
                {"pattern": r"\bfire\b", "message": "Use 'emit' or 'trigger'"}
            ],
            "required_sections": [],
        }
    }
```

**Snippet 2 — Checker logic (shared pattern, rarely changes):**
```python
import re

def main(input):
    artifact = input["artifact"]
    rules = input["rules"]
    findings = []
    for phrase in rules.get("banned_phrases", []):
        if phrase.lower() in artifact.lower():
            findings.append({"type": "banned_phrase", "match": phrase})
    for pat in rules.get("regex_patterns", []):
        for m in re.finditer(pat["pattern"], artifact, re.IGNORECASE):
            findings.append({"type": "pattern", "match": m.group(), "message": pat["message"]})
    return {"findings": findings, "pass": len(findings) == 0}
```

## Workato project IDs

| Resource | Value |
|---|---|
| Workspace | TBD (production workspace) |
| Project | TBD |
| MCP server | TBD |
| MCP URL | TBD |

## Design decisions

- **3 tools, not 1 or 6** — discovery + rubrics + checks are distinct operations with distinct callers. One combined tool would force unnecessary data fetching. Six per-pillar tools would bloat MCP context.
- **Rubric embedded in snippet 1** — git is authoritative. Data table would split source of truth.
- **Static checks on Workato, LLM reasoning client-side** — Claude Desktop parity: Desktop can't run local code. Workato handles mechanical checks for all surfaces equally.
- **`pillars` param is always optional** — caller controls scope. Some artifact types don't need all pillars.
