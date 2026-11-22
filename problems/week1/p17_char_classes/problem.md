# P17 · Character classes

Read a full line. Count vowels, consonants (other ASCII letters), digits and spaces. Print `vowels=V consonants=C digits=D spaces=S`.

**Focus:** reading a full line is different in each language: `fgets`, `std::getline`, `input()`, `read_line`. `fgets` and `read_line` keep the trailing `\n`, so strip it before counting.

**Sample input** (also in `in.txt`):
```
Hello World 2026
```
