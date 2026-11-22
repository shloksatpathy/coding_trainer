a, b = input().split()
prev = list(range(len(b) + 1))
for i, ca in enumerate(a, 1):
    cur = [i]
    for j, cb in enumerate(b, 1):
        if ca == cb:
            cur.append(prev[j - 1])
        else:
            cur.append(1 + min(prev[j], cur[j - 1], prev[j - 1]))
    prev = cur
print(prev[-1])
