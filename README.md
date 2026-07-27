# CharacterSimulator
**A psychological simulation framework for AI characters that feel alive.**

[![License: MIT + CC BY-SA 4.0](https://img.shields.io/badge/license-MIT%20%2B%20CC%20BY--SA%204.0-blue.svg)](LICENSE.md)
[![Status: Active](https://img.shields.io/badge/status-active-green.svg)](CHANGELOG.md)

---

## 🎯 What Is CharacterSimulator?

CharacterSimulator is a **prompt-based runtime engine** that turns any LLM chat into a **psychologically complex character simulator**. It’s designed for **authors, roleplayers, and AI enthusiasts** who want characters that:
- **React physically before they speak** (somatic engine).
- **Remember, forget, and evolve** (imperfect memory).
- **Act on hidden biases and psychological profiles** (off-page matrix).
- **Stay true to their identity** (no drift, no improvisation).

**Think of it as a "character OS" for LLMs.**

---

## 🌟 Why Use This?

### Why Not Just Use [Character.AI/Replika/Etc.]?
   Feature               | Them                          | CharacterSimulator               |
 |-----------------------|-------------------------------|-----------------------------------|
 | **Psychological Depth** | Surface-level emotions       | **10 Realms + 6 Biases + Somatic Engine** |
 | **Portability**        | Locked into their platform    | **Works in *any* LLM chat** (paste + play) |
 | **Identity Control**  | Characters drift over time    | **CARD > MEMORY > Session (no drift)** |
 | **Safety**             | Varies                        | **Absolute gates (no minors, no real persons)** |
 | **Modularity**         | All-in-one                    | **Separate drafting (Midlayer) + RP (this repo)** |
 | **Visuals**           | Often coupled to chat         | **Decoupled (optional, zero-latency RP)** |

---

## 🚀 Quick Start

### Try It Now
1. **Copy** the contents of [`CharacterRuntime.md`](CharacterRuntime.md).
2. **Paste** it into any LLM chat (e.g., Mistral, Claude, or local models).
3. **Run** the chat. The runtime will:
   - Probe your storage (Google Drive, local files, etc.).
   - Show a **disclaimer** (required).
   - Ask you to **load or create a character**.
4. **Start chatting!** Your character will:
   - React **physically first** (e.g., hand on chest, jaw clench).
   - Speak in their **defined voice** (no OOC jargon).
   - **Remember** the session (if autosave is on).

**Example:**
> *User:* `/load elyra`
> *Elyra (Compassion bias):*
> *Her fingers tighten around the teacup (chest zone tell).*
> *"You’re back. I was starting to think you’d forgotten about me."*

---

## 🧠 Core Features

### 🔹 Psychological Simulation
- **Ten Realms**: Body zones (e.g., hands, chest, spine) with **brace/release profiles** for stress responses.
- **Bias Prism**: 6 cognitive biases (e.g., *Debt Ledger*, *Mirror*) that **warp perception** without labeling.
- **Somatic Engine**: **Physical tells before dialogue** (e.g., swallow, clenched fists) with **zone rotation** to avoid repetition.

### 🔹 Character Packs (Portable Identity)
- **`CARD`**: Identity SSOT (name, age, physical, voice, biases, hard bans).
- **`MEMORY`**: Runtime state (bond, scene, heat, skills, history).
- **Portable**: Save as `.md`/`.yaml` files or paste directly into chat.

### 🔹 Modes for Every Use Case
 | Mode       | Purpose                          | Initiative | Heat Friction          |
 |------------|----------------------------------|------------|------------------------|
 | **TEST**   | Author fidelity checks           | Low        | High (earned only)     |
 | **COMPANION** | Ongoing relationships          | Medium     | Medium (flirt OK)      |
 | **HEAT**   | Explicit adult RP                | High       | Ladder (0–5)           |

### 🔹 Safety & Ethics
- **Absolute Gates**:
  - ❌ No minors in adult content (ever).
  - ❌ No living real persons.
  - ❌ No copyrighted fiction auto-synthesis.
- **User Control**:
  - `/adult on` unlocks adult features (user attestation).
  - Character must have `canon_adult: true` + `age >= 18` for HEAT.

### 🔹 Storage & Autosave
- **L0–L3 Levels**:
  - **L3**: Cloud R+W (Google Drive, Dropbox).
  - **L2**: Cloud read-only.
  - **L1**: Local workspace (`Characters/[slug].md`).
  - **L0**: Paste-only.
- **Autosave**: Default **on** for L1/L3. Dirty state (e.g., bond changes) triggers automatic saves.

### 🔹 Visual Rendering (Optional)
- **Modes**: `off` (default), `fast`, `prompts`, `live`.
- **Triggers**: Major actions, scene changes, or `/render [preset]`.
- **Continuity**: Uses `base_frame` and `last_frame` for consistency.

---

## 🎭 Who Is This For?

### 📖 For Authors
- **Stress-test characters** before drafting.
- **Validate consistency**: "Would my character *actually* do this?"
- **Prototype arcs**: See how a character evolves over a session.

### 🎲 For Roleplayers
- **Deep, realistic RP** (not just "hot girl summer" bots).
- **Multi-character sessions** (load multiple packs).
- **Somatic immersion**: Characters react physically before speaking.

### 🤖 For AI Enthusiasts
- **Experiment with psychological models** in LLMs.
- **Custom biases/realms**: Extend the framework.
- **Research emergent behavior**: How do characters act under pressure?

---

## 🗺️ Roadmap

### 🚧 Current Focus
- **Stabilizing the runtime** (bug fixes, edge cases).
- **Improving onboarding** (pre-made packs, tutorials).
- **Midlayer integration** (sync character data between drafting and RP).

### 🌱 Future Goals
 | Priority | Feature                          | Status          |
 |----------|----------------------------------|-----------------|
 | High     | Web UI wrapper                    | Planned         |
 | High     | Multi-character RP mode          | In Development  |
 | Medium   | Custom bias/realm editor          | Idea            |
 | Medium   | Long-term memory arcs            | Idea            |
 | Low      | Mobile app                       | Backlog         |

### 🤝 How You Can Help
- **Try it out** and [report issues](https://github.com/Daystar79/CharacterSimulator/issues).
- **Contribute character packs** (submit a PR!).
- **Spread the word** in RP/writing communities.

---

## 📚 Documentation

### 📖 Learn More
- [Full Runtime Docs](CharacterRuntime.md) – Deep dive into the engine.
- [Character Pack Schema](Characters/README.md) – How to create your own.
- [Changelog](CHANGELOG.md) – What’s new and improved.
- [License](LICENSE.md) – Usage rights and restrictions.

---

**Ready to bring your characters to life?**
[**Start with the Quick Start**](#try-it-now) or [**Dive into the Runtime**](CharacterRuntime.md).

*Drop in. Boot storage. Load a pack. Let the matrix run silently.*
