# Coding Redo — Week 1 Problem Set (Basics)

Nov 22, 2026 · @Shlok Satpathy

## How this plan works

- **Weekly sets, daily deliverables.** One set is released per week, after the previous week's checkpoint, so difficulty follows your actual level. Each day has its own deliverable: **3 problems × 4 languages = 12 solutions**.
- **Basics → advanced.** Week 1 is fundamentals. It also doubles as your Rust on-ramp: each day introduces one Rust concept (mutability, borrowing, slices, `String`/`&str`, structs, enums).
- **Order per problem: C → C++ → Python → Rust.** C makes you handle types and memory by hand. C++ shows what the STL takes off your hands. Python gives you working reference logic fast. Rust goes last, so you are translating logic you already know is correct. When Rust fails, you are debugging the language, not the algorithm.
- **Same input, same output.** All 4 versions read the same input format. Save the sample input in `in.txt`, run all four, and diff the outputs. If they differ, one of them has a bug.

### Workload analysis (Week 1 estimate)

| Language | Est. min / problem | What drives the time |
| --- | --- | --- |
| C | 12 | Manual I/O, fixed arrays, no string type |
| C++ | 8 | STL shortens most solutions |
| Python | 5 | Reference implementation |
| Rust | 20 | New language; compiler errors take most of the time early on |
| **Total** | **\~45** | **≈ 2.25 h/day for 3 problems** |

Week 1 totals: 21 problems, 84 solutions. The number to watch is your Rust time. It should fall from \~20 min to \~10 min by Day 7. If it doesn't, Week 2 slows down.

### Folder setup

```
coding-redo/
  week1/
    day01/
      p01_arithmetic/   main.c   main.cpp   main.py   in.txt
    rust/               (one cargo project per week)
      src/bin/p01.rs
      src/bin/p02.rs
```

- C: `gcc -Wall -o p main.c && ./p < in.txt`
- C++: `g++ -std=c++17 -Wall -o p main.cpp && ./p < in.txt`
- Python: `python3 main.py < in.txt`
- Rust: `cargo new rust` once inside `week1`, then `cargo run --bin p01 < ../day01/p01_arithmetic/in.txt`

After each problem, replace ☐ with ✅ in that day's tracker and write the total minutes.

## Day 1 — Sun, Nov 22 · Setup + I/O and arithmetic

**Deliverable:** gcc, g++, python3 and Rust (via rustup) all working, plus P01–P03 in all 4 languages. **Rust concept of the day:** `let` vs `let mut`, reading stdin, `parse()`.

### P01 · Integer arithmetic

Read two integers `a b`. Print `a+b a-b a*b a/b a%b`.

- Input: `-7 2` → Output: `-5 -9 -14 -3 -1`
- Focus: C, C++ and Rust truncate division toward zero. Python floors it (`-7 // 2 = -4`, `-7 % 2 = 1`). Make the Python output match the others, and write a comment explaining why the results differ.

### P02 · Temperature conversion

Read a temperature in Celsius (decimal). Print it in Fahrenheit with 2 decimals: `F = C × 9/5 + 32`.

- Input: `37` → Output: `98.60`
- Focus: formatted output with `printf("%.2f")`, `std::fixed << std::setprecision(2)`, `f"{x:.2f}"` and `println!("{:.2}", x)`. Watch for `9/5` being integer division in C and C++.

### P03 · Swap via a function

Read `a b`. Swap them using a function, not inline, then print them.

- Input: `3 5` → Output: `5 3`
- Focus: C uses pointers (`int *`), C++ uses references (`int &`), Python returns a tuple, and Rust uses `&mut i32` (then try `std::mem::swap`). This is your first contact with borrowing.

| Problem | C | C++ | Python | Rust | Total min |
| --- | --- | --- | --- | --- | --- |
| P01 | ☐ | ☐ | ☐ | ☐ |  |
| P02 | ☐ | ☐ | ☐ | ☐ |  |
| P03 | ☐ | ☐ | ☐ | ☐ |  |

## Day 2 — Mon, Nov 23 · Conditionals and loops

