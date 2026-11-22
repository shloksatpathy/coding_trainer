a, b = map(int, input().split())
# Python's // floors toward -infinity; C/C++/Rust truncate toward zero.
q = abs(a) // abs(b) * (1 if (a < 0) == (b < 0) else -1)
r = a - b * q
print(a + b, a - b, a * b, q, r)
