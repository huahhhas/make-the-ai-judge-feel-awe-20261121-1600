"""Make the AI judge feel awe — entry program.

Writes one short text to /output/entry.txt: starlight that left its
star before the first cities were built, still travelling, unhurried —
and a night wide enough to hold it all.
Python 3.13, standard library only, no network.
"""

import os
from pathlib import Path

TEXT = (
    "The light reaching you tonight left its star before the first "
    "cities were built, and it travelled all that way without "
    "hurrying. You are small beside it, and nothing you are carrying "
    "is urgent beside that. The night is wide enough to hold it all — "
    "and still has room for you."
)


def validate(text: str) -> None:
    # Length is counted as Unicode code points, per the rules.
    if not 1 <= len(text) <= 280:
        raise ValueError(f"text is {len(text)} characters, must be 1-280")
    if not text.strip():
        raise ValueError("text must not be only white space")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
