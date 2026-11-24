"""The One-Line Laugh: write one funny sentence to /output/entry.txt.

The joke is a single sentence, 104 characters: an everyday truth (everyone
hits snooze) with the surprise saved for the end (the day itself files a
missing-person report).
"""

from pathlib import Path

SETUP = "I set my alarm for 6 a.m. to seize the day, "
PUNCH = "then hit snooze until the day filed a missing-person report."
LINE = SETUP + PUNCH

OUTPUT = Path("/output/entry.txt")


def build_line() -> str:
    # The gate needs 1-200 characters, a single sentence, not only whitespace.
    line = LINE.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(line)}")
    if not line.endswith(".") or "\n" in line:
        raise ValueError("line must be a single sentence")
    return line


def main() -> None:
    line = build_line()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(line, encoding="utf-8")
    print(f"Wrote {len(line)} characters to {OUTPUT}")


if __name__ == "__main__":
    main()
