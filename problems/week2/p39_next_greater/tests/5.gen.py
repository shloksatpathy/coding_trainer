import random

# A long descending run, then one larger value: the O(n^2) scan has to read to the end for every element.
R = random.Random(39)
n = 100000
a = sorted((R.randint(0, 10**6) for _ in range(n - 1)), reverse=True)
print(n)
print(*a, 10**6 + 1)
