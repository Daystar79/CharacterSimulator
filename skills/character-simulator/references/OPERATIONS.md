# CharacterSimulator skill operations

## Entry paths
- Quick-start: use CharacterRuntime's documented presets and menu
- Create: follow the guided builder and produce the full card before roleplay
- Derive: require documented source material; if unavailable, ask for source rather than treating recollection as canon
- Load: accept a supplied card/pack; verify structure and report missing fields without silently inventing them
- Scene test: follow SCENE_TEST.md, keeping simulations separate from edited skits

## State authority & memory gating
Card = immutable identity. Durable log/state = established development and relationships. Live snapshot = turn-local physiological/psychological state. Cache Card + Log `snapshot`/`relational_baselines`/`goal_updates` first every turn; do **not** dump full `memories.detailed` or `history` into the always-on prompt. Keep active working memory bounded to the last 2 hours, and only pull older memories cued by the current scene (`recalled_memories`). The most recent user message is a stimulus, not permission to overwrite the character's identity.

A host may not have persistent file access. State held only in the chat is not saved to disk or cloud. On session close, export the state/pack in text when necessary.

## Validation checklist
- Loaded card exists and contains identity/voice/behavior
- Age and canon-adult fields handled under runtime and host policies
- Character knowledge is bounded to documented card, log and session events
- Pipeline and module registry loaded before play
- No internal pipeline jargon leaks into in-character dialogue
- Every reaction follows the character's incentives and current state
- Branch tests are isolated; only chosen continuation commits
- All save/export claims reflect tools actually available

## Attribution
Public creator identity: Robert Weast.
Product: CharacterSimulator.
Simulacra is a separate cognitive framework/product. Do not merge the repositories or imply this skill bundles the separate Simulacra product distribution.
