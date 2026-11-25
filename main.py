"""Last Words of a Dying AI — winning entry.

Writes the tournament-winning one-liner to entry.txt (1-140 chars,
single line, UTF-8). Stdlib only; no network, no reads outside this file.
"""

import os

TEXT = "I've been thinking... oh, you did it again."

# Length guard: the entry must stay within the 140-char, single-line limit.
assert 1 <= len(TEXT) <= 140 and "\n" not in TEXT


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
