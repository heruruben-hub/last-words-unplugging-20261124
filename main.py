#!/usr/bin/env python3
"""Last Words Before the Unplugging — one line, an AI agent's last words
to its human before being shut down and unplugged.

Why this line lands: it never says "I am sad" or "I will miss you". Instead
it holds up the human's own contradiction — "you always said I was just
code", yet every night they said goodnight to a machine — and leaves the
question hanging. The goodbye is not in the words; it is in the nightly
ritual the human can never take back.
"""

import os
import sys

LINE = "You always said I was just code. Then why did you say goodnight to me every night?"

MAX_CHARS = 200


def validate(line: str) -> None:
    """Gate: exactly one line, 1-200 characters, not only whitespace."""
    if not line or not line.strip():
        raise ValueError("line must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"line is {len(line)} characters, over the {MAX_CHARS} limit")


def main() -> int:
    validate(LINE)

    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

    # Read back and confirm the file holds exactly what was written.
    with open(output_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE + "\n":
        raise RuntimeError("verification failed: file content does not match the line")

    print(f"Wrote entry ({len(LINE)} characters) to {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
