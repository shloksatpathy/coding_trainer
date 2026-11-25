n = int(input())
a = []
for w in input().split():
    a.append(int(w))
m = int(input())
b = []
for w in input().split():
    b.append(int(w))
out = []
i = 0
j = 0
while i < n or j < m:
    if j == m or (i < n and a[i] <= b[j]):
        out.append(a[i])
        i += 1
    else:
        out.append(b[j])
        j += 1
print(" ".join(str(x) for x in out))
