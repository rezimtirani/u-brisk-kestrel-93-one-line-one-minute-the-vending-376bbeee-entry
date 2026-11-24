"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single pickup line, spoken by a vending machine to a passing
human, to $MAKEFUN_OUTPUT_DIR/entry.txt. The line leans on the machine's
own world: its coils, its lights, the hallway it stands in, and the one
thing on the whole floor it cannot dispense.
"""

import os
import sys


LINE = (
    "My coils are full, my lights are on, and of everything in this "
    "hallway, you're the only thing I can't dispense."
)


def check_line(line):
    """Refuse anything the gate would refuse: outside 1-200 chars, or
    only white space. A bad line fails here, loudly, instead of
    travelling to the grader and scoring zero."""
    if not line.strip():
        raise ValueError("entry line must not be only white space")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry line must be 1-200 characters, got %d" % len(line))


def main():
    check_line(LINE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