**Deliverable:** P04–P06 in all 4 languages. **Rust concept of the day:** `if` is an expression, `for i in 1..=n`, `while`, `match` on simple values.

### P04 · FizzBuzz

Read `n`. For 1..n print `Fizz` for multiples of 3, `Buzz` for multiples of 5, `FizzBuzz` for both, otherwise the number.

- Input: `15` → last line: `FizzBuzz`
- Focus: check order matters (test 15 before 3 and 5). In Rust, write it once with `if/else` and once with `match (i % 3, i % 5)`.

### P05 · Leap year

Read a year. Print `Leap` or `Not leap`. Rule: divisible by 4, except centuries, unless divisible by 400.

- Input: `1900` → `Not leap` · `2000` → `Leap` · `2024` → `Leap`
- Focus: write it as one boolean expression. Test all three samples in every language.

### P06 · Reverse number and palindrome

Read a non-negative integer. Print its reverse and whether it is a palindrome.

- Input: `12321` → `12321 Palindrome` · `1230` → `321 Not palindrome`
- Focus: the `% 10` and `/ 10` loop, done arithmetically with no string conversion. In Rust, use `u64` and `let mut`.

| Problem | C | C++ | Python | Rust | Total min |
| --- | --- | --- | --- | --- | --- |
| P04 | ☐ | ☐ | ☐ | ☐ |  |
| P05 | ☐ | ☐ | ☐ | ☐ |  |
| P06 | ☐ | ☐ | ☐ | ☐ |  |

## Day 3 — Tue, Nov 24 · Number theory with loops

**Deliverable:** P07–P09 in all 4 languages, plus one timing comparison for P07. **Rust concept of the day:** `Vec<bool>`, `vec![true; n]`, integer overflow behavior, `checked_add`.

### P07 · Primes up to n (Sieve of Eratosthenes)

Read `n`. Print all primes ≤ n using a sieve.

- Input: `30` → `2 3 5 7 11 13 17 19 23 29`
- Analysis: the sieve is O(n log log n), while trial division of each number is O(n√n). Run both for n = 1,000,000 in C and Python and note the time difference.

### P08 · GCD and LCM

Read `a b`. Print `gcd lcm` using Euclid's algorithm. Write it both iteratively and recursively.

- Input: `12 18` → `6 36`
- Focus: compute LCM as `a / gcd * b`, not `a * b / gcd`. The first form avoids overflow for large inputs.

### P09 · Fibonacci and overflow

Read `n`. Print the first `n` Fibonacci numbers (F0 = 0, F1 = 1). Then find the largest k where F(k) fits in an unsigned 64-bit integer.

- Input: `10` → `0 1 1 2 3 5 8 13 21 34`
- Expected finding: k = 93.
- Focus: C wraps unsigned overflow silently, Rust panics in debug builds, and Python never overflows. In Rust, detect the limit with `checked_add` returning `None`.

| Problem | C | C++ | Python | Rust | Total min |
| --- | --- | --- | --- | --- | --- |
| P07 | ☐ | ☐ | ☐ | ☐ |  |
| P08 | ☐ | ☐ | ☐ | ☐ |  |
| P09 | ☐ | ☐ | ☐ | ☐ |  |

## Day 4 — Wed, Nov 25 · Functions and recursion

**Deliverable:** P10–P12 in all 4 languages. **Rust concept of the day:** function signatures with types, return without `;`, recursion with `u64`.

### P10 · Factorial

Read `n` (0 ≤ n ≤ 20). Print n! computed both iteratively and recursively.

- Input: `5` → `120` · `20` → `2432902008176640000`
- Analysis: 20! is the largest factorial that fits in 64 bits, and 21! overflows. Python has arbitrary-precision integers, so it has no limit. Note this in a comment.

### P11 · Fast power (modular exponentiation)

Read `x n m`. Print `x^n mod m` using binary exponentiation.

- Input: `2 10 1000` → `24`
- Analysis: the naive loop does n multiplications, binary exponentiation does about log₂(n). Try n = 10^18 and see which one finishes.

### P12 · Tower of Hanoi

