n = int(input())
a = []
for w in input().split():
    a.append(int(w))
for i in range(n // 2):
    t = a[i]
    a[i] = a[n - 1 - i]
    a[n - 1 - i] = t
for i in range(n):
    if i > 0:
        print(" ", end="")
    print(a[i], end="")
print()
