import sys
sys.setrecursionlimit(20000)
n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
s = int(input())
for a in adj:
    a.sort()
seen = [False] * (n + 1)
order = []

def dfs(u):
    seen[u] = True
    order.append(u)
    for v in adj[u]:
        if not seen[v]:
            dfs(v)

dfs(s)
print(*order)
comps = 1
for u in range(1, n + 1):
    if not seen[u]:
        comps += 1
        dfs(u)
print(f"components={comps}")
