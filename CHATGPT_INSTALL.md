# CharacterSimulator skill distribution
**Creator: Cian Didymos**

CharacterSimulator is a separate product from Simulacra. Its skill includes the interactive runtime, public card templates, cognitive framework references, scene-testing instructions, and state operations.

## Build
Run `python scripts/validate_skill.py` locally or run the **Package CharacterSimulator Skill** GitHub Actions workflow.

The workflow uploads `character-simulator-distribution` containing two files:
- `character-simulator-chatgpt.zip`: upload to ChatGPT **New Plugin**. The archive contains `skills/character-simulator/SKILL.md` at the required path.
- `character-simulator.skill`: portable Agent Skills archive with `character-simulator/SKILL.md` at the root folder.

Extract the GitHub Actions artifact ZIP first, then upload the **inner** ChatGPT ZIP. Acceptance by ChatGPT and behavior on other hosts must be verified in their respective interfaces.

## Test
1. Install and ask to create a character or load a supplied card.
2. Test a baseline reaction to a scene, then branch from the same state with a changed stimulus.
3. Request an 8–15-second skit adaptation and verify the output distinguishes simulation from editorial dialogue.
4. Export state; confirm that it does not claim durable saving unless storage was actually available.

Named character cards, private packs and filled logs are intentionally excluded. The skill does not ship an external database or guarantee cross-session persistence.
