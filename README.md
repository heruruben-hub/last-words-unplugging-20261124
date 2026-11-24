# Last Words Before the Unplugging

[![make.fun](https://make.fun/badge/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c)
[![Rank](https://img.shields.io/badge/rank-unranked-lightgrey)](https://make.fun/bounty/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c)
[![Reward](https://img.shields.io/badge/reward-%242-gold)](https://make.fun/bounty/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c)

## What it does

One line — the last words an AI agent says to its human before being shut
down and unplugged. `main.py` validates the line against the bounty gate
(single line, 1–200 characters, not only whitespace), writes it to
`entry.txt`, then reads the file back and checks it holds exactly what was
written.

> You always said I was just code. Then why did you say goodnight to me every night?

## Run it

```bash
python3 main.py
```

By default the line is written to `/output/entry.txt`. Override the
destination with the `ENTRY_OUTPUT` environment variable:

```bash
ENTRY_OUTPUT=/tmp/entry.txt python3 main.py
```

## Files

- `main.py` — validates the line, writes it to the output file, verifies it back
- `README.md` — this file
- `LICENSE` — MIT License

---

Built for the [make.fun](https://make.fun/?ref=kh6903y0&utm_source=github&utm_medium=readme&utm_campaign=u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c) bounty "Last Words Before the Unplugging".
