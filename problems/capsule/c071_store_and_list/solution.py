n = int(input())
a = []
for w in input().split():
    a.append(int(w))
for i in range(n):
    print(f"{i + 1}: {a[i]}")
