# CharacterSimulator — ChatGPT plugin

CharacterSimulator is distributed independently of [Simulacra-Skill](https://github.com/Daystar79/Simulacra-Skill).

1. Run the **Package CharacterSimulator for ChatGPT** workflow from GitHub Actions.
2. Download the `character-simulator-chatgpt` workflow artifact and extract the outer artifact archive.
3. In ChatGPT, choose **New Plugin** and upload `character-simulator-chatgpt.zip`.

The plugin archive contains `skills/character-simulator/SKILL.md`, the interactive runtime, cognitive framework, schemas, public templates and character-builder instructions. The path matches the ChatGPT upload dialog's reported `skills/*/SKILL.md` requirement; actual acceptance must be verified after building.

The packager uses a strict allowlist. Named character cards, filled logs, private packs and user data are not included.

## Local build

```bash
python scripts/package_chatgpt.py
```

This package is an LLM skill, not a hosted state service. Long-term persistence depends on the host's available file tools; users can export packs when persistence isn't available.
