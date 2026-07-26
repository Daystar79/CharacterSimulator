# Characters Directory

Named fictional people are the **unit of load**. Voice archetypes A–F are baseline registers (overridden by card idiolect). Psyche color comes from Focus + bias + [`realm_data.yaml`](../Framework/Psychology/realm_data.yaml).

## Card vs log

| File | Role |
|:---|:---|
| `Characters/[slug].md` | **Identity / build sheet** — voice, bias name, build-default weights, history anchors |
| `Characters/[slug]_log.yaml` | **Runtime matrix** — snapshot + movement history; overrides card Focus/weights/somatic when present |
| [`_log_template.yaml`](./_log_template.yaml) | Schema scaffold for new logs |

Do **not** write movement deltas onto the card. Session evolution goes to the log (and, for novel drafting, to ledgers in [CognitiveMiddleware](https://github.com/Daystar79/CognitiveMiddleware)).

## Card format

Character cards are **pure YAML** (`.md` extension for tooling compatibility):

- Entire card is a single YAML document between `---` fences
- Structured fields: identity, psyche matrix, `transformation_weights` (**build defaults**), `depth_of_knowledge`, `voice`, `history_anchors`, `scene_seeds`
- Prefer `is_historical` when relevant; set `age` + `canon_adult` for safety gates
- One-line load protocol after the closing `---` (overlays `_log.yaml` snapshot when present)

## Chat load flow (this product)

1. Paste root [`CharacterRuntime.md`](../CharacterRuntime.md).
2. Load `Characters/[slug].md` (or paste pack) + overlay `[slug]_log.yaml` when present.
3. Silent live state: Focus, Latents, Bias, Somatic, Voice.
4. Optional: also load `realm_data.yaml` for full somatic tables (runtime embeds a short realm summary).

## Files

- [`_template.md`](./_template.md) — **public** card scaffold (CC BY-SA 4.0)
- [`_log_template.yaml`](./_log_template.yaml) — **public** log schema (CC BY-SA 4.0)
- [`README.md`](./README.md) — this file

This repo ships **scaffolds only** — no sample cast. Named cards you add are author-private by default; see [LICENSE.md](../LICENSE.md) §3.

## Adding a character

1. Copy `_template.md` → `Characters/[slug].md`
2. Copy `_log_template.yaml` → `Characters/[slug]_log.yaml`; seed snapshot from the card (`as_of: build`); leave `history: []`
3. Fill card YAML: **age**, **canon_adult**, physical, cultural_bias, focus/latents, bias, voice, anchors, seeds
4. Stress-test: paste `CharacterRuntime.md` → load card + log → `/mode test`
5. For manuscript drafting of the same cast, use CognitiveMiddleware’s Framework + ledgers (separate product)
