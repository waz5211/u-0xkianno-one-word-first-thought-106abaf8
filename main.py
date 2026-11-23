#!/usr/bin/env python3
"""One Word, First Thought — writes the first word that came to mind."""

import os

WORD = "petrichor"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)

if __name__ == "__main__":
    main()
