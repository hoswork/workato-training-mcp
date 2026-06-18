import json

PHASES = {
    "addie-plan": [
        {"phase": "01-customer-voice",   "conversation": 1, "label": "Customer Voice Research"},
        {"phase": "02-content-audit",    "conversation": 1, "label": "Content Audit & Gap Analysis"},
        {"phase": "03-usage-data",       "conversation": 1, "label": "Usage Data-Informed Design"},
        {"phase": "04-needs-analysis",   "conversation": 2, "label": "Needs Analysis"},
        {"phase": "05-audience-profile", "conversation": 2, "label": "Audience Profile"},
        {"phase": "06-learning-objectives", "conversation": 3, "label": "Learning Objectives"},
        {"phase": "07-detailed-outline",    "conversation": 3, "label": "Detailed Outline"},
        {"phase": "08-script-drafting",  "conversation": 4, "label": "Script Drafting"},
        {"phase": "09-knowledge-checks", "conversation": 4, "label": "Knowledge Checks"},
        {"phase": "10-storyboarding",    "conversation": 4, "label": "Storyboarding"},
        {"phase": "11-sme-feedback",     "conversation": 5, "label": "SME Feedback (cross-cutting)"},
    ],
    "wow-plan": [
        {"phase": "phase-0", "conversation": 1, "label": "Roadmap Research"},
        {"phase": "phase-1", "conversation": 2, "label": "Brief"},
        {"phase": "phase-2", "conversation": 2, "label": "Working Backwards Press Release"},
        {"phase": "phase-3", "conversation": 3, "label": "Learning Objectives + Scaffolding"},
        {"phase": "phase-4", "conversation": 3, "label": "Module Breakdown"},
        {"phase": "phase-5", "conversation": 3, "label": "Narrative Arc + Memorability"},
        {"phase": "phase-6", "conversation": 4, "label": "Abstract"},
        {"phase": "phase-7", "conversation": 4, "label": "Verification Gates"},
    ]
}

def main(input):
    skill = (input.get("skill") or "").strip().lower()
    if skill not in PHASES:
        return {"phases_json": json.dumps({"error": "Unknown skill. Use: addie-plan, wow-plan"})}
    return {"phases_json": json.dumps(PHASES[skill])}
