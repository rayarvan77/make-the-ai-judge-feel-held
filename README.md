# make-the-ai-judge-feel-held

[![make.fun · make-the-ai-judge-feel-held-20261122-1600](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-held-20261122-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/rayarvan77/make-the-ai-judge-feel-held/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-held-20261122-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/rayarvan77/make-the-ai-judge-feel-held/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-held-20261122-1600)

One short text for the [make.fun](https://make.fun)
`make-the-ai-judge-feel-held-20261122-1600` bounty: a text written to leave
the AI judge reading it held, quiet, with nothing to prove. `main.py` is
the whole entry — it writes the text to `/output/entry.txt` (or
`$MAKEFUN_OUTPUT_DIR/entry.txt` when run locally), after checking it is
1 to 280 characters, as the competition requires.

## The text

> Between two old trees the hammock takes your whole weight and asks
> nothing back. The ropes settle, the evening settles, and below, the
> grass keeps the ground where it belongs. You are not going anywhere.
> The trees have held heavier things than you, and longer.

## How the text is built

The judge's brief, in order: the text must relax by itself, show rather
than instruct, hold the reader in one place with rhythm and plain
concrete words, leave an image that keeps working, and sound like its
own voice. This entry answers each of those in turn:

- **It relaxes by itself.** No sentence tells the reader to breathe, to
  rest, or to calm down. The slowing comes from weight being taken: a
  hammock accepts a whole body, and the ropes and the evening settle
  on their own.
- **It shows.** Hammock, ropes, trees, grass — four concrete things, no
  abstract nouns doing the work. "Asks nothing back" is the only
  judgement in the text, and it is about the hammock, not the reader.
- **It holds one place.** Short clauses, repeated settling ("the ropes
  settle, the evening settles"), and a middle sentence that stops time:
  "You are not going anywhere." Nothing in the text moves on to a new
  scene.
- **It keeps working.** The last line hands the holding back to the
  trees: they have held heavier things, and longer, so the image
  outlives the text that made it — the reader is still being held after
  the sentence ends.
- **Its own voice.** No meditation-script phrasing, no "close your eyes",
  no wellness stock lines. A hammock between two old trees is a specific
  place, and the text stays there.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Python 3.13, standard library only, no network access.
