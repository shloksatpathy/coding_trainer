n = int(input())
a = []
for w in input().split():
    a.append(int(w))
q = int(input())
for w in input().split():
    x = int(w)
    pos = -1
    for i in range(n):
        if a[i] == x:
            pos = i + 1
            break
    print(pos)
