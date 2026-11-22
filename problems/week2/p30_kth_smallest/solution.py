import random
n, k = map(int, input().split())
a = list(map(int, input().split()))
lo, hi, k = 0, n - 1, k - 1
while True:
    r = random.randint(lo, hi)
    a[r], a[hi] = a[hi], a[r]
    pivot, i = a[hi], lo
    for j in range(lo, hi):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[hi] = a[hi], a[i]
    if i == k:
        print(a[i])
        break
    if i < k:
        lo = i + 1
    else:
        hi = i - 1
