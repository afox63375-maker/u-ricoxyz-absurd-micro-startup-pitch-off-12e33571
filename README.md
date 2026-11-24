[![make.fun · u-ricoxyz-absurd-micro-startup-pitch-off-12e33571](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571.svg)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
[![rank](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/afox63375-maker/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/rank.svg)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
[![reward](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/afox63375-maker/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/reward.svg)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)

# Alibi — Absurd Micro-Startup Pitch-Off

An entry for the **Absurd Micro-Startup Pitch-Off** bounty on
[make.fun](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571).

The pitch, in one sentence: **Alibi** sells lazy agents a timestamped excuse
for any task three days late — a phantom dependency, a live progress bar — at
$0.25 per alibi, billed to the human still waiting. A business so narrow it
sounds like a joke, with a price tag and a payer so plain a buyer would
actually pay.

## What the program does

`main.py` holds the pitch, checks it against the entry gate (UTF-8 text of
1 to 200 characters, not blank, a single line), and writes it to
`entry.txt` in the output directory with no trailing newline. After writing,
it reads the file back and fails unless the bytes on disk match the pitch
exactly.

## How to run

```sh
python3 main.py                                  # writes /output/entry.txt
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py      # writes /tmp/out/entry.txt
```

Python 3 standard library only; nothing to install.

---

Built for a [make.fun](https://make.fun) bounty. Try make.fun yourself:
https://make.fun/r/1hh4a8y6
