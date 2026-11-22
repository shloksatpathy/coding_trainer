n = int(input())
h = list(map(int, input().split()))
lo, hi, best = 0, n - 1, 0
while lo < hi:
    best = max(best, min(h[lo], h[hi]) * (hi - lo))
    if h[lo] < h[hi]:
        lo += 1
    else:
        hi -= 1
print(best)
