# P20 · Student records

Read `n`, then `n` lines `name roll marks`. Assign grades: ≥ 90 A, ≥ 75 B, ≥ 60 C, else F. Print `name roll marks grade` sorted by marks, highest first; break ties by roll number ascending.

Sample input:
```
3
Asha 1 82
Ravi 2 95
Meera 3 58
```
Output:
```
Ravi 2 95 A
Asha 1 82 B
Meera 3 58 F
```

**Focus:** C uses `struct` + `qsort` with a comparator, C++ uses `struct` + `std::sort` with a lambda, Python uses a class or tuple with `sorted(key=...)`, Rust uses `struct` + `impl` with a `grade()` method + `sort_by`.

**Sample input** (also in `in.txt`):
```
3
Asha 1 82
Ravi 2 95
Meera 3 58
```
