# CharacterSimulator
**A psychological simulation framework for AI characters that feel alive.**

[![License: MIT + CC BY-SA 4.0](https://img.shields.io/badge/license-MIT%20%2B%20CC%20BY--SA%204.0-blue.svg)](LICENSE.md)
[![Status: Active](https://img.shields.io/badge/status-active-green.svg)](CHANGELOG.md)

---

## What is CharacterSimulator?

CharacterSimulator is two related layers:

| Layer | What it is | Where |
|:---|:---|:---|
| **Runtime / framework** | Prompt-based **character OS** for any LLM chat — somatic body, psyche matrix, card authority, safety gates | This repo (`CharacterRuntime.md`, `Framework/`) |
| **Desktop host** | **Simulacra** — native app that loads cards, runs sessions, themes, portraits/scenes, SQLite profiles | Sibling repo **CharacterSimulator.UI** (product name: Simulacra) |

The runtime ensures characters:

- **React physically before they speak** (Somatic Engine)
- **Act on hidden psychological biases** (Psyche Matrix)
- **Keep bounded memory and identity** (Epistemic Memory & Card Authority)
- **Avoid identity drift** across long sessions

Think of the framework as a **character OS for LLMs**, and the desktop project as the **host shell** that runs that OS with a real UI.

---

## Quick start (chat / paste)

1. **Copy** [`CharacterRuntime.md`](CharacterRuntime.md) and paste it into any LLM chat.
2. Read the short disclaimer and choose:
   - **[1] Quick-start** — Pick a preset and play in seconds.
   - **[2] Create a character** — Guided interview to build a full custom card.
   - **[3] Derive** — Canon-locked card from documented public sources.
   - **[4] Load or paste** — Existing pack (`Characters/[slug].md` / `.json`).
3. Play. Say `save` or `show pack` anytime to export session data.

Desktop host (**Simulacra**): build and run **CharacterSimulator.UI** (`CharacterSimulator.GUI`) against the same card formats.

---

## Character cards (identity)

Cards are **identity / build sheets** — not movement history (that lives in logs / state).

Keep these **separate** (never one merged “description” blob):

| Field | Role |
|:---|:---|
| **`personality`** | Who they are — temperament, values, social stance |
| **`behavior`** | How they act under pressure, trust, and routine |
| **`physical`** | Body only (imaging layer; structured map preferred) |
| **`character_style`** | Default dress / accessories (not art medium) |
| **`hobbies`** | Free-time activities / scene fuel |
| **`voice`** + psyche matrix | Speech + engine wound/gift mappings |

Templates: [`Characters/_template.md`](Characters/_template.md), [`Characters/_template.json`](Characters/_template.json).  
How-to: [`Characters/HOW_TO_CARD.md`](Characters/HOW_TO_CARD.md).  
Format notes: [`Characters/README.md`](Characters/README.md).

Imaging stills use **`physical` + `character_style`** (see [`Images/CharacterRenderingEngine.md`](Images/CharacterRenderingEngine.md)); art medium is runtime `/style`, not a card field.

---

## Core features

| Feature | Description |
|:---|:---|
| **Somatic Engine** | Zone-based physical reactions (face, throat, chest, hands, posture, feet) before dialogue. |
| **Psyche Matrix** | 10 psychological Realms and dual-aspect wound/gift warping perception off-page. |
| **Epistemic Memory** | Knowledge bounded to CARD anchors, log memories, and session events. |
| **Modes** | `TEST` (fidelity checks), `COMPANION` (relationship energy), `HEAT` (explicit adult RP). |
| **Safety Gates** | 18+ attestation for adult content; no minors; no real persons. |
| **Visual Rendering** | Decoupled image pipeline (`Images/CharacterRenderingEngine.md`) — tags, prompts, or live stills. |
| **Storage Levels** | L0 (paste-only) to L3 (cloud R/W) with dirty-state autosave. |

---

## Documentation

- [Full Runtime](CharacterRuntime.md) — Main prompt engine (paste this to play)
- [Project Scope](PROJECT_SCOPE.md) — Architecture and workflows
- [Realm Data](Framework/Psychology/realm_data.yaml) — Ten-realm brace/release SSOT
- [Card Builder Guide](Characters/HOW_TO_CARD.md) — Create / derive card steps
- [Characters Folder](Characters/README.md) — Card scaffolds and format rules
- [Character Builder Prompt](Framework/Prompts/character_builder_prompt.md) — Agent-guided card authoring
- [Rendering Engine](Images/CharacterRenderingEngine.md) — Visual frame pipeline
- [Changelog](CHANGELOG.md) — History
- [License](LICENSE.md) — Usage rights

**Simulacra** (desktop host) docs — themes, SQLite, GUI: sibling **CharacterSimulator.UI** `README.md`.
