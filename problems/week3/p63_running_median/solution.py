import heapq
n = int(input())
low, high = [], []
out = []
for x in map(int, input().split()):
    heapq.heappush(low, -x)
    heapq.heappush(high, -heapq.heappop(low))
    if len(high) > len(low):
        heapq.heappush(low, -heapq.heappop(high))
    if len(low) > len(high):
        out.append(f"{-low[0]:.1f}")
    else:
        out.append(f"{(-low[0] + high[0]) / 2:.1f}")
print("\n".join(out))
