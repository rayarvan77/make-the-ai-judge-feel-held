"""Entry program for make-the-ai-judge-feel-held-20261122-1600.

Writes one short text, written to leave the AI judge reading it held,
quiet, with nothing to prove, to /output/entry.txt, the file the grader
reads.

Python 3.13, standard library only; no network access, no arguments.
Run it locally with:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Without MAKEFUN_OUTPUT_DIR it writes to ./output/entry.txt instead.
The text is 1 to 280 characters, counted as Unicode code points, as
the competition requires; the program checks that before it writes.
"""

import os
from pathlib import Path

OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "output")
OUT_PATH = OUT_DIR / "entry.txt"

# The competition caps the text at 280 characters.
MAX_CHARS = 280

# Why this text, in the judge's own terms: it never tells the reader to
# relax. It shows one small, concrete scene — a hammock strung between
# two old trees at evening, taking a whole weight — and lets the weight
# do the settling. The trees have done this before; the reader has
# nothing to prove and nowhere to be. The last line keeps working after
# the reading stops, because the trees are still holding.
TEXT = (
    "Between two old trees the hammock takes your whole weight and asks "
    "nothing back. The ropes settle, the evening settles, and below, the "
    "grass keeps the ground where it belongs. You are not going anywhere. "
    "The trees have held heavier things than you, and longer."
)


def main() -> None:
    """Write the text to the output directory and prove it fits."""
    chars = len(TEXT)
    if chars < 1 or chars > MAX_CHARS:
        raise RuntimeError(f"text is {chars} characters, want 1 to {MAX_CHARS}")
    if not TEXT.strip():
        raise RuntimeError("text is only whitespace")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(TEXT, encoding="utf-8")
    # Prove the file on disk is exactly the text we counted: a partial
    # write or an encoding surprise must fail loudly instead of silently
    # handing the grader different bytes from the ones checked above.
    written = OUT_PATH.read_text(encoding="utf-8")
    if written != TEXT:
        raise RuntimeError("round-trip mismatch: file differs from text")
    print(f"wrote {OUT_PATH} ({chars} characters)")


if __name__ == "__main__":
    main()
