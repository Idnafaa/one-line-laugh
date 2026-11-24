"""One-Line Laugh entry: writes a single funny sentence to /output/entry.txt."""

from pathlib import Path

LINE = (
    "I set my alarm for 6 a.m. to seize the day, "
    "then hit snooze until the day filed a missing-person report."
)


def main() -> None:
    # The gate requires 1-200 characters, a single sentence, not only whitespace.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters"
    assert LINE.strip() == LINE and LINE.endswith(".") and "\n" not in LINE, (
        "must be one sentence"
    )
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    print(f"Wrote {len(LINE)} characters to {out}")


if __name__ == "__main__":
    main()
