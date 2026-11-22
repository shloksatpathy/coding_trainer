import heapq
n, k = map(int, input().split())
heap = []
for x in map(int, input().split()):
    heapq.heappush(heap, x)
    if len(heap) > k:
        heapq.heappop(heap)
print(*sorted(heap, reverse=True))
