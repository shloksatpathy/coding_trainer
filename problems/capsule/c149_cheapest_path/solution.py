r, c = map(int, input().split())
g = []
for i in range(r):
    row = []
    for w in input().split():
        row.append(int(w))
    g.append(row)
best = []
for i in range(r):
    best.append([0] * c)
for i in range(r):
    for j in range(c):
        if i == 0 and j == 0:
            best[i][j] = g[i][j]
        elif i == 0:
            best[i][j] = best[i][j - 1] + g[i][j]
        elif j == 0:
            best[i][j] = best[i - 1][j] + g[i][j]
        else:
            best[i][j] = min(best[i - 1][j], best[i][j - 1]) + g[i][j]
print(best[r - 1][c - 1])
