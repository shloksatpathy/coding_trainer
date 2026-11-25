def total(a, i):
    if i == len(a):
        return 0
    return a[i] + total(a, i + 1)


n = int(input())
a = []
for w in input().split():
    a.append(int(w))
print(total(a, 0))
