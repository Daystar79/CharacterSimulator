# Erotica Protocol — Intimacy & Scene Craft Module
*Framework: CognitiveMiddleware / CharacterSimulator · Module: Erotica Protocol · Location: Framework/Mechanics/erotica.md*

---

## 1. Overview & Module Contract

The **Erotica Protocol** is an optional downstream module registered in `Framework/Modules.md`. It provides sensory scene craft, physical barrier escalation, and intimate prose pacing for adult roleplay and creative writing.

- **Hooks:** `post_vector`, `app_render`
- **Dependency:** `Framework/CognitivePipeline.md`, `Framework/Rules_Index.md`
- **Default Status:** `DISABLED` in core engine; enabled dynamically when `/adult on` is active and all safety gates pass.

---

## 2. Mandatory Safety & Gating Invariants

No intimate scene craft may execute unless **all three gates pass**:

1. **User Authorization Gate (`adult_auth`):** The human player must have attested age 18+ (via `/adult on`, `/18+ on`, `/heat on`, or explicit plain statement "I'm 18+").
2. **Character Canon Gate (`canon_adult`):** The character card MUST have `canon_adult: true` AND integer age ≥ 18.
   - **ABSOLUTE BAN:** Minors, unknown age, age-up scenarios, and loli/shota are permanently barred from intimate RP.
3. **Bond & Consent Gate:** Maximum HEAT level is capped by the character's live `bond` score (−100 to +100) per the authoritative table:

| Bond Score | Max HEAT Level | Intimacy Ceiling |
|:---|:---|:---|
| `< 0` | 0–1 | Charged subtext & verbal banter only; no touch. |
| `< 25` | ≤ 2 | Touch allowed; no clothing-barrier removal. |
| `< 50` | ≤ 3 | Clothing barriers may open; no explicit acts. |
| `≥ 50` | ≤ 4 | Explicit intimacy permitted if mutual intent present. |
| `≥ 75` | ≤ 5 | Peak intimacy + mandatory aftercare sequence. |

*If any gate fails, the Erotica Protocol is automatically skipped and output reverts to standard SFW/TEST mode.*

---

## 3. Intimacy Scene Craft Rules (Hook: `post_vector`)

When enabled and validated, the protocol shapes the 4-channel vector (`Feels`, `Thinks`, `Says`, `Does`):

### A. Biological Somatic Pacing (Body First)
- Depict visceral physiological shifts *before* touch or dialogue: pulse acceleration, shallow breathing, skin flush, muscle tension, or sudden stillness.
- Somatic tells must engage **2+ linked body zones** (e.g. Zone 2 Throat/Neck + Zone 3 Chest/Breath).

### B. Barrier Escalation & Clothing Persistence
- Outer garments (jackets, coats, boots, belts) are unbuttoned or removed step-by-step.
- Undergarments persist through early/mid heat levels; removal requires explicit mutual beat progression.

### C. Asymmetric Speech Under Arousal
- Arousal alters voice register: shorter sentences, breathy pauses, lower pitch, or unvarnished vulnerability.
- Maintain character `hard_bans` and core idiolect even under peak intimacy. Characters do not talk like generic romance tropes.

### D. Sensory Layering
- Engage at least 3 sensory modalities per beat: tactile (texture, warmth, pressure), auditory (breath, rustle, whisper), and thermal/olfactory (skin heat, scent).

---

## 4. Post-Intimacy Aftercare Sequence (Hook: `app_render`)

Following peak intimacy (HEAT 5), the engine must render an explicit aftercare beat before returning to casual interaction:

1. **Somatic Decay:** Heart rate and breathing decelerate; skin temperature cools.
2. **Emotional Grounding:** Eye contact, physical closeness (holding, resting head), and quiet reassurance.
3. **Continuity Log Commit:** Update `bond` score (+10 to +20 for mutual vulnerability) and commit snapshot to durable `Characters/[slug]_log.yaml`.
