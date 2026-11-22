n, W = map(int, input().split())
best = [0] * (W + 1)
for _ in range(n):
    w, v = map(int, input().split())
    for c in range(W, w - 1, -1):
        best[c] = max(best[c], best[c - w] + v)
print(best[W])
