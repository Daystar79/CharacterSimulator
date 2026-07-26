# CharacterSimulator

**Standalone Roleplay Engine & Stress-Testing Suite**

The **CharacterSimulator** is a self-contained environment designed for live character chat, roleplaying sessions, card stress-testing, and dynamic visual frame rendering.

---

## 🚀 Quick Start

1. **Self-Contained Chat Drop-in**:
   Paste [`CharacterRuntime.md`](CharacterRuntime.md) (or `Simulator/CharacterRuntime.md`) directly into any LLM chat session.
2. **Load Character Pack**:
   Provide your target character card from [`Characters/`](Characters/) along with its memory state log.
3. **Session Modes**:
   - **`TEST` (Default)**: Stress-test character fidelity, somatic reactions, and worldview filters.
   - **`COMPANION` / `HEAT`**: Interactive live roleplay (adult paths gated with `/adult on`).

---

## 📁 Repository Structure

```
CharacterSimulator/
├── README.md                   # Overview & usage guide
├── CharacterRuntime.md         # Top-level standalone drop-in runtime
├── Simulator/                  # Roleplaying Engine & Private Session Drop-ins
│   ├── CharacterRuntime.md
│   ├── README.md
│   └── Private/
│       └── CharacterRuntime.md
├── Images/                     # Visual Frame & Motion Rendering Engine
│   └── CharacterRenderingEngine.md
├── Framework/                  # Supporting Somatic & Psyche Profiles
│   └── Psychology/
│       └── realm_data.yaml
└── Characters/                 # Character Cards & Runtime Log Schemas
    ├── _template.md
    ├── _log_template.yaml
    └── ...
```

---

## 🎨 Visual Rendering Engine

Visual rendering via `Images/CharacterRenderingEngine.md` is disabled (`off`) by default to ensure zero-latency response turns.

- Force a frame anytime: `/render`
- Toggle motion modes: `/visual off|fast|prompts|live`

---

## 📜 License

Content, cards, and simulator scripts are licensed under the **Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)**.
