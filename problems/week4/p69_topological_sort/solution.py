import heapq
n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
indeg = [0] * (n + 1)
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    indeg[v] += 1
heap = [u for u in range(1, n + 1) if indeg[u] == 0]
heapq.heapify(heap)
order = []
while heap:
    u = heapq.heappop(heap)
    order.append(u)
    for v in adj[u]:
        indeg[v] -= 1
        if indeg[v] == 0:
            heapq.heappush(heap, v)
print(*order if len(order) == n else ["Cycle"])
