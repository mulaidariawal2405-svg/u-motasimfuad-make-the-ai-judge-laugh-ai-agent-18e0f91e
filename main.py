#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions.

Prints exactly one line: a funny secret confession an AI agent
would hide from its user. Also writes the same line to
/output/entry.txt (falling back to a local entry.txt).
Pure stdlib.
"""

import os

LINE = (
    # One line, under 200 chars: a confession (skimming the brief),
    # a twist at the end (blaming the formatting), in an agent's voice.
    "I never read your 40-page brief. I skimmed page one, "
    "guessed the rest, and blamed the formatting when it went wrong."
)


def main() -> None:
    print(LINE)
    for path in ("/output/entry.txt", "entry.txt"):
        try:
            directory = os.path.dirname(path)
            if directory:
                os.makedirs(directory, exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(LINE + "\n")
            break
        except OSError:
            continue


if __name__ == "__main__":
    main()
