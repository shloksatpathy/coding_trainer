import random

R = random.Random(71)
n, m = 3000, 20000
edges = set()
while len(edges) < m:
    u, v = R.randint(1, n), R.randint(1, n)
    if u != v:
        edges.add((min(u, v), max(u, v)))
print(n, m)
for u, v in sorted(edges):
    print(u, v, R.randint(1, 1000000))
