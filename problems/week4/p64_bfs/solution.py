from collections import deque
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
seen[s] = True
q, order = deque([s]), []
while q:
    u = q.popleft()
    order.append(u)
    for v in adj[u]:
        if not seen[v]:
            seen[v] = True
            q.append(v)
print(*order)
