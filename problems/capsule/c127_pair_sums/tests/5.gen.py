import random

random.seed(127)
n = 200000
values = sorted(random.sample(range(-10**8, 10**8), n))
print(n, values[1000] + values[-1000])
print(" ".join(map(str, values)))
