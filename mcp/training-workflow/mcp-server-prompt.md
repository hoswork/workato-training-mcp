# training-workflow MCP — server description and tool descriptions

## Server description
> Training workflow assistant for addie-plan and wow-plan. Follows a context-before-execution pattern: call get_skill_context first, then list_phases to understand the structure, then get_phase_prompt to retrieve specific prompts. Skills remain fully standalone — this MCP provides always-current prompts without reinstalling.

## Recommended call order (mirrors Enterprise Data semantic layer pattern)
1. `get_skill_context(skill)` — Project setup, file structure, conversation groups
2. `list_phases(skill)` — phase index with conversation groupings
3. `get_phase_prompt(skill, phase)` — full prompt text for execution

## Tool: get_skill_context
> Returns Project setup instructions, file structure, and conversation groups for addie-plan or wow-plan. Call this first to understand the workflow before fetching specific phases.

## Tool: list_phases
> Lists available phases for a training skill (addie-plan or wow-plan) with conversation groupings showing which phases run together and what files they read and write.

## Tool: get_phase_prompt
> Returns the full prompt text for a specific phase. Pass skill (addie-plan or wow-plan) and phase (e.g. 01-customer-voice for addie-plan, phase-0 for wow-plan). Returns prompt_text and error.
