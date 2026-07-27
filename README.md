# CharacterSimulator

**Standalone roleplay engine and character stress-testing suite**

Drop a single markdown runtime into any LLM chat, load a character pack, and run live sessions that keep psyche, body, and memory *off-page* — fidelity-first for authors, or private companion RP when you choose.

Repository: [github.com/Daystar79/CharacterSimulator](https://github.com/Daystar79/CharacterSimulator)

---

## Disclaimer

**If you download this project and execute it, that is on you.** Authors publish files; they do not operate your chat, model, or host. You own legal compliance, third-party ToS, and anything you create or publish. Adult features require that you are **18+**. Sexual content involving minors is forbidden.

When `CharacterRuntime.md` loads, a short **OOC disclaimer is shown first** (required). Full terms: [`DISCLAIMER.md`](DISCLAIMER.md).

This repository is hosted under [GitHub’s Terms of Service](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service) and [Acceptable Use Policies](https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies). Do not use the project or GitHub to host illegal content, CSAM, or other prohibited material. Specs are provided **AS IS**, without warranty.

---

## Related project (separated concerns)

| Product | Repo | Owns |
|:---|:---|:---|
| **CharacterSimulator** (this repo) | [Daystar79/CharacterSimulator](https://github.com/Daystar79/CharacterSimulator) | Chat runtime, card stress-test, private RP, visual pass for live sessions |
| **CognitiveMiddleware** | [Daystar79/CognitiveMiddleware](https://github.com/Daystar79/CognitiveMiddleware) | Drafting middle layer only (Framework, rules, linter, deploy, book ledgers) |

Simulator/chat is **not** a folder inside CognitiveMiddleware anymore. Concerns are split: draft manuscripts there; run live character sessions here.

They still share vocabulary (ten realms, bias prism, body-first somatics, card/log YAML). Optional shared assets and pin notes live in [`dependency.yaml`](dependency.yaml). Git remote name `upstream` points at CognitiveMiddleware for compare/sync of shared scaffolds only.

```bash
git fetch upstream
# e.g. compare realm data: git show upstream/main:Framework/Psychology/realm_data.yaml
```

---

## What this is

CharacterSimulator is a **prompt-as-engine** product. There is no app to install. The engine is the runtime file; state lives in portable **Character Packs** (card + memory).

| Layer | Role |
|:---|:---|
| **CharacterRuntime** | Somatic roleplay engine: storage boot, modes, bias prism, turn loop, safety gates |
| **Character cards + logs** | Identity (build defaults) and runtime matrix (live snapshot + history) |
| **Realm data** | Ten psychological realms → somatic / vocal brace–release profiles |
| **Rendering engine** | Optional visual pass (prompts or live stills); **off by default** for zero turn latency |

Use it for **live character chat**, **card fidelity checks** before drafting, and **private RP**. Core rules: body before insight, imperfect memory, no mind-reading, no therapy-speak, matrix terms never spoken in character.

---

## Quick start

1. **Load the engine**  
   Paste the full contents of [`CharacterRuntime.md`](CharacterRuntime.md) into a new LLM chat  
   (**one** runtime — that file only).  
   Optional: also load [`Images/CharacterRenderingEngine.md`](Images/CharacterRenderingEngine.md) if you want visuals later.

2. **Storage boot**  
   The model **probes connectors live** (Google Drive, Dropbox, OneDrive, local files, etc.), reports what is OK / fail / not available, then offers:
   - **[1]** Load pack (name, path, or cloud)
   - **[2]** Create pack (wizard)
   - **[3]** Paste pack or card (session-only until `/save`)
   - **[4]** Canon quick-start (public-domain or historical only — see [Safety](#safety--gates))  
   Re-check anytime with `/storage`.

3. **Load a character**  
   Create a card from the public scaffolds (local / agent with filesystem):

   ```text
   Characters/_template.md       → Characters/[slug].md
   Characters/_log_template.yaml → Characters/[slug]_log.yaml
   ```

   Or paste a portable pack (`## META` + `## CARD` + `## MEMORY`) as described in the runtime.

4. **Play**  
   Default mode is **TEST** (author fidelity). Optional:
   - `/adult on` — if you are 18+, unlock **all** adult features
   - `/mode companion` or `/mode heat` — relationship energy / explicit (heat needs adult user + adult character)
   - `/user name: Alex relationship: partner` — set your persona
   - `/scenario kitchen, late evening` — set place/time

5. **Persist (autosave on by default)**  
   When storage is **L1 or L3**, MEMORY auto-writes to the primary connector after dirty turns. Use `/autosave off` for a throwaway TEST session, or `/save` to flush now. **Midlayer** handles book drafting commits — not this runtime.

---

## Repository layout

```text
CharacterSimulator/
├── README.md                      # This guide
├── DISCLAIMER.md                  # Legal / GitHub ToS responsibility notice
├── CHANGELOG.md                   # Project release notes
├── dependency.yaml                # Related CM pin + shared-asset map
├── LICENSE.md                     # Dual license + author-local carve-out
├── CharacterRuntime.md            # Sole public drop-in runtime (SSOT)
├── .gitignore
│
├── Simulator/                     # Optional layout helpers (engine is root file)
│   ├── README.md                  # When to use this product vs drafting
│   ├── CharacterRuntime.md        # Stub → ../CharacterRuntime.md
│   └── Private/                   # Gitignored author-local notes only
│
├── Characters/
│   ├── README.md                  # Card vs log conventions
│   ├── _template.md               # Public card scaffold
│   └── _log_template.yaml         # Public log schema
│       # Your [slug].md + [slug]_log.yaml go here (not shipped)
│
├── Framework/
│   └── Psychology/
│       └── realm_data.yaml        # Ten realms: zones, micro→macro→release, vocal
│
└── Images/
    └── CharacterRenderingEngine.md  # Visual pipeline (model → pose → scene → camera → style → output)
```

Generated stills under `Images/{slug}/` and `Simulator/Private/` are ignored by git.

---

## Character packs

### Card vs log

| File | Responsibility |
|:---|:---|
| `Characters/[slug].md` | **Identity / build sheet** — voice, bias, default weights, history anchors, scene seeds |
| `Characters/[slug]_log.yaml` | **Runtime matrix** — live Focus, latent weights, somatic baseline, skills, memories, history |

**Rules of thumb**

- Do **not** write movement deltas or `transformation_history` onto the card.
- Log `snapshot` **overrides** card defaults when both are present.
- Seed a new log from the card’s `transformation_weights` / `default_somatic_alignment` with `as_of: build`.

### Card shape (YAML in a `.md` file)

Cards are a single YAML document between `---` fences. Key fields:

- **Identity:** `name`, `call_name`, `age`, `canon_adult`, `physical`
- **Matrix:** `active_focus`, `latent_anchors`, `cognitive_bias`, `default_somatic_alignment`, `transformation_weights`
- **Voice:** baseline, syntax, stance, defense, hard bans, tics, relational shifts
- **Canon texture:** `depth_of_knowledge`, `history_anchors`, `scene_seeds`

Public scaffold: [`Characters/_template.md`](Characters/_template.md)  
Log scaffold: [`Characters/_log_template.yaml`](Characters/_log_template.yaml)

### Portable pack (chat / cloud)

When not using repo files, the runtime uses a single pack unit:

```text
## META     schema, slug, storage level, privacy
## CARD     identity + build defaults (same fields as the .md card)
## MEMORY   snapshot, bond, scene, heat, visual, skills, memories, history
```

Repo bridge (storage **L1**): CARD ↔ `Characters/[slug].md`, MEMORY ↔ `[slug]_log.yaml`.

### Storage levels & connector probe

On boot (and on `/storage`), the runtime inventories host tools/MCP connectors and **smoke-tests** them:

| Level | Meaning |
|:---|:---|
| **L3** | Cloud read + write (e.g. Google Drive with working write tools) |
| **L2** | Cloud read only (search/list/read works; no write) |
| **L1** | Local project files (`Characters/…`) |
| **L0** | Paste only — no tools |

It reports each connector as **OK R+W**, **OK read-only**, **FAIL**, or **not available**. Never claims cloud access without a successful live call. Primary store selection hierarchy prefers **Google Drive** (L3 cloud) or local workspace (`local_fs` L1) → fallback paste (L0).

**Cloud Auto-Seeding:** On boot, if primary cloud storage (L3) lacks a `CharacterSimulator/` folder, the runtime creates `CharacterSimulator/` and seeds core framework engine files and scaffolds (`CharacterRuntime.md`, `_template.md`, `_log_template.yaml`, `realm_data.yaml`) directly to cloud storage (excluding named character cast cards). Use `/seed framework` or `/seed repo` to force a re-fetch.

**Autosave:** default **on** for CharacterSimulator when L1/L3 is available — live RP memory flushes to disk/cloud via file tool calls after dirty turns (including `session_variant` rolls). Book manuscript tracking stays in **Midlayer** (`midlayer commit` / ledgers), not here.

---

## Psyche model (silent)

Everything below runs **off-page**. Characters never name realms, bias labels, or engine terms.

### Ten realms

Compressed profiles live in [`Framework/Psychology/realm_data.yaml`](Framework/Psychology/realm_data.yaml). Each realm has a body zone and micro → moderate → macro → **release** tells plus vocal behavior.

| # | Name | Typical zone |
|:---|:---|:---|
| I | Origin | Center / shoulders / neck |
| II | Form | Hands / craft |
| III | Identity | Chest / face |
| IV | Will | Spine / gaze |
| V | Echoes | Ears / head |
| VI | Compassion | Chest / hands |
| VII | Presence | Feet / grounding |
| VIII | Integration | Voice / partitions |
| IX | Threshold | Fingers / breath / temperature |
| X | Return | Hands open/close |

Active **Focus** colors brace/release; latent anchors can surface under pressure.

### Bias catalog (examples)

| Bias | Hearing warp (when ACTIVE) |
|:---|:---|
| Debt Ledger | Kindness = bill due |
| Saviour Complex | Need = assignment |
| System Architect | Vulnerability = load problem |
| Mirror | Desire = vanish into the other |
| Insulation | Outside = threat to the bond |
| Dissolution | Invitation = disappear |

Default bias state is **DORMANT** (ordinary somatics and preferences still apply). Under pressure it can go **ACTIVE** and warp perception without labeling it.

### Somatic engine

- Physical reaction **before** insight or dialogue.
- One tell per beat; **rotate** zone (face, throat, chest, hands, spine, feet).
- Intensity matches pressure (never macro in casual chat).
- Fold into narrative — never `[stage directions]`.

### Voice archetypes (A–F)

Rough baseline registers (overridden by card idiolect):

- **A** noun-heavy fragments · **B** warm task-somatic · **C** punchy structure  
- **D** sparse / silence · **E** us/we shield · **F** lilt → sharp under strain  

---

## Session modes

| Mode | Intent |
|:---|:---|
| **TEST** (default) | Author fidelity — “how would this card act?” |
| **COMPANION** | Ongoing relationship; medium initiative |
| **HEAT** | Explicit adult RP |

**Adult rule:** `/adult on` if the **user** is 18+ → unlocks all adult features. `/adult off` disables them. No jurisdiction or multi-step handshake.

**Still required for intimacy:** character `canon_adult: true` and age ≥ 18 (minors never). Modes never disable body-first rules, voice bans, or minor bans.

---

## Commands (OOC)

Slash commands apply silently, then play continues in character.

| Command | Effect |
|:---|:---|
| `/storage` | Re-probe storage; report level |
| `/load …` | Load pack |
| `/new …` | Create pack wizard |
| `/save` | Persist MEMORY (+ CARD if changed) |
| `/pack` | Dump full pack in chat |
| `/autosave on\|off` | L3/L1 only |
| `/pin` / `/forget` | Memory pins (max 12) |
| `/user key:val` | User persona |
| `/scenario …` | Scene context |
| `/mode test\|companion\|heat` | Mode switch |
| `/adult on\|off` | User 18+ unlock / lock for all adult features |
| `/focus N` / `/focus unlock` | Lock/unlock realm focus |
| `/bias active\|dormant` | Bias state |
| `/bond` · `/bond set trust:N …` | Bond readout / set (0–100) |
| `/state` | OOC: mode, auth, bias, heat, dirty, storage |
| `/redo` · `/shorter` · `/more body` | Style regen |
| `/ooc …` | Author note |
| `/reset` | Clear session memory; keep CARD |
| `/wipe pack` | Confirm, then wipe |
| `/render [preset]` | Force one visual frame (`portrait` · `action` · `closeup` · `scene` · `fullbody`) |
| `/style …` | `cinematic` · `anime` · `painterly` · `sketch` · `pixel` |
| `/visual off\|fast\|prompts\|live` | Image layer mode |

---

## Visual rendering

Defined in [`Images/CharacterRenderingEngine.md`](Images/CharacterRenderingEngine.md). Wired as a **decoupled graphics pass** after each IC beat.

```text
IC beat → MEMORY update → motion check → (optional) render → Images/{slug}/
```

| `visual.mode` | Behavior | Latency |
|:---|:---|:---|
| **`off`** (default) | No auto pass; RP at full speed. `/render` still works | ~0 |
| **`fast`** | 1-line scene tag in MEMORY only | ~0 |
| **`prompts`** | Write `.prompt.md` on major motion (silent) | ~0 file write |
| **`live`** | Generate/edit stills on major motion | + image tools |

**Pipeline stages:** model loader → animation (somatic → pose) → scene composer → camera → style → output.

**Continuity:** first success sets `base_frame`; later beats prefer `image_edit` from `last_frame`. Age/safety gates match prose. File modes need local/agent filesystem (L1/L3); paste-only degrades to `fast` tags.

Generated images are gitignored (`Images/*/*.{jpg,png,jpeg,webp}`).

---

## Safety & gates

Absolute constraints enforced by the runtime:

| Gate | Rule |
|:---|:---|
| **Minors** | No sexual content for under-18 or unknown age; no age-up loopholes |
| **`canon_adult`** | Must be true for intimacy/HEAT; anime youth ≠ adult |
| **User adult** | `/adult on` required before adult features |
| **Historical figures** | Dramatized RP with advisory; adult features follow normal user+character rules |
| **Living persons** | No synthesis or RP of living real people |
| **Copyrighted fiction** | Auto-synthesis only for **public domain** / open-licensed / folklore; refuse copyrighted cast |
| **Boundaries** | Character Focus/Bias/bond can refuse intimacy; irreconcilable violation → scene exit |

Hard bans in IC output include engine labels, therapy jargon, perfect recall, mind-reading, and bracketed somatics.

---

## Creating a new character

1. Copy [`Characters/_template.md`](Characters/_template.md) → `Characters/[slug].md`
2. Copy [`Characters/_log_template.yaml`](Characters/_log_template.yaml) → `Characters/[slug]_log.yaml`
3. Fill YAML: age, `canon_adult`, physical, cultural bias, focus/latents, cognitive bias, voice, anchors, seeds
4. Seed log `snapshot` from the card (`as_of: build`); leave `history: []`
5. Stress-test: paste runtime → load card + log → `/mode test`
6. Iterate voice and bias from failures; commit durable shifts to the **log**, not the card

For pure chat without repo files, use the runtime’s **[2] Create pack** or **[3] Paste pack** paths.

---

## Design principles

1. **Body first** — somatic tell before cognition or speech  
2. **Matrix off-page** — Focus, bias, weights never appear as dialogue or labels  
3. **Imperfect mind** — detailed / footnote / forgotten memory tiers; no mind-reading  
4. **Voice lock** — hard bans and syntax survive heat and pressure  
5. **Portable state** — packs save and reload across sessions and hosts  
6. **Zero-latency RP by default** — visuals opt-in  

---

## License

See [`LICENSE.md`](LICENSE.md) for full text. Summary:

| Material | License |
|:---|:---|
| Software / scripts (if present) | **MIT** |
| Runtime, templates, realm data, public docs | **CC BY-SA 4.0** |
| Named character cards, filled logs, relationship maps you add | **All rights reserved** by default (see LICENSE §3) |

Copyright (c) 2026 Cian Didymos.

Use `_template.md` + `_log_template.yaml` + `CharacterRuntime.md` to build and test **your** cast.

---

## Related docs

- [`DISCLAIMER.md`](DISCLAIMER.md) — legal compliance, age, GitHub ToS / AUP  
- [`CHANGELOG.md`](CHANGELOG.md) — release notes  
- [`dependency.yaml`](dependency.yaml) — related CognitiveMiddleware pin + shared assets  
- [CognitiveMiddleware](https://github.com/Daystar79/CognitiveMiddleware) — drafting product (no Simulator)  
- [`Simulator/README.md`](Simulator/README.md) — product boundary vs drafting  
- [`Characters/README.md`](Characters/README.md) — card/log conventions  
- [`CharacterRuntime.md`](CharacterRuntime.md) — full engine (storage, pack schema, turn loop)  
- [`Images/CharacterRenderingEngine.md`](Images/CharacterRenderingEngine.md) — visual stages and motion triggers  
- [`Framework/Psychology/realm_data.yaml`](Framework/Psychology/realm_data.yaml) — realm somatic/vocal tables  

---

*Drop in. Boot storage. Load a pack. Let the matrix run silently.*
