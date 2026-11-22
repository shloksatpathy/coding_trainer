from collections import deque
n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
color = [-1] * (n + 1)
ok = True
for s in range(1, n + 1):
    if color[s] != -1:
        continue
    color[s] = 0
    q = deque([s])
    while q and ok:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = 1 - color[u]
                q.append(v)
            elif color[v] == color[u]:
                ok = False
print("Yes" if ok else "No")
