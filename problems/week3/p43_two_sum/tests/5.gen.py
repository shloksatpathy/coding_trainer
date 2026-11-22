import random

# Every value is a multiple of 4 except one 1 and one 5, so 1 + 5 = 6 is the only pair summing to 6.
R = random.Random(43)
n = 100000
a = [4 * R.randint(-250000, 250000) for _ in range(n)]
a[R.randint(0, 49999)] = 1
a[R.randint(50000, 99999)] = 5
print(n, 6)
print(*a)
