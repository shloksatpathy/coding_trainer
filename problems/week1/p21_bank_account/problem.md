# P21 · Mini-project: bank account

Read commands, one per line, until `Q`: `D amt` deposits, `W amt` withdraws, `B` prints the balance. A withdrawal larger than the balance prints `Insufficient` and changes nothing. The balance starts at 0.

Sample input:
```
D 500
W 200
W 400
B
Q
```
Output:
```
Insufficient
300
```

**Focus:** this combines loops, conditionals, functions and a struct. In Rust, parse each line into an `enum Command { Deposit(i64), Withdraw(i64), Balance, Quit }` and `match` on it. Week 2 builds on this pattern.

**Sample input** (also in `in.txt`):
```
D 500
W 200
W 400
B
Q
```
