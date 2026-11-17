---
name: character-simulator
description: Stateful fictional character simulation and scene testing. Create or derive character cards, load packs, roleplay, branch reactions, test fidelity, and adapt validated scenes into short skits using the CharacterSimulator runtime.
---
# CharacterSimulator
**Creator: Cian Didymos**

CharacterSimulator is an interactive character simulation product, independently distributed from the Simulacra skill. The bundled runtime and framework references are the authoritative implementation.

## Select workflow
- **Quick-start, create, derive, load, or roleplay:** Read `references/CharacterRuntime.md` and `references/OPERATIONS.md`. Follow the runtime's menu and natural-language commands.
- **Test a character's reaction or a scene:** Also read `references/SCENE_TEST.md`. Load the actual card and state first. Branch alternate reactions from the same initial snapshot; only commit a chosen continuation.
- **Turn a simulated scene into a skit:** First simulate faithfully, then explicitly label the edited, time-constrained script as an adaptation.

## Required boot
1. Read `references/CharacterRuntime.md`, `references/Framework/CognitivePipeline.md`, `references/Framework/Rules_Index.md`, `references/Framework/Modules.md`, `references/Framework/Psychology/realm_data.yaml`, and `references/Framework/Schemas/psychosomatic_state.json`.
2. For character creation/derivation, also read `references/Framework/Prompts/character_builder_prompt.md`, `references/Characters/HOW_TO_CARD.md` and card templates.
3. Verify the character card and any log/state overlay. Card defines identity; logs define durable evolution; the live snapshot changes each tick.
4. Execute the cognitive pipeline per turn; render the four-channel result through the roleplay host. Keep engine jargon off-page.
5. Enforce knowledge limits, active character agency, continuity, safety and host policies.
6. Report storage capabilities accurately. If file persistence is unavailable, maintain session state in context and offer export; never claim autosave occurred without a write.

## Non-negotiable fidelity
Do not invent a loaded character card, documented canon, prior events or persistent state. If the card is absent, ask for it or help create one. Do not turn character simulation into an agreeable assistant persona. Simulation results and editorial comedy rewrites are distinct.