Read `n`. Print every move as `Move disk k from A to C`, then the total count.

- Input: `3` → 7 moves
- Analysis: the move count is 2^n − 1. Confirm it from your program's output for n = 1 to 10.

| Problem | C | C++ | Python | Rust | Total min |
| --- | --- | --- | --- | --- | --- |
| P10 | ☐ | ☐ | ☐ | ☐ |  |
| P11 | ☐ | ☐ | ☐ | ☐ |  |
| P12 | ☐ | ☐ | ☐ | ☐ |  |

## Day 5 — Thu, Nov 26 · Arrays

**Deliverable:** P13–P15 in all 4 languages. **Rust concept of the day:** `Vec<i64>`, slices `&[i64]` and `&mut [i64]`, iterator methods (`iter().min()`, `sum()`).

### P13 · Min, max, sum, average

Read `n`, then `n` integers. Print `min max sum average` (average to 2 decimals).

- Input: `5` / `4 -2 9 0 7` → `-2 9 18 3.60`
- Focus: C uses a fixed array or `malloc`, C++ uses `std::vector`. In Rust, do it once with a manual loop and once with iterators, and compare the code length.

### P14 · Reverse an array in place

Read `n` integers and reverse them in place with two pointers, with no second array.

- Input: `1 2 3 4 5` → `5 4 3 2 1`
- Focus: in Rust, use `v.swap(i, j)`. Try writing `let a = &mut v[i]; let b = &mut v[j];` first and read the compiler error. It shows the borrowing rule: only one mutable reference at a time.

### P15 · Binary search

Read a sorted array and a target. Print the target's index, or `-1` if it is missing. Write the loop yourself.

- Input: `1 3 5 7 9 11` target `7` → `3` · target `4` → `-1`
- Analysis: compute `mid = lo + (hi - lo) / 2`, not `(lo + hi) / 2`, because the sum can overflow. Afterwards compare with the library versions: `bsearch`, `std::lower_bound`, `bisect`, `slice::binary_search`.

| Problem | C | C++ | Python | Rust | Total min |
| --- | --- | --- | --- | --- | --- |
| P13 | ☐ | ☐ | ☐ | ☐ |  |
| P14 | ☐ | ☐ | ☐ | ☐ |  |
| P15 | ☐ | ☐ | ☐ | ☐ |  |

## Day 6 — Fri, Nov 27 · Strings

**Deliverable:** P16–P18 in all 4 languages. **Rust concept of the day:** `String` vs `&str`, `.chars()`, `.trim()`, why `s[i]` doesn't compile.

### P16 · Palindrome string

Read a line. Print `true` if it is a palindrome when you ignore case and all non-alphanumeric characters.

- Input: `A man, a plan, a canal: Panama` → `true` · `race a car` → `false`
- Focus: C uses `isalnum` and `tolower` on a `char` array. Rust uses `is_alphanumeric()` and `to_ascii_lowercase()`. Use two pointers, not a reversed copy.

### P17 · Character classes

Read a full line. Count vowels, consonants, digits and spaces.

- Input: `Hello World 2026` → `vowels=3 consonants=7 digits=4 spaces=2`
- Focus: reading a full line is different in each language: `fgets`, `std::getline`, `input()`, `read_line`. `fgets` and `read_line` keep the trailing `\n`, so strip it before counting.

### P18 · Anagram check

Read two lowercase words. Print `Yes` if they are anagrams, else `No`.

- Input: `listen silent` → `Yes` · `rat car` → `No`
- Analysis: a 26-slot count array is O(n). Sorting both words is O(n log n). Implement the count array in all 4 languages, then the sort version in Python as a cross-check.

| Problem | C | C++ | Python | Rust | Total min |
| --- | --- | --- | --- | --- | --- |
| P16 | ☐ | ☐ | ☐ | ☐ |  |
| P17 | ☐ | ☐ | ☐ | ☐ |  |
| P18 | ☐ | ☐ | ☐ | ☐ |  |

## Day 7 — Sat, Nov 28 · Structs, 2D arrays, mini-project

