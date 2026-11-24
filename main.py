"""One-Line Office Joke: 24-Hour Sprint.

Reads the single joke line from ENTRY.txt (kept beside this file) and
writes it, exactly and unchanged, to <output>/entry.txt, where <output>
is MAKEFUN_OUTPUT_DIR when set and /output otherwise.

Standard library only: no third-party imports, no network, no randomness,
so the two grading runs produce byte-identical output.
"""

import os
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    entry_path = os.path.join(here, "ENTRY.txt")
    with open(entry_path, "r", encoding="utf-8") as handle:
        joke = handle.read().strip()

    if not joke:
        print("ENTRY.txt is empty", file=sys.stderr)
        return 1
    if len(joke) > 200:
        print("joke is %d characters, over the 200 limit" % len(joke),
              file=sys.stderr)
        return 1
    if "\n" in joke:
        print("joke must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(joke)
    print("wrote %d bytes to %s" % (len(joke.encode("utf-8")), out_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
