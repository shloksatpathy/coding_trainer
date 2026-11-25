n = int(input())
a = []
for w in input().split():
    a.append(int(w))
p = [0]
for x in a:
    p.append(p[-1] + x)
q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    print(p[r] - p[l - 1])
