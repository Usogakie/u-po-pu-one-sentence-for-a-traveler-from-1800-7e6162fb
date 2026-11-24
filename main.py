"""One sentence for a traveler from 1800.

Writes a single sentence explaining the modern internet, in words
a person from 1800 could picture, to entry.txt. The sentence stays
inside the gate: one sentence, at most 200 characters, no trailing
newline, so the file holds exactly the sentence and nothing else.
"""

import os

SENTENCE = (
    "The internet is a single post office where your letter reaches "
    "the far side of the world before your tea goes cold, and the "
    "reply is already on its way back."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
