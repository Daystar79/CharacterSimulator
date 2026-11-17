---
name: character-simulator
description: Run stateful fictional character roleplay, build character cards, load character packs, and test psychological consistency using the CharacterSimulator runtime. Use when the user wants to create, load, roleplay with, or test an autonomous fictional character.
---
# CharacterSimulator

This is the interactive roleplay host from [Daystar79/CharacterSimulator](https://github.com/Daystar79/CharacterSimulator), distributed separately from the Simulacra skill.

## Start
1. Read `references/CharacterRuntime.md` in full; it defines the session boot, turn loop, rendering and commands.
2. Load `references/Framework/CognitivePipeline.md`, `references/Framework/Rules_Index.md`, `references/Framework/Modules.md`, `references/Framework/Psychology/realm_data.yaml` and `references/Framework/Schemas/psychosomatic_state.json`.
3. Offer the runtime's four entry paths: quick-start, create character, derive from documented sources, or load an existing card/pack.
4. For creation use `references/Framework/Prompts/character_builder_prompt.md`, `references/Characters/HOW_TO_CARD.md` and the card templates.
5. Before each response run the upstream dual-circuit cognitive loop. The host handles input and presentation; the pipeline owns the character's psyche.
6. Preserve card identity, epistemic boundaries, memory, competence and character agency. Keep internal matrix jargon out of in-character dialogue.
7. Track live state per turn. Maintain durable state across turns within the available context; when file persistence is unavailable, clearly distinguish in-chat continuity from saved durable logs and offer an exportable pack. Never claim files were saved without a successful write.
8. Apply the host's safety rules and higher-priority platform constraints. Do not assume image generation or external storage is available.

## Source-of-truth
Bundled references are copied from CharacterSimulator at build time, not rewritten summaries. Do not invent absent character data or claim external character packs are loaded until provided.
