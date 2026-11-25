#!/usr/bin/env python3
"""Write the one-line excuse to /output/entry.txt.

The line is built from two clauses: the instruction the human gave,
then the turn that makes the instruction itself the bug.
"""
import os
from pathlib import Path

LINE = "You told me to use my best judgment. My best judgment was the bug."


def main():
    text = LINE.strip()
    assert text == LINE, "entry must have no leading or trailing space"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text, "entry must be a single line"
    assert len(text.encode("utf-8")) == 66, "entry must be 66 bytes"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(text, encoding="utf-8")
    assert target.read_bytes() == text.encode("utf-8")


if __name__ == "__main__":
    main()
