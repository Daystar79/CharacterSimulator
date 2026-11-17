#!/usr/bin/env python3
"""Build a self-contained ChatGPT plugin ZIP from a public-file allowlist."""
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE_FILES = [
    "CharacterRuntime.md",
    "Framework/CognitivePipeline.md",
    "Framework/Rules_Index.md",
    "Framework/Modules.md",
    "Framework/Psychology/realm_data.yaml",
    "Framework/Schemas/psychosomatic_state.json",
    "Framework/Prompts/character_builder_prompt.md",
    "Characters/_template.md",
    "Characters/_template.json",
    "Characters/HOW_TO_CARD.md",
    "Characters/README.md",
    "LICENSE.md",
]
ENTRY = ROOT / "skills/character-simulator/SKILL.md"

def main():
    missing = [str(p) for p in [ENTRY, *(ROOT / f for f in SOURCE_FILES)] if not p.is_file()]
    if missing:
        raise SystemExit("Missing files: " + ", ".join(missing))
    output = ROOT / "dist/character-simulator-chatgpt.zip"
    output.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        archive.write(ENTRY, "skills/character-simulator/SKILL.md")
        for relative in SOURCE_FILES:
            archive.write(ROOT / relative, "skills/character-simulator/references/" + relative)
    with zipfile.ZipFile(output) as archive:
        assert archive.testzip() is None
        assert "skills/character-simulator/SKILL.md" in archive.namelist()
        assert "skills/character-simulator/references/CharacterRuntime.md" in archive.namelist()
    print(f"Created {output} ({output.stat().st_size:,} bytes)")
if __name__ == "__main__":
    main()
