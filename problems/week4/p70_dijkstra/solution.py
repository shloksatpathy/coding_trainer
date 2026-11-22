import heapq
n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
s = int(input())
INF = float("inf")
dist = [INF] * (n + 1)
dist[s] = 0
heap = [(0, s)]
while heap:
    d, u = heapq.heappop(heap)
    if d > dist[u]:
        continue
    for v, w in adj[u]:
        if d + w < dist[v]:
            dist[v] = d + w
            heapq.heappush(heap, (dist[v], v))
print(*["INF" if d == INF else d for d in dist[1:]])
