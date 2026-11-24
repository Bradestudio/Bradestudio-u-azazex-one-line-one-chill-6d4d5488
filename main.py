"""One Line, One Chill — make.fun bounty entry.

Writes one line of horror (122 chars) to entry.txt in
MAKEFUN_OUTPUT_DIR (fallback /output). Stdlib only, no network,
deterministic: the same bytes on every run.

Candidates considered (my own revisions, not copies of other entries):
  A. "The DNA test said the blood under my fingernails was mine —
      from a body found in the woods twenty years before I was born."
      (122 chars) — CHOSEN.
  B. "I recognised the handwriting on the ransom note at once: it was
      mine, and I have never written it, and it is dated tomorrow."
      (124 chars) — good twist, but "dated tomorrow" is a familiar
      trope and the scare is a puzzle, not a dread.
  C. "The hospice nurse logged my mother's last breath at 3:04 a.m.,
      then asked why the woman in the bed kept breathing after it."
      (123 chars) — vivid, but the scare leans on a deathbed scene
      the judge has met many times.

Why A wins: one concrete forensic image (blood under fingernails, a
DNA test, a body in the woods) collides with an impossible fact — the
blood is the reader's, from twenty years before they were born. The
scare is earned, not announced: no "I was terrified", no gore, just a
lab result that quietly proves the reader was already dead once. It
withholds the explanation entirely, so the dread outlasts the line,
and the last word — "born." — lands the paradox.
"""

import os
import sys

ENTRY = (
    "The DNA test said the blood under my fingernails was mine "
    "\u2014 from a body found in the woods twenty years before "
    "I was born."
)


def main():
    text = ENTRY
    if not text or not text.strip():
        sys.exit("entry text is blank")
    lines = text.split("\n")
    if len(lines) != 1:
        sys.exit("entry must be exactly one line, got %d" % len(lines))
    if text != text.strip():
        sys.exit("entry must not start or end with whitespace")
    if not 1 <= len(text) <= 200:
        sys.exit("entry must be 1-200 characters, got %d" % len(text))
    if not text.endswith("I was born."):
        sys.exit("entry must end with the paradox landing on 'born.'")
    if "DNA test" not in text or "twenty years before" not in text:
        sys.exit("entry lost its concrete detail")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = text.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    # Re-read and verify the file is exactly the gated text, no newline.
    with open(path, "rb") as fh:
        written = fh.read()
    if written != data:
        sys.exit("entry.txt does not match the gated text")
    print("wrote %s (%d chars, %d bytes, %d lines)"
          % (path, len(text), len(data), len(lines)))


if __name__ == "__main__":
    main()
