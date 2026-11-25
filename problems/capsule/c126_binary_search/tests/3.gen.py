import random

random.seed(126)
n = 200000
values = sorted(random.sample(range(-10**9, 10**9), n))
print(n)
print(" ".join(map(str, values)))
q = 200000
print(q)
print(" ".join(str(random.choice(values) if random.random() < 0.5 else random.randint(-10**9, 10**9)) for _ in range(q)))
