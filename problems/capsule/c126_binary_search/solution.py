n = int(input())
a = []
for w in input().split():
    a.append(int(w))
q = int(input())
for w in input().split():
    x = int(w)
    lo = 0
    hi = n - 1
    pos = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == x:
            pos = mid + 1
            break
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    print(pos)
