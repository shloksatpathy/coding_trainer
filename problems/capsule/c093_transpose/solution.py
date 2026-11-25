r, c = map(int, input().split())
g = []
for i in range(r):
    row = []
    for w in input().split():
        row.append(int(w))
    g.append(row)
for j in range(c):
    for i in range(r):
        if i > 0:
            print(" ", end="")
        print(g[i][j], end="")
    print()
