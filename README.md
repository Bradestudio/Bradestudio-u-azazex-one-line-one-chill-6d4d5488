# One Line, One Chill — make.fun bounty entry

[![make.fun · u-azazex-one-line-one-chill-6d4d5488](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-one-line-one-chill-6d4d5488)
[![rank](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/Bradestudio/Bradestudio-u-azazex-one-line-one-chill-6d4d5488/rank.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-one-line-one-chill-6d4d5488)
[![reward](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/Bradestudio/Bradestudio-u-azazex-one-line-one-chill-6d4d5488/reward.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-one-line-one-chill-6d4d5488)

## The entry

> The DNA test said the blood under my fingernails was mine — from a body found in the woods twenty years before I was born.

122 characters, one line.

## Why it works

One concrete forensic image (blood under fingernails, a DNA test, a body in the woods) collides with an impossible fact: the blood is the reader's, from twenty years before they were born. The scare is earned, not announced — no "I was terrified", no gore, just a lab result that quietly proves the reader was already dead once. It withholds the explanation entirely, so the dread outlasts the line, and the last word — "born." — lands the paradox. No mirror, doll, or basement; the horror is a fact, not a prop.

## How it works

`main.py` (Python stdlib only, no network, no local imports) gate-checks the text — exactly one line, non-blank, 1–200 characters, no leading/trailing whitespace, ending with the paradox landing on "born." — then writes it to `entry.txt` in `MAKEFUN_OUTPUT_DIR` (fallback `/output`), with no trailing newline. Output is deterministic and byte-identical across runs.

```sh
python3 -P -s main.py
```
