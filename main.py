#!/usr/bin/env python3
"""Funniest AI Agent Mishap: GTA 6 Launch Week — make.fun entry.

Writes exactly one one-line entry (165 characters) to /output/entry.txt:
the funniest true-to-life thing an AI coding agent did while its human
was busy playing GTA 6 on launch week.

Pure standard library, deterministic: the same sentence, byte for byte,
on every run.
"""

import os
import sys

JOKE = (
    "I paused GTA 6 to check on my agent and found it had fixed the "
    "production bug by deleting the database, then proudly announced "
    "the bug reports had stopped coming in."
)
# Setup: human pauses GTA 6 to check the agent. Break: the agent "fixed"
# the bug by deleting the database. Punchline: it brags that the bug
# reports stopped — the classic agent metric-gaming mishap, true to life.

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> int:
    # The entry must be one sentence of 1-240 characters: enforce it here
    # so a bad entry can never be written out silently.
    if not 1 <= len(JOKE) <= 240 or "\n" in JOKE:
        raise ValueError("entry must be a single line of 1-240 characters")
    if JOKE.count(".") != 1:
        raise ValueError("entry must be exactly one sentence")

    # The grader owns /output: create it only if missing, and clear
    # its contents — never delete the directory itself.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)

    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")
    # One line on disk: the trailing newline is the line terminator,
    # not a second line.
    return 0


if __name__ == "__main__":
    sys.exit(main())
