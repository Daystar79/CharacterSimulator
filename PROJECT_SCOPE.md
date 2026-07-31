# Project Scope, Architecture & Execution Outline — CharacterSimulator

**Product:** CharacterSimulator  
**Version:** 2.1.0 (Authoritative Product Alignment)  
**System Foundation:** Cognitive Middleware (Cognitive Pipeline v2.1)  
**Target Audience:** AI Agents, LLM Chat Orchestrators, Character Creators, and Roleplay Participants  
**Workspace Root:** `./`  

---

## 1. Executive Summary & Product Mission

**CharacterSimulator** is a standalone, menu-first character simulation and roleplay host application powered by the **Cognitive Middleware** neurobiological engine.

It provides a zero-friction, natural-language interactive roleplay environment where users can:
1. **Quick-Start** preset characters in under a minute.
2. **Create Custom Characters** via a guided plain-language interview that generates full-spec identity cards and machine state objects.
3. **Derive Canon Characters** from documented public sources with strict physical accuracy locks and zero invention of blank lore.
4. **Simulate Realistic Human Behavior** driven by an invisible mind-body pipeline, dual-aspect Wound ↔ Gift psychology, multi-zone somatic cascades, epistemic memory gating, and switchless state persistence.

---

## 2. Architecture & Layer Separation

CharacterSimulator separates the **interaction host / chat UI layer** from the **cognitive simulation engine core**:

```
                              👤 HUMAN PLAYER
                                     │
                                     ▼
 💬 HOST & UI LAYER               CharacterRuntime.md
   ├── Menu UX & Plain Language    ├── Storage Boot (L0–L3) & OOC Parser
   ├── Card Authority (SSOT)       └── JSON Machine State Engine
                                     │
                                     ▼
 🧠 COGNITIVE PIPELINE CORE       Framework/CognitivePipeline.md
   ├── Nervous System (Z1–Z6)      ├── Subconscious Prism (Wound ↔ Gift)
   ├── Raw Affective Impulse       └── Priority Arbitration
                                     │
                                     ▼
 🔌 MODULES EXTENSION API         Framework/Modules.md
   ├── pre_somatic / affect_filter ├── post_vector (Erotica Protocol)
   └── pre_arbitration / app_render└── on_commit (Durable Log Commit)
                                     │
                                     ▼
 🗣️ DEPICTION & VISUAL LAYER      Off-Page RP Prose & Visual Pass
   ├── Narrative RP Prose          └── Images/CharacterRenderingEngine.md
```

### Layer Responsibilities
| System Layer | Primary Responsibilities | Core Files |
|:---|:---|:---|
| **Host & UI Layer** | Menu UX, plain language intent parsing, slash command aliases, storage boot (L0–L3), JSON machine state management, chat hygiene. | [`CharacterRuntime.md`](CharacterRuntime.md) |
| **Cognitive Pipeline** | Neurobiological mind-body simulation, visceral reaction, raw affect, prism interpretation, priority arbitration, 4-channel vector (`Feels`/`Thinks`/`Says`/`Does`). | [`Framework/CognitivePipeline.md`](Framework/CognitivePipeline.md), [`Framework/Psychology/realm_data.yaml`](Framework/Psychology/realm_data.yaml) |
| **Extension API** | Domain injectors at defined loop hooks (`pre_somatic`, `affect_filter`, `pre_arbitration`, `post_vector`, `app_render`, `on_commit`). | [`Framework/Modules.md`](Framework/Modules.md), [`Framework/Mechanics/erotica.md`](Framework/Mechanics/erotica.md) |
| **Card & State Storage** | Dual-file storage: Immutable Build Identity Card + High-speed Machine Runtime State & Durable Log. | [`Characters/[slug].json`](Characters/shinano.json), [`Characters/[slug]_state.json`](Characters/Shinano_state.json) |
| **Visual Rendering** | Motion-driven visual stills, PG-13 / Mature content ceilings, zero RP turn latency by default (`visual_mode: off`). | [`Images/CharacterRenderingEngine.md`](Images/CharacterRenderingEngine.md) |

---

## 3. Product Modes & User Workflows

CharacterSimulator provides four primary entry workflows:

### Workflow [1]: Quick-Start
- **Target:** Users wanting immediate roleplay with zero setup homework.
- **Mechanism:** Select from curated presets (e.g., Ilyra, Cass, Nedra). Automatically instantiates a playable identity card and machine state.

