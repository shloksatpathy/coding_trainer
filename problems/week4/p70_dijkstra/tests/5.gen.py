import random

R = random.Random(70)
n, m = 5000, 30000
edges = set()
while len(edges) < m:
    u, v = R.randint(1, n), R.randint(1, n)
    if u != v:
        edges.add((u, v))
print(n, m)
for u, v in sorted(edges):
    print(u, v, R.randint(0, 1000000))
print(1)
