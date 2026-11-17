#!/usr/bin/env python3
"""Validate source files and packaged CharacterSimulator skill structure."""
from pathlib import Path
from zipfile import ZipFile
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from package_chatgpt import SOURCE_FILES, SKILL_FILES, build

def main():
    for path in [*SOURCE_FILES, *SKILL_FILES]:
        if not (ROOT / path).is_file():
            raise SystemExit(f"Missing: {path}")
    skill = (ROOT / "skills/character-simulator/SKILL.md").read_text()
    if not skill.startswith("---\n") or "name: character-simulator" not in skill:
        raise SystemExit("Invalid SKILL.md frontmatter")
    output = build()
    with ZipFile(output) as archive:
        names = set(archive.namelist())
        expected = {"skills/character-simulator/" + path.removeprefix("skills/character-simulator/") for path in SKILL_FILES}
        expected.update("skills/character-simulator/references/" + path for path in SOURCE_FILES)
        if names != expected:
            raise SystemExit(f"Archive mismatch: missing={expected-names}, unexpected={names-expected}")
        if archive.testzip() is not None:
            raise SystemExit("Corrupt ZIP")
    print(f"Validated {len(names)} bundled files")

if __name__ == "__main__":
    main()
