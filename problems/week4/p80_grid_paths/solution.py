MOD = 10 ** 9 + 7
r, c = map(int, input().split())
g = [input() for _ in range(r)]
row = [0] * c
for i in range(r):
    for j in range(c):
        if g[i][j] == "#":
            row[j] = 0
        elif i == 0 and j == 0:
            row[j] = 1
        elif j > 0:
            row[j] = (row[j] + row[j - 1]) % MOD
print(row[-1])
