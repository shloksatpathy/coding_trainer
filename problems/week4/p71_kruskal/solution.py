n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))
parent = list(range(n + 1))

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

total = used = 0
for w, u, v in sorted(edges):
    a, b = find(u), find(v)
    if a != b:
        parent[a] = b
        total += w
        used += 1
print(total if used == n - 1 else "Disconnected")
