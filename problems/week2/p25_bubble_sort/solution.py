n = int(input())
a = list(map(int, input().split()))
swaps = passes = 0
for i in range(n - 1):
    passes += 1
    swapped = False
    for j in range(n - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            swaps += 1
            swapped = True
    if not swapped:
        break
print(*a)
print(f"swaps={swaps} passes={passes}")
