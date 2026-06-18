import json

SKILL_CONTEXTS = {
    "addie-plan": {
        "description": "Async self-paced e-learning course design using the ETT ADDIE Prompt Pipeline (Amelia Blevins).",
        "surface": "Claude Desktop Cowork or Chat — requires a Claude Desktop Project per course.",
        "project_instructions": "Course: [course-name]\nWorking files: brief.md · world.md · course.md · build.md · log.md\nIf I say 'resume' or start without context: read @log.md CURRENT STATE block and announce where we are. Always read @brief.md before responding.",
        "file_structure": {
            "brief.md": "Stable anchor: audience, goal, format, delivery date, product scope. Fill once before starting.",
            "world.md": "What is TRUE externally: customer voice, content gaps, usage data, GA deps, platform changes. Written by conversations 1-2.",
            "course.md": "What WE DECIDED: needs analysis, audience profile, learning objectives, outline. Written by conversations 2-3.",
            "build.md": "What gets BUILT: scripts, Knowledge Checks, storyboards. Written by conversation 4.",
            "log.md": "Running record: quality gate results, CURRENT STATE block at top, decisions made."
        },
        "conversation_groups": [
            {"id": 1, "label": "Project Prep", "phases": ["01-customer-voice", "02-content-audit", "03-usage-data"], "reads": ["brief.md"], "writes": ["world.md"]},
            {"id": 2, "label": "Analyze",      "phases": ["04-needs-analysis", "05-audience-profile"],             "reads": ["brief.md", "world.md"], "writes": ["course.md"]},
            {"id": 3, "label": "Design",       "phases": ["06-learning-objectives", "07-detailed-outline"],        "reads": ["brief.md", "world.md", "course.md"], "writes": ["course.md"]},
            {"id": 4, "label": "Develop",      "phases": ["08-script-drafting", "09-knowledge-checks", "10-storyboarding"], "reads": ["brief.md", "course.md"], "writes": ["build.md"]},
            {"id": 5, "label": "SME Feedback", "phases": ["11-sme-feedback"],                                      "reads": ["brief.md", "build.md"], "writes": ["build.md"]}
        ],
        "quality_gates": "the-once-over invoked in gate mode after each conversation. Single pillar fail = block. Iterate until clean before writing output file and closing conversation.",
        "resume_pattern": "Say 'resume'. Claude reads log.md CURRENT STATE and picks up without re-explanation."
    },
    "wow-plan": {
        "description": "1-day WoW workshop course planning using Amazon Working Backwards.",
        "surface": "Claude Desktop Cowork or Chat — requires a Claude Desktop Project per course.",
        "project_instructions": "Course: [course-name]\nWorking files: brief.md · world.md · plan.md · log.md\nIf I say 'resume' or start without context: read @log.md CURRENT STATE block and announce where we are. Always read @brief.md before responding.",
        "file_structure": {
            "brief.md": "WHO/WHAT/WHEN/CONSTRAINTS: topic, audience, duration, tier, output mode, track context. Fill once before starting.",
            "world.md": "WHAT IS TRUE: feature deps, GA dates, Jira blockers, platform changes, FDE refs. Written by conversation 1.",
            "plan.md": "THE COURSE PLAN growing through phases: press release → LOs → modules → narrative → abstract. Written by conversations 2-4.",
            "log.md": "Running record: quality gate results, open questions, CURRENT STATE block at top."
        },
        "conversation_groups": [
            {"id": 1, "label": "Roadmap Research",       "phases": ["phase-0"], "reads": ["brief.md"], "writes": ["world.md"]},
            {"id": 2, "label": "Brief + Press Release",  "phases": ["phase-1", "phase-2"], "reads": ["brief.md", "world.md"], "writes": ["plan.md"]},
            {"id": 3, "label": "LOs + Modules + Narrative", "phases": ["phase-3", "phase-4", "phase-5"], "reads": ["brief.md", "world.md", "plan.md"], "writes": ["plan.md"]},
            {"id": 4, "label": "Abstract + Verification", "phases": ["phase-6", "phase-7"], "reads": ["brief.md", "plan.md"], "writes": ["plan.md"]}
        ],
        "quality_gates": "the-once-over invoked in gate mode at Phase 7. Single pillar fail = course plan blocked. Iterate until clean.",
        "resume_pattern": "Say 'resume'. Claude reads log.md CURRENT STATE and picks up without re-explanation."
    }
}

def main(input):
    skill = (input.get("skill") or "").strip().lower()
    if skill not in SKILL_CONTEXTS:
        return {"context_json": json.dumps({"error": "Unknown skill. Use: addie-plan, wow-plan"})}
    return {"context_json": json.dumps(SKILL_CONTEXTS[skill])}
