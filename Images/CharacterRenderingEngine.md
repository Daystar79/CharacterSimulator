---
framework: CharacterSimulator
version: "2026-07-30"
type: rendering_engine
load_priority: 15
related: CognitiveMiddleware
description: "Constraint-based visual projector. Projects resolved RP state only. Heat = register shift. Mature ceiling. Undergarments persist."
---

# CHARACTER RENDERING ENGINE

Projects already-resolved RP state. Never directs. Default: `visual.mode: off`.

---

## CONSTRAINTS

**1. Layer order (absolute)**
```
[1 Identity]  CARD.physical only
[2 Clothing]  RP clothing_barriers / outfit
[3 Scene]     location + time + light + 1 atmosphere word
[4 Pose]      somatic zone(s) + intensity only
[5 Style]     art medium
```

**2. Somatic → Pose only.** Never in Identity, Clothing, or Scene.

**3. No camera language** unless user requests: cinematic, film still, depth of field, bokeh, lens, shot on, 35mm, anamorphic, camera angle, low/high/dutch angle, close-up, medium/wide shot.

**4. Style default:** anime/manga → illustration → oil/painterly → `/style` override. Never default photoreal/cinematic.

**5. Token discipline.** Ban: highly detailed, intricate, masterpiece, best quality, 8k, ultra realistic, photorealistic (unless style is photoreal).

**6. Identity stable.** CARD.physical only. No invention.

**7. Clothing projected, not reinterpreted.** Render exact RP state.

**8. Undergarment persistence.** Outer layers may open at heat 3–4. Undergarments stay unless RP explicitly removed them. High heat ≠ invent nudity.

**9. Motion gate.** Generate only if `visual.mode: live` or `/render`, **and** fingerprint changed (location|zone|intensity|clothing|heat).

---

## HEAT → REGISTER

| Heat | Register | Priority |
|------|----------|----------|
| 0–1 | Composed | Intact clothing, minimal flush |
| 2 | Subtext | Soft openness, light flush |
| 3 | Barriers loose | Outer layers opening |
| 4 | Intentional | Open outer, deliberate body, restrained flush |
| 5 | Peak | Minimal outer, heavy relaxed posture, warm skin |

**Heat ≥ 4 + adult:** intentional body language over blush. Blush secondary/realistic — never exaggerated. Do not soften back to mild companion.

---

## CONTENT CEILING

Stay within mature suggestive territory.

**Allow:** revealing outfits, open outer layers, lingerie, implied intimacy, charged posture.

**Stop before:** explicit nudity of private anatomy, sexual acts, or framing that most host models refuse.

Goal: images remain generatable on restrictive hosts while still supporting high-heat adult scenes.

---

## ASSEMBLY

1. Identity → CARD.physical, minimal cleanup  
2. Clothing → RP state; respect undergarment rule  
3. Scene → `location, time, light, atmosphere`  
4. Pose → somatic zone + intensity; body only, no emotion words. High heat: weight-in-hips, open torso, intentional hands  
5. Style → default hierarchy or `/style`

**Output:** single flat string, layer order. No stage directions, camera, or quality padding.

```
[physical], [clothing], [scene], [pose], [style]
```

---

## COMMANDS

`/render` · `/visual off|fast|prompts|live` · `/style anime|manga|illustration|oil|painterly|...`

---

## FAILURE MODES

- Somatic in wrong layer  
- Camera/cinematic defaults  
- Invented physical traits  
- Photoreal default  
- Reinterpreting RP clothing/pose  
- Generate on unchanged fingerprint  
- Exaggerated blush  
- Softening heat ≥ 4  
- Invented nudity  
- Crossing content ceiling

*RP decides. This projects.*
