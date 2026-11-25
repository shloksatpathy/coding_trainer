n = int(input())
a = []
for w in input().split():
    a.append(int(w))
total = 0
for i in range(n):
    total += a[i]
    if i > 0:
        print(" ", end="")
    print(total, end="")
print()
