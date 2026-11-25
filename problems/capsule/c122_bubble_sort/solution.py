n = int(input())
a = []
for w in input().split():
    a.append(int(w))
swaps = 0
swapped = True
while swapped:
    swapped = False
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            t = a[i]
            a[i] = a[i + 1]
            a[i + 1] = t
            swaps += 1
            swapped = True
for i in range(n):
    if i > 0:
        print(" ", end="")
    print(a[i], end="")
print()
print(f"swaps: {swaps}")
