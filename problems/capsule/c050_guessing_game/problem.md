# C050 · Checkpoint: guessing game

The first line has the secret number and `n`, the number of guesses. Then come `n` guesses, one per line. For each guess print `too low` or `too high`, or `correct on guess K` (K counts from 1) and stop: ignore the remaining guesses. If no guess is correct, print `no luck, it was SECRET` at the end.

**Example**

Input (also in `in.txt`):
```
42 3
50
25
42
```
Output:
```
too high
too low
correct on guess 3
```

**Focus:** checkpoint for module 5: a counting loop, decisions inside it, leaving early with `break`, and remembering whether it happened.
