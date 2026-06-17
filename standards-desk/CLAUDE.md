# standards-desk — Claude context

Standards Desk MCP server. Three tools: pillar discovery, rubric fetch, and static checker. The calling agent does LLM reasoning client-side using the rubrics; Workato handles the mechanical checks.

## Tools

### 1. `list_pillars()`
Returns metadata for all available pillars — names, descriptions, what each checks for. Lightweight discovery. No artifact needed.

```
list_pillars() → [{ name, description, checks_for }]
```

### 2. `get_rubrics(pillars?: string[])`
Returns full rubric markdown for each requested pillar. Omit `pillars` to get all six. The calling agent uses these to reason about the artifact client-side.

```
get_rubrics(pillars?: string[]) → { pillar: rubric_markdown }
```

### 3. `run_static_checks(artifact: string, pillars?: string[])`
Runs mechanical static checks (banned phrases, regex patterns, structural rules) for the requested pillars. Returns findings only — no rubric. Omit `pillars` to run all.

```
run_static_checks(artifact: string, pillars?: string[]) → { pillar: { findings: finding[], pass: bool } }
```

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
1. list_pillars()                              → discover what's available
2. get_rubrics(["say-it-plain", "fact-check"]) → fetch rubrics for selected pillars
3. run_static_checks(artifact, [...])          → get mechanical findings
4. Agent reasons client-side using rubrics + findings → synthesis
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
