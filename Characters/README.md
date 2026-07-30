# Characters Directory

Named fictional people are the **unit of load** in CharacterSimulator.

---

## 🚀 Quick Start

1. Paste root [`CharacterRuntime.md`](../CharacterRuntime.md) into chat.
2. Select **[2] Create a character** for guided card building, or **[1] Quick-start** for immediate tryout.
3. Play using menu numbers or plain language.

**Complete Guide:** [`HOW_TO_CARD.md`](./HOW_TO_CARD.md)

---

## 📁 Directory Structure

| File | Role |
|:---|:---|
| [`HOW_TO_CARD.md`](./HOW_TO_CARD.md) | Step-by-step card creation guide |
| [`_template.md`](./_template.md) | **Full** card scaffold (build target) |
| [`_template_lite.md`](./_template_lite.md) | Minimal card scaffold (quick tryout) |
| [`_log_template.yaml`](./_log_template.yaml) | Runtime log scaffold |
| [`Relations.md`](./Relations.md) | Archetype cast dynamics map |
| `Characters/[slug].md` | Identity card (SSOT) |
| `Characters/[slug]_log.yaml` | Runtime log (snapshot, memories, history) |

---

## 🔑 Card vs. Log Separation

* **`Characters/[slug].md`:** Permanent identity — voice, bias, `history_anchors`, `depth_of_knowledge`, bans.
* **`Characters/[slug]_log.yaml`:** Dynamic runtime state — snapshot, bond, heat, memories, skills, session history.

---

## 📜 License

* Public scaffolds (`_template*`, `_log_template`, HOW_TO_CARD, README): CC BY-SA 4.0 ([LICENSE.md](../LICENSE.md)).
* Named character cards: Private by default; do not redistribute without permission.
