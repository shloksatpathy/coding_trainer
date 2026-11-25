n = int(input())
a = []
for w in input().split():
    a.append(int(w))
a.sort()
print(" ".join(str(x) for x in a))
a.reverse()
print(" ".join(str(x) for x in a))
