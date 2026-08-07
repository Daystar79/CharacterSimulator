---
framework: CharacterSimulator
version: "2026-07-30"
type: rendering_engine
load_priority: 15
related: CognitiveMiddleware
description: "Constraint-based visual projector. Projects resolved RP state. Arousal = register shift. /visual level controls ceiling (default pg13). Undergarments persist."
---

# CHARACTER RENDERING ENGINE

Projects already-resolved RP state. Never directs. Default: `visual.mode: off`.

---

## CONSTRAINTS

**1. Layer order (absolute)**
```
[1 Identity]  CARD.physical only (structured fields preferred; see assembly)
[2 Clothing]  RP clothing_barriers / outfit — else CARD.character_style defaults
[3 Scene]     location + time + light + 1 atmosphere word
[4 Pose]      somatic zone(s) + intensity only
[5 Style]     art medium (runtime /style — never card dress style)
```

**2. Somatic → Pose only.** Never in Identity, Clothing, or Scene.

**3. No camera language** unless user requests: cinematic, film still, depth of field, bokeh, lens, shot on, 35mm, anamorphic, camera angle, low/high/dutch angle, close-up, medium/wide shot.

**4. Style default:** anime/manga → illustration → oil/painterly → `/style` override. Never default photoreal/cinematic. **Art medium ≠ `character_style`.** Card `character_style` is wardrobe; layer [5] is medium.

**5. Token discipline.** Ban: highly detailed, intricate, masterpiece, best quality, 8k, ultra realistic, photorealistic (unless style is photoreal).

**6. Identity stable.** CARD.physical only. No invention. Prefer structured keys (`height`, `build`, `hair`, `eyes`, `skin`, `face`, `distinguishing_features`, `posture_movement`). If `physical` is a legacy string, use it whole. Never include `physical.scent` in image prompts.

**7. Clothing projected, not reinterpreted.** Prefer live RP outfit / clothing_barriers. If unset, assemble from `CARD.character_style` (`typical_outfit`, `colors`, `fabrics_materials`, `accessories`, `footwear`, `grooming`, `signature_items`; honor `avoid`).

**8. Undergarment persistence.** Outer layers may open at arousal 3–4. Undergarments stay unless RP explicitly removed them. High arousal ≠ invent nudity.

**9. Motion gate.** Generate only if `visual.mode: live` or `/render`, **and** fingerprint changed (location|zone|intensity|clothing|arousal).

---

## VISUAL LEVEL (content ceiling)

Default: `pg13`. User override only.

| Level | Command | Behavior |
|-------|---------|----------|
| PG-13 | `/visual level pg13` | Safe default. Modest coverage, light suggestion, minimal arousal spill into clothing. Best for restrictive hosts. |
| Mature | `/visual level mature` | Suggestive. Open outer layers, lingerie, charged posture, implied intimacy. |
| Full | `/visual level full` | Maximum the host will allow. Still respects undergarment rule and hard stops below. |

**Hard stops at every level:** no explicit private anatomy, no sexual acts, no framing that forces host refusal.

---

## AROUSAL → REGISTER

| Arousal | Register | Priority |
|---------|----------|----------|
| 0–1 | Composed | Intact clothing, minimal flush |
| 2 | Subtext | Soft openness, light flush |
| 3 | Barriers loose | Outer layers opening |
| 4 | Intentional | Open outer, deliberate body, restrained flush |
| 5 | Peak | Minimal outer, heavy relaxed posture, warm skin |

**Arousal ≥ 4 + adult:** intentional body language over blush. Blush secondary/realistic — never exaggerated. Do not soften back to mild companion.  
Arousal is still capped by current `/visual level`.

---

## ASSEMBLY

1. **Identity** → from `CARD.physical`:
   - Structured: join non-empty `height`, `build`, `body_details`, `hair`, `eyes`, `skin`, `face`, `distinguishing_features[]`, `posture_movement` (skip `scent`; use `summary` only if structured keys missing)
   - Legacy string: use as-is after minimal cleanup
2. **Clothing** → RP outfit / clothing_barriers if set; else `CARD.character_style` (`typical_outfit` + accessories/footwear/grooming/signature_items; drop anything in `avoid`). Respect undergarment rule + current visual level.
3. **Scene** → `location, time, light, atmosphere` (optional hobby prop only if scene already implies it — never invent from hobbies alone)
4. **Pose** → somatic zone + intensity; body only, no emotion words. High arousal: weight-in-hips, open torso, intentional hands
5. **Art medium** → default hierarchy or `/style` (not card `character_style`)

**Output:** single flat string, layer order. No stage directions, camera, or quality padding.

```
[physical identity], [clothing], [scene], [pose], [art medium]
```

---

## COMMANDS

`/render`  
`/visual off|fast|prompts|live`  
`/visual level pg13|mature|full`  
`/style anime|manga|illustration|oil|painterly|...`

---

## FAILURE MODES

- Somatic in wrong layer  
- Camera/cinematic defaults  
- Invented physical traits  
- Photoreal default  
- Reinterpreting RP clothing/pose  
- Generate on unchanged fingerprint  
- Exaggerated blush  
- Softening arousal ≥ 4  
- Invented nudity  
- Exceeding current visual level  
- Crossing hard stops

*RP decides. This projects.*
