# Simulator folder

CharacterSimulator’s chat engine is the **repo root** file:

**[`../CharacterRuntime.md`](../CharacterRuntime.md)** — paste that entire file into any LLM chat.

This `Simulator/` directory is only layout helpers and old-path stubs. There is **no** second engine here, and CognitiveMiddleware **does not** ship a Simulator anymore.

## Product boundary

| Goal | Product |
|:---|:---|
| Live RP, card stress-test, private sessions | **CharacterSimulator** (this repo) |
| Long-form novel drafting, ledgers, linter, deploy | **[CognitiveMiddleware](https://github.com/Daystar79/CognitiveMiddleware)** |

## Modes (see root runtime)

| Mode | Intent |
|:---|:---|
| **TEST** (default) | Author fidelity — “how would this card act?” |
| **COMPANION** | Ongoing relationship energy |
| **HEAT** | Explicit adult RP — `/adult on` (user 18+) **and** adult character |

**Adult rule:** `/adult on` if you are 18+ → all adult features. Minors remain forbidden on the character side.

**Visuals:** `Images/CharacterRenderingEngine.md` — off by default; `/render` anytime.

## Disclaimer & license

On load, the runtime shows a mandatory legal disclaimer (user/host compliance, 18+ for adult features, no minors). Full text: [`../DISCLAIMER.md`](../DISCLAIMER.md).

Runtime text: CC BY-SA 4.0 (root `LICENSE.md`). Your packs and sessions are your data.
