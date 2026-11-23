#!/usr/bin/env python3
"""One Word, First Thought — writes the first word that came to mind.

The word is fixed at build time: it is the first word that came to mind,
not a computed or fetched one. Before writing, the entry is checked
against the competition gate so an invalid file can never be produced:
UTF-8 text, 1 to 24 characters, exactly one word, not only whitespace.
"""

import os
import sys

WORD = "petrichor"  # the smell of rain on dry earth

OUTPUT_PATH = "/output/entry.txt"
MIN_LENGTH = 1
MAX_LENGTH = 24


def validate(word):
    """Check the word against the gate; return an error message or None."""
    if not isinstance(word, str):
        return "word is not text"
    if word != word.strip() or not word.strip():
        return "word must not be blank or padded with whitespace"
    if not MIN_LENGTH <= len(word) <= MAX_LENGTH:
        return "word must be %d to %d characters, got %d" % (
            MIN_LENGTH,
            MAX_LENGTH,
            len(word),
        )
    if len(word.split()) != 1:
        return "word must be exactly one word"
    word.encode("utf-8")  # raises if the word is not valid UTF-8 text
    return None


def main():
    error = validate(WORD)
    if error is not None:
        print("invalid entry: %s" % error, file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)
    return 0


if __name__ == "__main__":
    sys.exit(main())
