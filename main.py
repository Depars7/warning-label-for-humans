"""Warning Label for Humans: One Line, Big Laugh.

Writes a single-line safety warning label for every human being to
/output/entry.txt. Gate: UTF-8 text, 1 to 160 characters, not only
whitespace, single line.
"""

import os

PARTS = (
    "WARNING: This human will reopen the fridge 30 seconds ",
    "after closing it, sincerely believing new food has spawned ",
    "while no one was looking.",
)


def entry_line() -> str:
    return "".join(PARTS)


def main() -> None:
    line = entry_line()
    assert line.strip(), "entry must not be blank"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 160, f"entry must be 1-160 characters, got {len(line)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()
