# Changelog

All notable changes to the **CharacterSimulator** project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project tracks chronological / semantic cuts.

**Product split:** CharacterSimulator owns chat/RP. [CognitiveMiddleware](https://github.com/Daystar79/CognitiveMiddleware) owns drafting only (no Simulator folder). Shared psyche vocabulary; separate repos. See [`dependency.yaml`](dependency.yaml).

---

## [Unreleased] - 2026-07-26

### Added
- **Talia card (performer OS)**: Expanded [`Characters/talia.md`](Characters/talia.md) + log — WV Orthodox → 19 cut → adult-creator routine; sexual delight; manga effect; core wound = fault-blindness (not Thomas-as-center). Optional cast history only.
- **Random session variants**: Cards may define `session_variants` with `selection: random_on_load`. Runtime rolls shoot/chat/off (or card-defined modes) on `/load` and `/reset`; **no user picker**. Documented in [`CharacterRuntime.md`](CharacterRuntime.md). Talia ships three equal-weight modes.
- **Related-project pin**: Added [`dependency.yaml`](dependency.yaml) for CognitiveMiddleware as sibling drafting product (shared assets + pin), not a monorepo extract.
- **Git remotes**: Linked `origin` to [Daystar79/CharacterSimulator](https://github.com/Daystar79/CharacterSimulator) and `upstream` to [Daystar79/CognitiveMiddleware](https://github.com/Daystar79/CognitiveMiddleware) (related compare remote).
- **Project changelog**: This file (`CHANGELOG.md`) for CharacterSimulator-specific release notes.
- **Load-time disclaimer**: Mandatory OOC disclaimer on CharacterRuntime storage boot — download/execute is on the user; legal compliance; 18+ for adult features; no minors; AS IS; GitHub ToS/AUP. Full text in [`DISCLAIMER.md`](DISCLAIMER.md); summary in README.
- **Connector probe on storage boot**: Live inventory + smoke tests for Google Drive, Dropbox, OneDrive, local FS, optional GitHub; boot message lists OK/FAIL/absent per connector; `/storage` re-probes; overall L0–L3 from highest working level.

### Fixed
- **Card authority / anti-drift**: Runtime now requires CARD as identity SSOT each turn; MEMORY only overlays runtime snapshot fields; chat history cannot replace voice/physical/hard_bans. Added `/reload card`, load/reset re-bind rules, and forbidden “play from model memory” failure modes.

### Changed
- **Autosave default on**: CharacterRuntime defaults `autosave: true` when storage is L1/L3; dirty MEMORY flushes to primary connector after IC turns. Explicitly not Midlayer book-commit — live RP memory only. `/autosave off` for ephemeral TEST.
- **README rewrite**: Replaced the short stub with a full product guide (quick start, pack schema, psyche model, commands, visual modes, safety, license carve-out, related-project map).
- **Single public runtime**: Root [`CharacterRuntime.md`](CharacterRuntime.md) is the only engine. `Simulator/CharacterRuntime.md` is a stub pointer. Private unlocked runtime retired.
- **Simple adult unlock**: `/adult on` = user confirms 18+ → unlock all adult features. Removed jurisdiction probes, country codes, and multi-step `/affirm` handshake. Character minor bans unchanged. Historical HEAT no longer permanently locked (still needs user adult + adult character).
- **Turn-loop `/render`**: Forced `/render` always runs a visual pass even when `visual.mode: off`. Removed ghost `visual.mode: on` from rendering engine agent steps.
- **Separated concerns**: Documented CharacterSimulator as the chat/RP product and CognitiveMiddleware as drafting-only (no Simulator). `dependency.yaml` reframed from “extract pin” to sibling/shared-asset pin.

### Removed
- **Sample character cast**: Deleted all named demo cards and logs under `Characters/` (ensemble, historical, mythic, and other test packs), plus `Relations.md` and `Relationships.canvas`. Public scaffolds only: `_template.md`, `_log_template.yaml`, `README.md`.
- **Dual/public private runtime forks**: No second public CharacterRuntime body; no separate Private engine for “unlocked” adult.

---

## [1.0.0] - 2026-07-26

Standalone repository cut: CharacterSimulator published as its own GitHub project for chat/RP (concerns later fully separated from CognitiveMiddleware drafting).

### Added
- **Repository bootstrap**: Initial git history on `main` (`00d181d`).
- **CharacterRuntime**: Self-contained somatic roleplay engine — storage boot (L0–L3), Character Pack schema, modes TEST / COMPANION / HEAT, bias prism, ten realms, epistemic memory & skills, safety gates.
- **CharacterRenderingEngine**: Motion-driven visual pipeline; default `visual.mode: off`.
- **Realm data**: [`Framework/Psychology/realm_data.yaml`](Framework/Psychology/realm_data.yaml).
- **Public scaffolds**: [`Characters/_template.md`](Characters/_template.md), [`_log_template.yaml`](Characters/_log_template.yaml), [`Characters/README.md`](Characters/README.md).
- **License**: Hybrid MIT + CC BY-SA 4.0 with author-local carve-out ([`LICENSE.md`](LICENSE.md)).

### Notes
- Drafting stack remains in CognitiveMiddleware only.
- Shared psyche vocabulary originated in the CognitiveMiddleware / Simulator era before the product split.

---

## Shared lineage (historical)

Before the split, chat runtime lived under CognitiveMiddleware’s Simulator. Themes that shaped this product:

| Period | Themes |
|:---|:---|
| 2026-07-23 | Vocal fields; motion-driven visual layer |
| 2026-07-17 | Adult path; Simulator as optional side tool; dual license |
| 2026-07-15 – 16 | Transformation / depth of knowledge; historical gates; YAML cards |
| 2026-07-12 – 14 | Body-first somatics; off-page matrix; CognitiveMiddleware rebrand |

CognitiveMiddleware release notes (drafting product): [CHANGELOG](https://github.com/Daystar79/CognitiveMiddleware/blob/main/CHANGELOG.md).

---

## Versioning

- **Major** — Breaking pack schema, command, or safety-gate changes that invalidate existing packs or sessions.
- **Minor** — New engine capabilities, visual modes, or documented workflows that remain backward-compatible.
- **Patch** — Docs, pin bumps without behaviour change, template clarifications, non-breaking hygiene.

Unreleased work lands under `## [Unreleased]` until a dated cut is published.
