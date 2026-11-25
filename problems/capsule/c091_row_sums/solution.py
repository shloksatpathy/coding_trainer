r, c = map(int, input().split())
g = []
for i in range(r):
    row = []
    for w in input().split():
        row.append(int(w))
    g.append(row)
for i in range(r):
    total = 0
    for j in range(c):
        if j > 0:
            print(" ", end="")
        print(g[i][j], end="")
        total += g[i][j]
    print(f" | {total}")
