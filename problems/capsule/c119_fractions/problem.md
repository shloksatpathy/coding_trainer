# C119 · Fractions

The input is two fractions `a/b c/d` with positive whole numbers. Store each in a `Fraction` record and write `add(f, g)`, which returns their sum in lowest terms (divide the top and bottom by their greatest common divisor). Print it as `p/q`, even when q is 1.

**Example**

Input (also in `in.txt`):
```
1/2 1/3
```
Output:
```
5/6
```

**Focus:** a function that builds and returns a new record; the greatest common divisor comes from Euclid's rule: gcd(a, b) = gcd(b, a % b), and gcd(a, 0) = a.
