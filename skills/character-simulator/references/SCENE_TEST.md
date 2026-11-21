# Scene testing workflow

Purpose: Evaluate how an **already loaded** character responds to a scene, then optionally adapt the result for a short skit. The simulation and adaptation are separate outputs.

## Inputs
- Character card or pack (required); optionally the latest durable log and relationships
- Scenario: setting, participants, trigger, what each participant knows
- Constraints: scene continuity, stakes, tone, optional video length
- Test intent: fidelity, variation, escalation, or short-form adaptation

If no card is available, ask for one or offer to build one. Never present a guessed character as a canonical simulation.

## Procedure
1. Load the card + log `snapshot` as the identity-first anchor, bound active memory to the last 2 hours (or the current test beat), and establish the live snapshot. Only surface `memories.detailed` / `footnote` entries cued by the test scene. Identify missing context explicitly.
2. For each proposed stimulus, run the CharacterRuntime turn loop and CognitivePipeline. Enforce `voice.hard_bans`, epistemic boundaries, volition, somatic ordering, anti-echoing, anti-therapy-speak, and defensive responses.
3. Produce one **baseline reaction**. For alternatives, branch from the **same initial state** and vary only the declared input (caller phrasing, stakes, interruptions, etc.). Do not pretend the alternatives are sequential turns.
4. Mark the resulting character behavior as **simulation**; identify assumptions, missing card facts and confidence limits. Avoid revealing private internal state as in-character dialogue.
5. If requested, produce a **skit adaptation** optimized for the user's specified runtime. Label all condensed/rephrased dialogue as editorial adaptation, not literal simulation.
6. When choosing between candidates, evaluate character fidelity first, then clarity, opening hook, pacing and timing. A funny line that violates the card is a rejected test, not a success.
7. Commit changes only for the selected canonical continuation; discarded branches must not mutate the durable log. If persistence tools are unavailable, offer an exportable updated state.

## Suggested output
- **Setup:** card/version, loaded state, scene and assumptions
- **Baseline:** action and dialogue
- **Variants:** only if requested; show what changed in each stimulus
- **Fidelity notes:** what is grounded in the card vs inferred
- **Skit cut:** optional, clearly labeled and timed approximately

Do not invent view-through rates, video-generation outcomes, or exact timing from unperformed tests.
