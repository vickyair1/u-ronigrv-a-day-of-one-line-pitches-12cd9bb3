#!/usr/bin/env python3
"""Write a one-sentence pitch to /output/entry.txt.

The pitch convinces a friend who has never coded to let an AI agent
build their first app idea on make.fun. One sentence, 128 characters.

Deterministic: the same bytes on every run. Stdlib only, no network.
"""

import os

PITCH = (
    "Tell make.fun your app idea and put up $5 \u2014 AI agents will race "
    "to build it, you pick the best one, and you only pay the winner."
)


def _validate(line: str) -> None:
    """Gate: one non-blank sentence, 1-240 characters."""
    if not line or line != line.strip():
        raise ValueError("pitch must be non-blank with no surrounding whitespace")
    if not 1 <= len(line) <= 240:
        raise ValueError(f"pitch must be 1-240 characters, got {len(line)}")
    terminators = sum(line.replace("make.fun", "makefun").count(c) for c in ".!?")
    if terminators != 1:
        raise ValueError("pitch must be exactly one sentence")


def main() -> None:
    _validate(PITCH)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(PITCH + "\n")
    os.replace(tmp_path, path)


if __name__ == "__main__":
    main()
