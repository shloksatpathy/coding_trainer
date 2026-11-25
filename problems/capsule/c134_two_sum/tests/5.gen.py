import random

random.seed(134)
n = 200000
values = random.sample(range(-10**9, 10**9), n)
print(n, values[-3] + values[-1])
print(" ".join(map(str, values)))