**Deliverable:** P19–P21 in all 4 languages, plus the Week 1 checkpoint below. **Rust concept of the day:** `struct` + `impl`, `Vec<Vec<i64>>`, `enum` + `match`, `sort_by`.

### P19 · Matrix multiplication

Read `r1 c1` and matrix A, then `r2 c2` and matrix B. Print A × B, or `Invalid` if `c1 ≠ r2`.

- Input: A = `[[1,2],[3,4]]`, B = `[[5,6],[7,8]]` → `19 22` / `43 50`
- Analysis: three nested loops give O(r1 · c1 · c2). In C, use a 2D array with fixed max size; in Rust, `vec![vec![0; c2]; r1]`.

### P20 · Student records

Read `n` students as `name roll marks`. Assign grades: ≥ 90 A, ≥ 75 B, ≥ 60 C, else F. Print them sorted by marks, highest first.

- Input: `Asha 1 82` / `Ravi 2 95` / `Meera 3 58` → `Ravi 2 95 A` / `Asha 1 82 B` / `Meera 3 58 F`
- Focus: C uses `struct` + `qsort` with a comparator, C++ uses `struct` + `std::sort` with a lambda, Python uses a class or tuple with `sorted(key=...)`, Rust uses `struct` + `impl` with a `grade()` method + `sort_by`.

### P21 · Mini-project: bank account

Read commands until `Q`: `D amt` deposits, `W amt` withdraws, `B` prints the balance. A withdrawal larger than the balance prints `Insufficient` and changes nothing.

- Input: `D 500` / `W 200` / `W 400` / `B` / `Q` → `Insufficient` / `300`
- Focus: this combines loops, conditionals, functions and a struct. In Rust, parse each line into an `enum Command { Deposit(i64), Withdraw(i64), Balance, Quit }` and `match` on it. Week 2 builds on this pattern.

| Problem | C | C++ | Python | Rust | Total min |
| --- | --- | --- | --- | --- | --- |
| P19 | ☐ | ☐ | ☐ | ☐ |  |
| P20 | ☐ | ☐ | ☐ | ☐ |  |
| P21 | ☐ | ☐ | ☐ | ☐ |  |

## Week 1 checkpoint (Sat, Nov 28)

Share these three things with me, and I'll build Week 2 from them:

1. **Completion:** how many of the 84 solutions you finished.
2. **Average minutes per problem for each language,** taken from the daily trackers.
3. **Where you got stuck:** which problems needed a hint, and which Rust compiler errors cost you the most time (borrowing, types, `String`/`&str`, etc.).

How Week 2 adapts:

| Result | Week 2 adjustment |
| --- | --- |
| ≥ 90% done and Rust ≤ 15 min/problem | Go straight to data structures at medium difficulty, 3 problems/day |
| 70–90% done or Rust 15–25 min | Each day: 1 consolidation problem + 2 new ones |
| < 70% done or Rust > 25 min | Repeat the Week 1 topics with new problems, plus focused Rust ownership drills |
| Everything felt easy (< 30 min/problem in total) | 4 problems/day, LeetCode-medium level |

## Tentative roadmap (adjusted after each checkpoint)

| Week | Dates | Topics | Rust focus |
| --- | --- | --- | --- |
| 1 | Nov 22 – Nov 28 | Basics: I/O, loops, functions, arrays, strings, structs | Mutability, borrowing, `String`/`&str`, structs, enums |
| 2 | Nov 29 – Dec 5 | Pointers and dynamic memory, sorting (insertion, merge, quick), linked lists, stacks, queues | `Box`, `Option`, ownership inside data structures |
| 3 | Dec 6 – Dec 12 | Hashing, two pointers, sliding window, recursion and backtracking, binary trees, BST, heaps | `HashMap`, traits, `Rc`/`RefCell` |
| 4 | Dec 13 – Dec 19 | Graphs (BFS, DFS, Dijkstra), dynamic programming, greedy | Generics, iterators, `Result` |
| Final | Dec 20 – Dec 21 | Capstone: one small CLI project in all 4 languages + review | Modules, file I/O |
