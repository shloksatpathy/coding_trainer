import random

R = random.Random(82)
n = 100000
print(n)
for _ in range(n):
    s = R.randint(0, 10**6)
    print(s, s + R.randint(1, 5000))