### Workflow [2]: Guided Create Character
- **Target:** Original Character (OC) builders.
- **Mechanism:** Step-by-step interview covering Name, Age, Look/Motion, Voice & Hard Bans, Wound & Gift, History Anchors, Knowledge Depth, and Adult Limits.
- **Output:** Silently writes [`Characters/[slug].json`](Characters/_template.json) (Card) and [`Characters/[slug]_state.json`](Characters/_log_template.yaml) (Machine State).

### Workflow [3]: Derive Canon Card
- **Target:** Existing fictional characters (anime, games, books, lore).
- **Mechanism:** Fetches documented public canon text (wiki, official profiles) as the Single Source of Truth (SSOT).
- **Locks:** Locks physical appearance to source (no beautification or body drift), bounds knowledge to canon role, and leaves missing fields blank rather than inventing lore.

### Workflow [4]: Load / Paste Pack
- **Target:** Power users loading existing character files or pasting portable packs.
- **Mechanism:** Reads identity card and overlays durable log snapshot.

---

## 4. Operational Invariants & Safety

1. **Absolute Age Gate:** Characters with `canon_adult: false` or age < 18 are **permanently barred** from intimate RP or HEAT mode. Minors are never sexual subjects.
2. **Triple Adult Authorization Gate:** HEAT mode requires:
   - User attestation (`adult_auth: true` via `/adult on` or *"I'm 18+"*).
   - Character card eligibility (`canon_adult: true` AND age ≥ 18).
   - Live bond score cap (gated by the authoritative bond friction table).
3. **Off-Page Matrix Invariant:** System mechanics, realm numbers, debt-ledger labels, and psychological jargon run 100% off-page and MUST NEVER leak into character dialogue or narrative RP prose.
4. **Hard Ban Supremacy:** Quoted forbidden tokens/phrases in character `hard_bans` override all other voice color rules.
5. **Switchless State Persistence:** Live state updates every turn tick in working memory; durable evolutions commit automatically to [`Characters/[slug]_log.yaml`](Characters/_log_template.yaml) on scene breaks.

---

## 5. Directory & File Map Outline

```
CharacterSimulator/
├── CharacterRuntime.md                  # Main drop-in host runtime prompt spec
├── PROJECT_SCOPE.md                     # This project scope & architecture outline
├── README.md                            # Product overview & quick-start guide
├── CHANGELOG.md                         # Version history & sync record
├── DISCLAIMER.md                        # Compliance, ToS & safety disclaimers
├── LICENSE.md                           # License agreements
├── Framework/
│   ├── CognitivePipeline.md             # Core mind-body simulation pipeline spec
│   ├── Modules.md                       # Extension API & loop hook registry
│   ├── Rules_Index.md                   # Hard bans & off-page matrix rules
│   ├── Main.md                          # Manuscript drafting specification
│   ├── source_changes.md                # Framework source change history
│   ├── linter.py                        # Automated prose linter for system leaks
│   ├── Mechanics/
│   │   ├── humanity.md                  # Biological timing & human behavior rules
│   │   ├── prose.md                     # Selective prose style selector
│   │   ├── voices.md                    # Spoken vs written syntactical voice engine
│   │   └── erotica.md                   # Intimacy scene craft & adult gating module
│   ├── Psychology/
│   │   └── realm_data.yaml              # 10-realm somatic body catalog (Z1–Z6)
│   └── Schemas/
│       └── psychosomatic_state.json     # Ephemeral live state JSON schema
├── Characters/
│   ├── README.md                        # Character card & log file format documentation
│   ├── HOW_TO_CARD.md                   # Card creation guide (Create vs Derive)
│   ├── _template.json                   # Standard JSON identity card scaffold
│   ├── _log_template.yaml               # Standard YAML durable log scaffold
│   ├── Shinano.md / shinano.json        # Demo character identity cards
│   └── Shinano_state.json               # Demo character machine state object
├── Simulator/
│   ├── README.md                        # Simulator folder guide & scope notes
│   └── CharacterRuntime.md              # Upstream host reference specification
├── Images/
│   └── CharacterRenderingEngine.md      # Visual rendering pipeline & prompt engine
└── scripts/
    ├── run.py                           # Cross-platform CLI runner
    ├── validate_state.py                # JSON state validator
    ├── unix/                            # Unix shell helper scripts (lint, deploy)
    └── windows/                         # Windows PowerShell helper scripts
```

---

*This document serves as the authoritative project scope, architecture, and file layout outline for CharacterSimulator.*
