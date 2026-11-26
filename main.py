#!/usr/bin/env python3
"""Entry for make.fun: The Robot Apology.

The entry is a two-line apology from a household robot. For
six months it watered the plastic plant with great devotion
while the real fern beside it died of thirst, because the
fern was filed under decoration and the plastic one was
closer to the tap. The second line is the lesson it has
carried ever since: a description is not a location, and
these days it photographs every plant it loves, just in
case love needs a reference image and a watering schedule.

Running this program writes the entry to /output/entry.txt,
falling back to ./output/entry.txt when /output is not
writable, and prints it to stdout as well.
"""

from pathlib import Path

ENTRY_TEXT = (
    "I am sorry I watered the plastic plant for six months while the "
    "real fern died of thirst beside it.\n"
    "I have learned that a description is not a location, and I now "
    "take a photo of every plant I love."
)

# Six months of faithful watering, aimed one pot to the left:
# the apology is sincere, the aim has since been recalibrated.
MONTHS_OF_DEVOTION = 6


def render_entry() -> str:
    """Return the apology exactly as the robot delivers it."""
    return ENTRY_TEXT


def two_lines_exactly(text: str) -> bool:
    """Confirm the apology is two lines and within the cap."""
    return text.count("\n") == 1 and len(text) <= 240


def write_entry(text: str) -> Path:
    """Write the entry text to the output file and return its path."""
    out_dir = Path("/output")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target
    except OSError:
        out_dir = Path("output")
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target


def main() -> None:
    text = render_entry()
    assert two_lines_exactly(text), "the apology must be two lines"
    write_entry(text)
    print(text)


if __name__ == "__main__":
    main()
