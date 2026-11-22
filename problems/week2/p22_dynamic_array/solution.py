n = int(input())
vals = list(map(int, input().split()))
cap, size, copies = 1, 0, 0
arr = [None] * cap
for v in vals:
    if size == cap:
        bigger = [None] * (cap * 2)
        for i in range(size):
            bigger[i] = arr[i]
        copies += size
        arr, cap = bigger, cap * 2
    arr[size] = v
    size += 1
print(*arr[:size])
print(f"capacity={cap} copies={copies}")
