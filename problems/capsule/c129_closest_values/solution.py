n = int(input())
a = []
for w in input().split():
    a.append(int(w))
a.sort()
best = a[1] - a[0]
for i in range(2, n):
    if a[i] - a[i - 1] < best:
        best = a[i] - a[i - 1]
print(best)
