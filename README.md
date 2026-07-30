# CharacterSimulator
**A psychological simulation framework for AI characters that feel alive.**

[![License: MIT + CC BY-SA 4.0](https://img.shields.io/badge/license-MIT%20%2B%20CC%20BY--SA%204.0-blue.svg)](LICENSE.md)
[![Status: Active](https://img.shields.io/badge/status-active-green.svg)](CHANGELOG.md)

---

## 🎯 What Is CharacterSimulator?

CharacterSimulator is a **prompt-based runtime engine** that turns any LLM chat into a **psychologically complex character simulator**. Designed for authors, roleplayers, and AI enthusiasts, it ensures characters:
- **React physically before they speak** (Somatic Engine).
- **Act on hidden psychological biases** (Off-page Psyche Matrix).
- **Maintain bounded memory and identity** (Epistemic Memory & Card Authority).
- **Prevent identity drift** across long sessions.

**Think of it as a "character OS" for LLMs.**

---

## 🚀 Quick Start

1. **Copy** [`CharacterRuntime.md`](CharacterRuntime.md) and paste it into any LLM chat.
2. Read the short disclaimer and choose:
   - **[1] Quick-start** — Pick a preset and play in seconds.
   - **[2] Create a character** — Guided interview to build a full custom card.
   - **[3] Load or paste** — Load an existing pack (`Characters/[slug].md`).
3. Play. Say `save` or `show pack` anytime to export your session data.

---

## 🧠 Core Features

| Feature | Description |
|:---|:---|
| **Somatic Engine** | Zone-based physical reactions (face, throat, chest, hands, posture, feet) before dialogue. |
| **Psyche Matrix** | 10 psychological Realms and 6 Cognitive Biases warping perception off-page. |
| **Epistemic Memory** | Knowledge strictly bounded to CARD anchors, log memories, and session events. |
| **Modes** | `TEST` (fidelity checks), `COMPANION` (relationship energy), `HEAT` (explicit adult RP). |
| **Safety Gates** | Absolute safety rules (18+ attestation required for adult content, no minors, no real persons). |
| **Visual Rendering** | Decoupled image pipeline (`Images/CharacterRenderingEngine.md`) supporting fast tags, prompts, or live stills. |
| **Storage Levels** | L0 (paste-only) to L3 (cloud R/W) with automatic dirty-state autosave. |

---

## 📚 Documentation

- [Full Runtime](CharacterRuntime.md) — Main prompt engine (paste this to play).
- [Realm Data](Framework/Psychology/realm_data.yaml) — Ten-realm brace/release SSOT (somatic profiles).
- [Card Builder Guide](Characters/HOW_TO_CARD.md) — Step-by-step character creation.
- [Characters Folder](Characters/README.md) — Card scaffolds & cast repository.
- [Rendering Engine](Images/CharacterRenderingEngine.md) — Visual frame generation pipeline.
- [Changelog](CHANGELOG.md) — Updates and version history.
- [License](LICENSE.md) — Usage rights and licensing.
