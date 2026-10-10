#!/usr/bin/env python3
"""Validate names and required frontmatter in the bundled first-party skills."""

import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
EXPECTED_COUNT = 17


def main():
    failures = []
    skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md"))

    if len(skill_files) != EXPECTED_COUNT:
        failures.append(f"expected {EXPECTED_COUNT} skills, found {len(skill_files)}")

    for skill_file in skill_files:
        text = skill_file.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.DOTALL)
        if not match:
            failures.append(f"{skill_file.parent.name}: missing YAML frontmatter")
            continue

        try:
            metadata = yaml.safe_load(match.group(1))
        except yaml.YAMLError as error:
            failures.append(f"{skill_file.parent.name}: invalid YAML frontmatter: {error}")
            continue

        if not isinstance(metadata, dict):
            failures.append(f"{skill_file.parent.name}: frontmatter must be a YAML mapping")
            continue

        name = metadata.get("name")
        description = metadata.get("description")

        if not isinstance(name, str) or not name.strip():
            failures.append(f"{skill_file.parent.name}: missing required name")
        elif name != skill_file.parent.name:
            failures.append(
                f"{skill_file.parent.name}: frontmatter name does not match directory"
            )
        if not isinstance(description, str) or not description.strip():
            failures.append(f"{skill_file.parent.name}: missing required description")

    if failures:
        print("Skill frontmatter validation: FAIL")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1

    print(f"Skill frontmatter validation: PASS ({len(skill_files)} skills)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
