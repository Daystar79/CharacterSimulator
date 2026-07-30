---
framework: CharacterSimulator
version: "2026-07-29"
type: rendering_engine
load_priority: 15
related: CognitiveMiddleware
description: "Visual rendering pipeline for CharacterSimulator CharacterRuntime. Off by default for zero RP latency; supports fast 1-line tags, prompt writing, and live image generation when enabled."
---

# CHARACTER RENDERING ENGINE

Convert CharacterRuntime state into visual frames on demand or on scene motion.  
**Default:** `visual.mode: off` (0 RP latency).  
**Enable via:** `/visual off|fast|prompts|live` or trigger on-demand via `/render`.

---

## ⚡ WORKFLOW & ARCHITECTURE

```text
CharacterRuntime IC beat → MEMORY update (scene, somatic, action)
  → Motion Fingerprint Check (location, time, zone, action, heat)
  → Rendering Pipeline (Stages 1–6)
  → Image Generation (base_frame or delta edit from last_frame)
  → Save still to Images/{slug}/ → Clean up temporary .prompt.md → Update MEMORY.visual
```

### Pipeline Stages
1. **Model Loader:** Construct base geometry from CARD (`physical`, `age`, `cultural_bias`).
2. **Animation System:** Map somatic zone & intensity to pose/expression.
3. **Scene Composer:** Convert `MEMORY.scene` & `scene_seeds` to lighting, time, atmosphere.
4. **Camera System:** Determine shot type (Medium/Close-up/Wide/Extreme) & angle based on narrative mood.
5. **Material & Shader:** Apply art style (`visual.style`: cinematic, anime, painterly, sketch, pixel).
6. **Render Output:** Generate prompt & render still via `image_gen` or `image_edit` / `generate_image`.

---

## 🎭 ANIMATION & CAMERA MAPPING

### Somatic Zone to Visual Focus
| Zone | Visual Focus | Keywords |
|:---|:---|:---|
| **1: Face & Eyes** | Expressions, gaze, micro-expressions | `eyes`, `gaze`, `facial expression` |
| **2: Throat & Neck** | Neck tension, breathing, swallowing | `neck`, `throat`, `breathing` |
| **3: Chest & Breathing** | Chest movement, posture, breath | `chest`, `posture`, `shoulders` |
| **4: Hands & Arms** | Positioning, gestures, finger detail | `hands`, `gestures`, `arm position` |
| **5: Spine & Posture** | Body posture, stance, alignment | `spine`, `posture`, `body language` |
| **6: Feet & Staging** | Grounding, foot placement, distance | `stance`, `feet`, `grounding` |

### Framing by Context
| Context | Shot Type | Purpose |
|:---|:---|:---|
| Dialogue (casual) | Medium Shot (waist up) | Character posture + hand gestures |
| Dialogue (intense) | Close-up (chest up) | Facial expressions & micro-tells |
| Action / Staging | Wide Shot (full body) | Spatial movement & environment |
| Intimate / Somatic | Close-up / Extreme Close-up | Emotional details & specific body tells |

---

## 🔄 MOTION FINGERPRINTING & TRIGGERS

After every IC beat, calculate motion fingerprint:
```text
hash = location | time | somatic_zone | last_action | clothing_barriers | heat.level | active_focus
```

* **Fire when:** `hash != visual.last_hash` AND `visual.mode != off`, OR when `/render` is run.
* **Skip when:** `visual.mode: off`, OOC-only turn, or hash unchanged.

### Commands
- `/render [preset]` — Force immediate image frame (`portrait`, `action`, `closeup`, `scene`, `fullbody`).
- `/visual off` — **Default:** Disable auto pass (zero latency).
- `/visual fast` — Record 1-line scene tag in `MEMORY.visual.last_prompt`.
- `/visual prompts` — Write `.prompt.md` files to `Images/{slug}/` on motion beats.
- `/visual live` — Auto-pass + render stills on motion beats via image tools.
- `/style [preset]` — Set `visual.style` (`cinematic`, `anime`, `painterly`, `sketch`, `pixel`).

---

## 📷 LIVE IMAGE GENERATION & CONTINUITY

When `visual.mode: live` or `/render` executes:
1. **First Frame:** Call `image_gen` (or `generate_image`) with full physical appearance & scene prompt → save to `Images/{slug}/{timestamp}_{descriptor}.jpg` → set `base_frame` and `last_frame`.
2. **Subsequent Beats:** Call `image_edit` with `image: last_frame` and a delta-only prompt (pose, light, staging change) → save new image → update `last_frame`.
3. **Prompt Cleanup Rule:** Once the image file is written to `Images/{slug}/`, **automatically delete/unlink temporary `.prompt.md` files** to prevent disk clutter (prompts retained on disk only in `visual.mode: prompts`).
4. **Agent Constraint:** File writing and image generation execute strictly in local environments (L1/L3 storage). In paste-only (L0) environments, rendering degrades silently to `fast` in-memory tags.

---

*When the scene moves, the frame moves.*
