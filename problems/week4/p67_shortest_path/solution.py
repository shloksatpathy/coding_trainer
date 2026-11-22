from collections import deque
n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
s, t = map(int, input().split())
for a in adj:
    a.sort()
parent = [0] * (n + 1)
dist = [-1] * (n + 1)
dist[s] = 0
q = deque([s])
while q:
    u = q.popleft()
    for v in adj[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            parent[v] = u
            q.append(v)
print(dist[t])
if dist[t] != -1:
    path = [t]
    while path[-1] != s:
        path.append(parent[path[-1]])
    print(*reversed(path))
