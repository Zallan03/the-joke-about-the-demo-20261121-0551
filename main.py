#!/usr/bin/env python3
"""The joke about the demo — make.fun entry.

Writes one one-line joke about working beside an AI coding agent to
/output/entry.txt. Deterministic, stdlib only, no network.
"""

import os

JOKE = (
    "My AI agent fixed the bug in four seconds, then brought it back "
    "on stage for an encore."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 280


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= MAX_CHARS, "joke must be 1-280 characters"
    assert text.strip(), "joke must not be only whitespace"
    assert "\n" not in text, "joke must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
