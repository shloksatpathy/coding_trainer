r, c = map(int, input().split())
g = []
for i in range(r):
    g.append(input())
for i in range(r):
    for j in range(c):
        if g[i][j] == "*":
            print("*", end="")
            continue
        count = 0
        for di in range(-1, 2):
            for dj in range(-1, 2):
                ni = i + di
                nj = j + dj
                if ni >= 0 and ni < r and nj >= 0 and nj < c and g[ni][nj] == "*":
                    count += 1
        print(count, end="")
    print()
