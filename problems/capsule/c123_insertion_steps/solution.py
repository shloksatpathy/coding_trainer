n = int(input())
a = []
for w in input().split():
    a.append(int(w))
for i in range(1, n):
    x = a[i]
    j = i - 1
    while j >= 0 and a[j] > x:
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = x
    for i in range(n):
        if i > 0:
            print(" ", end="")
        print(a[i], end="")
    print()
