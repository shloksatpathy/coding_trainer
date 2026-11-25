import random

random.seed(133)
n = 200000
values = random.sample(range(-10**9, 10**9), n - 1)
values.append(values[5])
print(n)
print(" ".join(map(str, values)))
