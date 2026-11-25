import random

random.seed(140)
n = 200000
print(n)
print(" ".join(str(random.randint(1, 60000) * 16661 - 10**9) for _ in range(n)))
