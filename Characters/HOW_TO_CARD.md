# How to Make a Character Card

You do **not** need to write raw YAML by hand. The recommended path is guided creation directly in chat.

---

## 🚀 Recommended: Guided Create (Full Card)

1. Copy and paste [`CharacterRuntime.md`](../CharacterRuntime.md) into any LLM chat.
2. Select **[2] Create a character** (or type `create` / `build a character`).
3. Answer the plain-language questions step by step:

| Step | You Provide | Lands on Card as |
|:---|:---|:---|
| 1. Name | Full name & call-name | `name`, `call_name` |
| 2. Age | Integer age | `age`, `canon_adult` |
| 3. Look | Physical appearance & motion line | `physical` |
| 4. Voice | Sound archetype & hard bans | `voice` block & `hard_bans` |
| 5. Wound / Bias | What they get wrong (plain English) | `cognitive_bias`, focus, somatics |
| 6. **History & Knowledge** | 2–3 anchors, general/esoteric/personal depth | **`history_anchors`**, **`depth_of_knowledge`** |
| 7. Opening | Place + pressure + object | `scene_seeds` |
| 8. Adult Limits | Intimacy limits (if adult RP intended) | Voice bans / card notes |

4. The runtime engine maps framework fields off-page and outputs a complete YAML card.
5. Select **Play now**, **Tweak**, or **Show pack** to export.

---

## 💡 Why History & Knowledge Matter

To keep character responses grounded without inventing biography or possessing omniscient knowledge, two core sections are required:

* **`history_anchors`:** 2–3 coarse past facts. Remained vague in speech until triggered by props, topics, or pressure.
* **`depth_of_knowledge`:** Defines what the character knows (`general`, `esoteric`) versus what is foggy or unexamined (`personal`).

---

## 🛠️ Hand-Editing Files (Power Users)

For manual creation or author editing:

1. Copy [`_template.md`](./_template.md) → `Characters/[slug].md`.
2. Copy [`_log_template.yaml`](./_log_template.yaml) → `Characters/[slug]_log.yaml`.
3. Fill identity, voice, `history_anchors`, `depth_of_knowledge`, and psyche fields.
4. Load the pack in runtime mode **TEST** to stress-test identity fidelity.

| File | Role |
|:---|:---|
| `Characters/[slug].md` | Permanent Identity (voice, bias, history anchors, knowledge depth) |
| `Characters/[slug]_log.yaml` | Runtime State (snapshot, memories, skills, durable history) |
