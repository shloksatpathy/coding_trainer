n = int(input())
a = sorted(map(int, input().split()))
found = False
for i in range(n - 2):
    if i > 0 and a[i] == a[i - 1]:
        continue
    lo, hi = i + 1, n - 1
    while lo < hi:
        s = a[i] + a[lo] + a[hi]
        if s < 0:
            lo += 1
        elif s > 0:
            hi -= 1
        else:
            print(a[i], a[lo], a[hi])
            found = True
            while lo < hi and a[lo] == a[lo + 1]:
                lo += 1
            lo += 1
            hi -= 1
if not found:
    print("None")
