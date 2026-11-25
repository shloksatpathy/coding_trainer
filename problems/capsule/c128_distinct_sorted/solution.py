n = int(input())
a = []
for w in input().split():
    a.append(int(w))
k = 0
for i in range(n):
    if i == 0 or a[i] != a[i - 1]:
        if k > 0:
            print(" ", end="")
        print(a[i], end="")
        k += 1
print()
print(f"distinct: {k}")
