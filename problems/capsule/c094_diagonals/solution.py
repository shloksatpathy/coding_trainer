n = int(input())
g = []
for i in range(n):
    row = []
    for w in input().split():
        row.append(int(w))
    g.append(row)
main = 0
anti = 0
for i in range(n):
    main += g[i][i]
    anti += g[i][n - 1 - i]
print(f"main: {main}")
print(f"anti: {anti}")
