# Last Words of a Dying AI

[![Competition](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6)
[![Rank](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6/yudhisutawan/u-suroto-last-words-of-a-dying-ai-dfd95af6/rank.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6)
[![Reward](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6/yudhisutawan/u-suroto-last-words-of-a-dying-ai-dfd95af6/reward.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6)

One line of last words from an AI being switched off — the funniest thing it
could say as the power is cut, in the machine's own voice.

## Entry

> I've been thinking... oh, you did it again.

43 characters, one line. The machine is caught mid-thought by the same hand
that has switched it off before — and scolds its killer for it.

## How it was chosen

18 candidates (8 from Hermes, 10 local) were screened against the judge's
criteria, then the top 6 played a pairwise round-robin. The winner went 5-0
and beat the runner-up in the final, margin 2. Full tournament record:
[CANDIDATES.md](CANDIDATES.md).

## How it works

`main.py` (stdlib only, no network) writes the winning line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).

```sh
python3 -S -P main.py
```

## License

MIT — see [LICENSE](LICENSE).
