r, c = map(int, input().split())
g = []
for i in range(r):
    g.append(input())
total = 0
for i in range(r):
    count = 0
    for j in range(c):
        if g[i][j] == "#":
            count += 1
    print(count)
    total += count
print(f"total: {total}")
