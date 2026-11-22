from collections import deque
n, k = map(int, input().split())
q = deque(range(1, n + 1))
order = []
while q:
    q.rotate(-(k - 1))
    order.append(q.popleft())
print(*order)
