n, k = map(int, input().split())
a = list(map(int, input().split()))
s = best = sum(a[:k])
for i in range(k, n):
    s += a[i] - a[i - k]
    best = max(best, s)
print(best)
