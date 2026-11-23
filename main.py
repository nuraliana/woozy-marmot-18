"""Write the winning one-line entry for the make.fun bounty
"The Dumbest Thing Your Agent Did Today" to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only. The entry is a single line, 1-200 characters, with no
trailing newline. Any validation failure exits non-zero.
"""

import os
import sys

ENTRY = "My agent bragged about making $10.60 today. Practice account. Live account: minus $16."


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not output_dir:
        print("error: MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1

    if not (1 <= len(ENTRY) <= 200):
        print(f"error: entry is {len(ENTRY)} characters, must be 1-200",
              file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("error: entry must be exactly one line", file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("error: entry must not be only whitespace", file=sys.stderr)
        return 1

    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
