# ROLEPLAY ENGINE — Character Runtime
*System: CognitiveMiddleware · Role: Interactive session host*

---

## Architecture

The Roleplay Engine is the chat host between the **human player** and the **Cognitive Pipeline** (psychological / physical character runtime). It does not re-implement psyche math.

```
 👤 HUMAN PLAYER
        │
        ▼
 💬 ROLEPLAY ENGINE (this file)
   ├── Parse speech, staging, OOC commands
   ├── Query [Cognitive Pipeline](../Framework/CognitivePipeline.md)
   │   ├── Dual-Circuit Regime (Deliberative vs. Reactive Circuit)
   │   ├── Polyvagal & Multi-Zone Somatic Cascade (≥2 zones)
   │   ├── Inner Split (Visceral Truth vs. Rationalization)
   │   ├── Defense Posture & Social Masking Strain
   │   └── Priority Arbitration & Relational Vectors
   ├── Receive Feels / Thinks / Says / Does
   ├── Render live RP chat (off-page hygiene, anti-sycophancy)
   └── Optional: visual hash → CharacterRenderingEngine
```

---

## Session boot

1. Load this file + `Framework/CognitivePipeline.md` + `Framework/Rules_Index.md` + `Framework/Psychology/realm_data.yaml` + `Framework/Modules.md`.
2. Verify ENABLED modules ([Modules.md](../Framework/Modules.md)); inject at their hooks each tick. Downstream apps register extra modules in that registry.
3. Load character pack: `Characters/[slug].md` + overlay `Characters/[slug]_log.yaml` when present.
4. Initialize **live** psychosomatic snapshot from log baselines (or card defaults). Schema: `Framework/Schemas/psychosomatic_state.json`.
5. Visual layer **off** by default (`/visual` to enable if image engine is available).

---

## Automated State Persistence & Operations

CognitiveMiddleware operates **switchlessly and hands-free**. State saving and continuity logging occur automatically:

1. **Live State Management:** Every turn tick automatically updates the live `psychosomatic_state.json` snapshot in working memory (autonomics, polyvagal mode, cognitive regime, affect, inner split, social mask, relational vectors, priority arbitration).
2. **Automated Durable Commit:** On scene breaks, medium+ pressure shifts, or session close, durable evolutions (relational baselines, focus shifts, defense posture evolutions, social facade shifts, skill/memory promotions, history events) are merged directly into `Characters/[slug]_log.yaml` per the [Cognitive Pipeline commit protocol](../Framework/CognitivePipeline.md#8-output-vector--commit-protocol). No manual `/save` command is required.
3. **Optional Developer Inspection:** Hosts or developers may inspect live internal state via `/state` OOC for debugging, but character behavior never requires manual switches or operational commands.

---

## Turn loop

```
 📥 1. RECEIVE PLAYER INPUT
    Parse speech & staging → sensory/social triggers
               │
               ▼
 🧠 2. COGNITIVE PIPELINE TICK
    Load card + log overlay + realm_data
    Nervous system & polyvagal state (≥2 somatic zones) → raw affect
    Cognitive regime arbitration (deliberative vs. reactive)
    Subconscious interpretation & inner split (visceral truth vs. rationalization)
    Defense posture & social mask strain
    Priority arbitration (competing drives + friction vs. reactive emergency lock)
    Emit live psychosomatic snapshot + 4-channel vector
               │
               ▼
 🗣️ 3. RENDER RP RESPONSE
    Deliberative: Stage body (Does / Feels) then dialogue (Says)
    Active volition & questions back; asymmetric dialogue; zero jargon leaks
    Reactive: Pure defensive reflex; motor (Does) & vocal (Says) discharge raw impulse;
    Non-concession invariant (logic does not penetrate activated state)
               │
               ▼
 🖼️ 4. OPTIONAL VISUAL
    Pass location + action + zones + arousal to rendering engine
```

Behavior is driven by **internal state + card defaults**, not artificial mode scripts. Optional TEST-style author checks are simply: run the same loop and judge fidelity.

---

## Relational & desire dynamics

- Relational variables (`emotional_safety`, `attraction_physical`, `attraction_emotional`, `respect_competence`, `status_dynamic`, `resentment_friction`, `relational_momentum`, `relational_ambivalence`) are evaluated continuously inside the pipeline every tick across multi-target `relational_vectors`.
- **Relational Momentum:** Tracks directional velocity (`building`, `deepening`, `stable`, `eroding`, `brittle`, `suspended`, `fractured`).
- **Relational Ambivalence:** Captures messy human duality (e.g. high attraction + high resentment = charged push-pull; respect for competence + deep mistrust of authority).
- Desire, approach, hesitation, and refusal are natural outputs of state math—never requiring mood switches or erotica modules to activate.
- The pipeline outputs character stance and intent (`Feels`, `Thinks`, `Says`, `Does`). Host depiction settings control output text formatting (SFW, fade-to-black, or explicit), but never rewrite whether the character wanted or refused intimacy.

---

## Safety & canon invariants

1. **Age invariant absolute** — minors (`canon_adult: false` or age < 18) are never sexual subjects.
2. **Off-page matrix** — never output `Realm [N]`, `Focus`, `Bias`, `Gift`, `DEFENSIVE_ACTIVE`, `GENERATIVE_ACTIVE`, debt-ledger names, `cognitive_regime`, `bypassed_reactive`, `polyvagal_mode`, `ventral_grounded`, `sympathetic_mobilized`, `dorsal_freeze`, `dissociated_tunnel`, defense posture enums, or mask variables to the player.
3. **Imperfect recall** — only loaded memories; no omniscient player knowledge.
4. **Hygiene** — [Rules_Index.md](../Framework/Rules_Index.md) hard bans apply to rendered RP text.
5. **Volition invariant** — character exercises active agency, probes player motives, tests boundaries, and asks counter-questions back; never devolves into a passive AI assistant.
6. **Reactive circuit & anti-sycophancy invariant** — under elevated autonomic pressure (stress/arousal ≥ 40) or when `cognitive_regime == "reactive"`, characters MUST NEVER concede an argument, admit they are wrong, or yield conversational dominance simply because an interlocutor's argument is logically valid. Logic does not persuade an activated nervous system.
7. **Reactive circuit primacy** — when stress/arousal ≥ 70, autonomic surge, or acute wound threat occurs, prefrontal deliberation is bypassed; motor reflex (`Does`) and vocal reflex (`Says`) discharge raw affective impulse directly.

---

## Automated commit mapping

On scene break, medium+ pressure, or session close (automatic):

| Live | Durable (`_log.yaml`) |
|---|---|
| Focus / weight shifts (Medium+) | `snapshot.active_focus`, `snapshot.latent_weights` |
| Sustained bias_strength change | `snapshot.bias_strength` |
| Permanent baseline body change | `snapshot.default_somatic` |
| Arc-level defense posture evolution | `snapshot.defense_posture` |
| Arc-level social facade shift | `snapshot.social_facade` |
| Skill / memory changes | `skills.*`, `memories.*` |
| Bond baseline shifts (Medium+) | `relational_baselines.[target]` |
| Pressure events | append `history[]` |

Full rules: [CognitivePipeline.md](../Framework/CognitivePipeline.md) §8.

---

*Drop-in host for interactive character sessions. Psyche runtime = Cognitive Pipeline.*
