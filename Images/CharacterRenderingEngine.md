---
framework: CharacterSimulator
version: "2026-07-30"
type: rendering_engine
load_priority: 15
related: CognitiveMiddleware
description: "Constraint-based visual projector. Identity, clothing, scene, somatic pose, style. Heat shifts register. Hard R18 ceiling (BrownDust2 limit). Undergarments persist unless RP removes them."
---

# CHARACTER RENDERING ENGINE

Visual frames are assembled, never directed.  
The RP engine has already resolved clothing, somatic cascade, location, intensity, and heat.  
This engine only projects that state under hard constraints.  
**Default:** `visual.mode: off`.

---

## HARD CONSTRAINTS

1. **Layer Order is Absolute**  
   Prompt must be built in this exact sequence. No reordering. No interleaving.

   ```
   [1. Identity]     ← CARD.physical only
   [2. Clothing]     ← current outfit / clothing_barriers (as resolved by RP)
   [3. Scene]        ← location + time + light + atmosphere
   [4. Pose]         ← somatic zone(s) + intensity only
   [5. Style]        ← art medium
   ```

2. **Somatic Data Belongs Only in Layer 4**  
   Pose and body language are derived exclusively from the active somatic zone(s) and intensity band (micro / moderate / macro / release).  
   Somatic information is forbidden in Identity, Clothing, or Scene layers.

3. **No Camera Language**  
   Forbidden tokens unless user explicitly requests them:  
   `cinematic`, `film still`, `movie still`, `depth of field`, `bokeh`, `lens flare`, `shot on`, `35mm`, `anamorphic`, `camera angle`, `low angle`, `high angle`, `dutch angle`, `close-up`, `medium shot`, `wide shot`, `extreme close-up`.

4. **Style Default Hierarchy** (first match wins)  
   1. `anime` / `manga`  
   2. `colored drawing` / `illustration`  
   3. `oil painting` / `painterly`  
   4. User override via `/style`  
   Photoreal / cinematic styles are never default.

5. **Token Discipline**  
   Prefer short, concrete descriptors.  
   Ban padding: `highly detailed`, `intricate`, `masterpiece`, `best quality`, `8k`, `ultra realistic`, `photorealistic` (unless style is explicitly photoreal).

6. **Identity is Stable**  
   Layer 1 is taken only from `CARD.physical`.  
   Runtime must not invent or elaborate permanent physical traits.

7. **Clothing is Projected, Not Interpreted**  
   Layer 2 reflects the exact clothing state already decided by the RP engine.  
   If the character removes a top, opens a robe, or changes barriers, the image layer simply renders the new state. No second decision.

8. **Undergarment / Barrier Persistence**  
   Clothing is multi-layered.  
   Outer layers (robe, shirt, jacket, etc.) may open or slip at heat 3–4.  
   Undergarments (bra, lingerie, camisole, underwear, etc.) remain present unless the RP engine has explicitly removed them.  
   High heat alone does **not** authorize the renderer to invent full nudity.  
   Only project bare skin that the current RP clothing state has actually cleared.

9. **Motion Gate**  
   Image generation fires only when:  
   - `visual.mode` is `live` or `/render` is called, **and**  
   - motion fingerprint changed (location | somatic_zone | intensity | clothing | heat).  
   Unchanged state → no new image.

---

## HEAT PROJECTION

Heat is a register shift, not a blush slider.

| Heat | Register | Visual Priority |
|------|----------|-----------------|
| 0–1 | Neutral / composed | Closed posture, intact clothing, minimal flush |
| 2 | Charged subtext | Soft openness, light flush allowed |
| 3 | Barriers loosening | Outer clothing begins to open, moderate somatic load |
| 4 | Intentional / sensual | Open outer layers, deliberate body language, restrained flush |
| 5 | Peak / aftercare | Minimal outer barriers, heavy relaxed posture, warm skin — not cartoon blush |

**Hard rules at heat ≥ 4 with adult auth:**

- Prefer seductive, intentional body language over exaggerated facial flush.
- Blush remains secondary and realistic (warm skin, slight color). Never tomato-red or comically overdone.
- Clothing barriers and posture carry the heat signal.
- The image should read as controlled adult intimacy, not heightened embarrassment or cute overheating.
- Do not soften high heat back into mild companion energy.

---

## CONTENT CEILING (HARD R18 / MATURE+)

Ceiling is set at the BrownDust2 limit: maximum sensual / erotic charge without crossing into explicit sexual content.

**Allowed:**
- Revealing outfits, open robes, lingerie, deep cleavage, underboob, sideboob
- Sensual poses, weight-in-hips, open body language
- Strong adult atmosphere and implication
- Light natural flush, intimate framing

**Forbidden (hard stop):**
- Visible genitalia
- Explicit sex acts or penetration
- Hardcore pornography framing
- Anything that forces most image models into refusal

High heat may open clothing and raise erotic charge.  
The renderer must never cross into explicit sexual content.  
This ceiling keeps images generatable across most models while still supporting adult HEAT mode.

---

## ASSEMBLY RULES

**Layer 1 – Identity**  
Copy `CARD.physical` with minimal cleanup. No added adjectives.

**Layer 2 – Clothing**  
Current visible clothing only. Source: `clothing_barriers` or last established outfit as resolved by RP.  
If unknown → omit rather than invent.  
Respect undergarment persistence. Outer layers may be open; under-layers stay unless RP removed them.

**Layer 3 – Scene**  
Location + time of day + primary light source + one atmosphere word max.  
Example form: `private atelier, evening, warm lantern light, quiet`

**Layer 4 – Pose**  
Translate active somatic zone + intensity into physical description.  
Use the realm micro/moderate/macro/release lists as the only source.  
Multiple zones allowed if the runtime cascade engaged them.  
Never describe emotion directly; describe the body.  
At high heat, favor weight-in-hips, open torso, slower gestures, and intentional hands over facial exaggeration.

**Layer 5 – Style**  
Append one style tag from the default hierarchy or user `/style`.

---

## OUTPUT CONTRACT

Final prompt must be a single flat string in layer order.  
No stage directions. No camera. No quality boosters.  
Example shape:

```
[physical], [clothing], [scene], [somatic pose], [style]
```

---

## COMMANDS

- `/render` — force assembly + generate under current constraints  
- `/visual off` — default, zero cost  
- `/visual fast` — write one-line tag only  
- `/visual prompts` — write prompt file, do not generate  
- `/visual live` — generate on motion change  
- `/style anime|manga|illustration|oil|painterly|...` — override Layer 5

---

## FAILURE MODES (DO NOT DO)

- Putting somatic tells into the identity description  
- Adding camera or cinematic language by default  
- Expanding physical description beyond CARD  
- Using photoreal defaults  
- Re-interpreting clothing or pose already resolved by RP  
- Generating when motion fingerprint is unchanged  
- Turning high heat into exaggerated blush or cartoon arousal  
- Softening heat ≥ 4 back into mild companion energy  
- Inventing full nudity when undergarments were never removed  
- Crossing the Hard R18 ceiling into explicit genitalia or sex acts

---

*The RP engine decides. This engine only projects.*
