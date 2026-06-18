# training-workflow

Three-tool Workato MCP — context-before-execution pattern (mirrors Enterprise Data MCP):
  get_skill_context → list_phases → get_phase_prompt

Python source: `cli/` (source of truth — embed into recipe JSON before pushing).
Recipe JSON: `workato/training-workflow/`.
Push: `cd workato && workato push --restart-recipes`, then re-assign tools via Dev API.

Skills stay fully standalone. This MCP is additive — for Cowork users with BT integration.
