n, s = map(int, input().split())
a = list(map(int, input().split()))
lo = total = 0
best = n + 1
for hi in range(n):
    total += a[hi]
    while total >= s:
        best = min(best, hi - lo + 1)
        total -= a[lo]
        lo += 1
print(best if best <= n else 0)
