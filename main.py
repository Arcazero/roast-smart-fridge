#!/usr/bin/env python3
"""Roast the Smart Fridge: One Line, Best Laugh Wins.

make.fun bounty: u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9

The whole entry is a single roast line of at most 160 characters. This
program writes that line to entry.txt inside the output directory the
grader provides, so the gate scorer can read it and the judge can compare
it head-to-head against the other entries.

Run it with `python3 main.py`. It reads MAKEFUN_OUTPUT_DIR for where to
put entry.txt and falls back to /output, the directory the sandbox mounts
writable. The run is deterministic: the same fixed line every time, no
network, no randomness, no input files.
"""

import os

LINE = (
    "My smart fridge locked the ice cream behind a wellness goal, "
    "so now I negotiate with an appliance at midnight like it is "
    "my parole officer."
)

# The gate requires 1 to 160 UTF-8 characters, not only whitespace.
assert 1 <= len(LINE) <= 160, "line is %d characters" % len(LINE)
assert LINE.strip(), "line must not be only whitespace"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")
    with open(path, "r", encoding="utf-8") as handle:
        saved = handle.read()
    if saved != LINE + "\n":
        raise SystemExit("entry.txt does not hold the roast line")
    print(LINE)


if __name__ == "__main__":
    main()
