n = int(input())
a = []
for w in input().split():
    a.append(int(w))
here = a[0]
best = a[0]
for i in range(1, n):
    if here > 0:
        here += a[i]
    else:
        here = a[i]
    if here > best:
        best = here
print(best)
