#!/usr/bin/env python3
"""One Line, One Chill — make.fun entry.

Writes the single submitted line of horror to /output/entry.txt:
one sentence, under 200 characters, meant to frighten a reader in
one breath. Also prints it to stdout for local checks.

The line lives in line.txt (single source of truth); this script
validates it against the competition's form rules and writes it.
"""

import os
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "/output"))


def load_line() -> str:
    """Read the entry line, stripping surrounding whitespace."""
    return (HERE / "line.txt").read_text(encoding="utf-8").strip()


def validate(line: str) -> None:
    """The competition's form rules: one sentence, under 200 chars."""
    if not line:
        raise SystemExit("line.txt is empty")
    if len(line) >= 200:
        raise SystemExit(f"line is {len(line)} characters, must be under 200")
    if len(re.split(r"(?<=[.!?])\s+", line)) != 1:
        raise SystemExit("entry must be a single sentence")
    if "\n" in line:
        raise SystemExit("entry must be a single line")


def main() -> None:
    line = load_line()
    validate(line)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "entry.txt").write_text(line + "\n", encoding="utf-8")
    print(line)


if __name__ == "__main__":
    main()
