# P22 · Growable array

Read `n` (n ≥ 1), then `n` integers. Store them in a dynamic array you grow yourself: start with capacity 1 and double the capacity whenever it is full, copying the old elements into the new block.

Print the elements on line 1, then `capacity=K copies=X` on line 2, where X is the total number of element copies done while growing.

**Focus:** C uses `malloc`/`realloc` (or `malloc` + manual copy + `free`), C++ uses `new[]`/`delete[]` (no `std::vector`), Python preallocates `[None] * cap` and copies into a bigger list, Rust uses `Vec::with_capacity` and copies by hand. **Analysis:** copies stay below 2n — that is why `push_back` is amortized O(1).

**Sample input** (also in `in.txt`):
```
5
3 1 4 1 5
```
