r, c = map(int, input().split())
g = []
for i in range(r):
    row = []
    for w in input().split():
        row.append(int(w))
    g.append(row)
for j in range(c):
    total = 0
    for i in range(r):
        total += g[i][j]
    if j > 0:
        print(" ", end="")
    print(total, end="")
print()
