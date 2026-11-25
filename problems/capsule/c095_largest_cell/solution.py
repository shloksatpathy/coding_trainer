r, c = map(int, input().split())
g = []
for i in range(r):
    row = []
    for w in input().split():
        row.append(int(w))
    g.append(row)
best = g[0][0]
br = 0
bc = 0
for i in range(r):
    for j in range(c):
        if g[i][j] > best:
            best = g[i][j]
            br = i
            bc = j
print(f"max: {best} at {br + 1} {bc + 1}")
