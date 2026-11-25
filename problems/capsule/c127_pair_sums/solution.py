n, t = map(int, input().split())
a = []
for w in input().split():
    a.append(int(w))
i = 0
j = n - 1
found = 0
while i < j:
    s = a[i] + a[j]
    if s == t:
        print(a[i], a[j])
        found += 1
        i += 1
        j -= 1
    elif s < t:
        i += 1
    else:
        j -= 1
if found == 0:
    print("none")
