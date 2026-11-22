n = int(input())
a = list(map(int, input().split()))
w = 1
for r in range(1, n):
    if a[r] != a[w - 1]:
        a[w] = a[r]
        w += 1
print(w)
print(*a[:w])
