r, c = map(int, input().split())
g = []
for i in range(r):
    g.append(input())
for j in range(c):
    for k in range(r):
        print(g[r - 1 - k][j], end="")
    print()
