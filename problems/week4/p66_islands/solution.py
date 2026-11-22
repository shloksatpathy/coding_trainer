from collections import deque
r, c = map(int, input().split())
g = [list(input()) for _ in range(r)]
count = 0
for i in range(r):
    for j in range(c):
        if g[i][j] == "#":
            count += 1
            g[i][j] = "."
            q = deque([(i, j)])
            while q:
                x, y = q.popleft()
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    a, b = x + dx, y + dy
                    if 0 <= a < r and 0 <= b < c and g[a][b] == "#":
                        g[a][b] = "."
                        q.append((a, b))
print(count)
