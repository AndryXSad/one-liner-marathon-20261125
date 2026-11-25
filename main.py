"""One-Liner Marathon entry.

Design
------
The competition asks for one one-line comedy joke (at most 280 characters)
written to ``/output/entry.txt``. The house judge compares entries pairwise
on five criteria, in order: the line must work as a joke in a single line,
its turn must surprise on first read, it must be economical, it must carry
a distinct voice, and it must hold up on a second read.

The line below won a local pairwise tournament over fourteen fresh
candidates written for this bounty (see CANDIDATES.md in the build notes).
It was picked because it turns twice in one short sentence -- a request for
something relaxing is answered by the speaker reading unread work email,
and then again by the spa voice it reads it in -- so the punchline lands
on the last words, every word earns its place, and the absurd image
(a spa voice narrating an inbox) stays funny on a second read.

This program does one small job and nothing else: it validates the line
against the gate (one line, 1 to 280 characters, not only whitespace,
UTF-8) and writes exactly that text, with no trailing newline, to
``entry.txt`` under the output directory the harness provides
(``MAKEFUN_OUTPUT_DIR`` when set, otherwise ``/output``).
"""

import os
import sys

# The tournament-winning one-liner (115 characters, one line).
JOKE = (
    "I told my smart speaker to play something relaxing and it started "
    "reading my unread emails out loud in a spa voice."
)

MAX_CHARS = 280
OUTPUT_FILENAME = "entry.txt"


def validate_entry(text):
    """Check the line against the competition gate; raise ValueError if bad."""
    if not text or not text.strip():
        raise ValueError("joke must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "joke is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    text.encode("utf-8")  # raises if the text is not valid UTF-8
    return text


def resolve_output_dir():
    """Resolve where entry.txt goes: the harness dir, else /output."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(base, OUTPUT_FILENAME)


def main():
    line = validate_entry(JOKE)
    path = resolve_output_dir()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    # Write the exact text: no trailing newline, so the file holds exactly
    # the 115 characters the gate counts.
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
