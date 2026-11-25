import random

random.seed(130)
for size in (100000, 100000):
    print(size)
    print(" ".join(map(str, sorted(random.randint(-10**9, 10**9) for _ in range(size)))))
