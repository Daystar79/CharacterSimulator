# Simulator Directory

The primary chat engine for CharacterSimulator is located at the root of the repository:

👉 **[`../CharacterRuntime.md`](../CharacterRuntime.md)** — Paste this entire file into any LLM chat.

---

## 📌 Product Boundaries

| Goal | Product / Location |
|:---|:---|
| Live RP, card stress-testing, private sessions | **CharacterSimulator** (this repository) |
| Long-form novel drafting, ledgers, linter, deploy | **[CognitiveMiddleware](https://github.com/Daystar79/CognitiveMiddleware)** |

---

## 🛠️ Modes & Visuals

- **Modes:** `TEST` (fidelity checks), `COMPANION` (relationship energy), `HEAT` (explicit adult RP via `/adult on`).
- **Visuals:** Decoupled visual rendering pipeline documented in [`../Images/CharacterRenderingEngine.md`](../Images/CharacterRenderingEngine.md).
- **Disclaimer:** Legal and safety terms in [`../DISCLAIMER.md`](../DISCLAIMER.md).
