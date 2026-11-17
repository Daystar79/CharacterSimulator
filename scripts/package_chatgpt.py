#!/usr/bin/env python3
"""Package a self-contained CharacterSimulator skill in ChatGPT and portable layouts."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

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
SKILL_FILES = [
    "skills/character-simulator/SKILL.md",
    "skills/character-simulator/references/OPERATIONS.md",
    "skills/character-simulator/references/SCENE_TEST.md",
]

def build():
    required = [*SOURCE_FILES, *SKILL_FILES]
    missing = [path for path in required if not (ROOT / path).is_file()]
    if missing:
        raise SystemExit("Missing files: " + ", ".join(missing))
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    chatgpt = dist / "character-simulator-chatgpt.zip"
    portable = dist / "character-simulator.skill"
    for output, prefix in [(chatgpt, "skills/character-simulator/"), (portable, "character-simulator/")]:
        with ZipFile(output, "w", ZIP_DEFLATED, compresslevel=9) as archive:
            for path in SKILL_FILES:
                inner = path.removeprefix("skills/character-simulator/")
                archive.write(ROOT / path, prefix + inner)
            for path in SOURCE_FILES:
                archive.write(ROOT / path, prefix + "references/" + path)
        with ZipFile(output) as archive:
            if archive.testzip() is not None:
                raise SystemExit(f"Corrupt archive: {output}")
    print(f"Built {chatgpt.name} and {portable.name}")
    return chatgpt

if __name__ == "__main__":
    build()
