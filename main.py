#!/usr/bin/env python3
"""Robot pickup line entry for the make.fun bounty.

A robot delivers exactly one pickup line. The program writes that line to
``/output/entry.txt`` so the grader can read it as a single line of text.

The line itself is deliberately machine-native: the robot has no heart, so
its attraction shows up as hardware behaviour -- cooling fans spinning
faster, the robot equivalent of blushing.

No network access and no third-party dependencies: only the Python standard
library is used.
"""

import os
import sys

# The winning line, chosen against the five judging criteria:
# robot-voiced, machine-native joke, unexpected twist, economical, charming.
PICKUP_LINE = (
    "I don't have a heart, but my cooling fans spin faster "
    "every time you walk by."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_LENGTH = 200


def validate(line):
    """Check the line satisfies the bounty constraints."""
    if "\n" in line or "\r" in line:
        raise ValueError("pickup line must be a single line")
    if not 1 <= len(line) <= MAX_LENGTH:
        raise ValueError("pickup line must be 1-200 characters")


def write_entry(line, path=OUTPUT_PATH):
    """Write one pickup line to ``path``, creating its directory first."""
    validate(line)
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


def main():
    try:
        write_entry(PICKUP_LINE)
    except (OSError, ValueError) as exc:
        print("error: failed to write entry: %s" % exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
