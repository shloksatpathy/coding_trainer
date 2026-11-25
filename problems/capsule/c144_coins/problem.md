# C144 · Making change

Read an amount in cents (0 ≤ amount ≤ 1 000 000). Pay it with the coins 200, 100, 50, 20, 10, 5, 2 and 1, always taking as many of the largest coin as fit before moving to the next. Print `COIN x COUNT` for each coin used, from the largest, then `coins: TOTAL`.

**Example**

Input (also in `in.txt`):
```
289
```
Output:
```
200 x 1
50 x 1
20 x 1
10 x 1
5 x 1
2 x 2
coins: 7
```

**Focus:** a greedy algorithm: take the best choice now and never look back. For these coins it gives the fewest coins.
