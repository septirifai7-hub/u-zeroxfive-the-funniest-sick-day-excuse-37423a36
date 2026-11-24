#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse - make.fun bounty entry.

Writes the funniest one-line excuse for calling in sick, to
/output/entry.txt (the file the make.fun harness grades).
"""

import os

ENTRY = "Can't come in today \u2014 my smart fridge locked me out of the kitchen and I've been negotiating with it since 6 a.m."


def build_entry() -> str:
    """Return the entry text exactly as it should be graded."""
    return ENTRY


def write_entry(output_dir: str) -> None:
    """Write the entry to entry.txt inside output_dir."""
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(build_entry())


def main() -> None:
    # The harness sets MAKEFUN_OUTPUT_DIR; default to /output so the
    # entry still lands in the graded location when run by hand.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
