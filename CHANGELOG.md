# Changelog

All notable changes to the **CharacterSimulator** project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project tracks chronological / semantic cuts.

**Product split:** CharacterSimulator owns chat/RP. [CognitiveMiddleware](https://github.com/Daystar79/CognitiveMiddleware) owns drafting only (no Simulator folder). Shared psyche vocabulary; separate repos. See [`dependency.yaml`](dependency.yaml).

---

## [Unreleased] - 2026-07-29

### Added
- **Dual-Aspect Psyche Matrix (Wound & Gift)** (synced from CognitiveMiddleware `4ea247f`): Cards and runtime now carry `cognitive_gift` + `voice.generative_stance` beside wound fields. Bias state resolves `DORMANT` / `DEFENSIVE_ACTIVE` / `GENERATIVE_ACTIVE` off-page.
- **Full-Body Cascade**: Multi-zone somatic rule (2+ linked body zones per state shift); shared `Framework/Psychology/realm_data.yaml` zone alignments from CognitiveMiddleware.
- **Gift fields on cast**: `anya`, `kira`, `serena`, `vera`, `victor` each have a gift + generative stance paired to their wound.

### Changed
- **CognitiveMiddleware pin**: `dependency.yaml` → `4ea247fea72a053041616d5556be4abe2068cded` (2026-07-29).
- **Create / HOW_TO_CARD**: Guided builder step 5 is Wound & Gift (dual-aspect), not wound alone.
- **Character Renaming & Book Decoupling**: Renamed all 5 character cards and logs to fully decouple the ensemble from external book references:
  - `Selene` → **Serena** (`serena.md` / `serena_log.yaml`)
  - `Talia` → **Kira** (`kira.md` / `kira_log.yaml`)
  - `Mara` → **Anya** (`anya.md` / `anya_log.yaml`)
  - `Rue` → **Vera** (`vera.md` / `vera_log.yaml`)
  - `Valen` → **Victor** (`victor.md` / `victor_log.yaml`)
- **Cast Web Update**: Updated [`Relations.md`](Characters/Relations.md) cross-reference matrix to reflect the renamed cast and standalone relational dynamics.

### Fixed
- **Framework logic (runtime):** Variant preserve on `/load`; epistemic transient answers; L0 dirty export prompt; unified **bond → HEAT cap** table; `last_somatic_zone` on snapshot; hard-ban token extraction (not whole-line / overbroad word bans).
- **Fresh cast logs:** Reset `anya`, `kira`, `serena`, `vera`, `victor` logs to clean `as_of: build` (empty memories/history, `session_variant: null`, no heat/bond/`adult_auth`/visual residue).
- **Session variant policy:** Cast `re_roll_on: ["reset"]` only — cold `/load` preserves log variant.
- **Serena ↔ Vera:** Serena card relationships + verbal shift for closed-circuit partner (was missing).
- **Realm SSOT:** Single path `Framework/Psychology/realm_data.yaml`; removed divergent root `realm_data.yaml`.

### Optimized & Streamlined
- **Framework Optimization & Logic Reduction**: Streamlined core files for context density and strict logic boundaries.
- **`CharacterRuntime.md` Streamlining**: Menu-first UX, full-card Create, epistemic, bond/HEAT, somatic rotation.
- **`Images/CharacterRenderingEngine.md` Reduction**: Compressed pipeline while keeping stages, camera/pose maps, motion fingerprint, prompt cleanup.
- **Character Card Standardization**: Renamed cast cards (`serena`, `kira`, `anya`, `vera`, `victor`) cleaned to template schema (session variants, history, knowledge, `somatic_zones`).
- **Documentation & Scaffolds Clean-up**: `HOW_TO_CARD.md`, `README.md`, `Simulator/README.md` focused on actionable workflows.


### Added
- **Menu-first UX**: Boot menu + plain language as primary controls; slash commands demoted to optional power aliases (not listed in first message).
- **Full-card Create**: Guided step-by-step builder (not CM cast factory) outputs a **complete** card + empty log — name, age, physical, full voice, bias/focus mapping, **history_anchors**, **depth_of_knowledge**, optional scene/adult boundaries. Required path quality for companions / adult RP.
- **Epistemic block restored (compact)**: Runtime binds knowledge to card anchors + depth_of_knowledge + MEMORY memories/skills/history; detailed / footnote / forgotten; skill tiers; no durable invented backstory mid-RP.
- **Quick-start presets**: Ilyra / Cass / Nedra or one-liner tryout; prompts upgrade to Create for rich/adult play.
- **Soft storage boot**: One-line storage status; full connector inventory only on demand.
- **Beginner docs**: [`Characters/HOW_TO_CARD.md`](Characters/HOW_TO_CARD.md), [`Characters/_template_lite.md`](Characters/_template_lite.md); Characters + root README aligned to create/quick-start paths.

### Added (earlier unreleased)
- **Kira performer OS** (renamed from Talia lineage): Adult-creator routine; shoot/chat/off variants; Wound Absolver; optional Victor history.
- **Random session variants**: `session_variants` with silent random selection; re-roll on reset by default; **no user picker**.
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
