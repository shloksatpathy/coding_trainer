from collections import deque
r, c = map(int, input().split())
g = [input() for _ in range(r)]
dist = [[-1] * c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if g[i][j] == "S":
            dist[i][j] = 0
            q = deque([(i, j)])
ans = -1
while q:
    x, y = q.popleft()
    if g[x][y] == "E":
        ans = dist[x][y]
        break
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        a, b = x + dx, y + dy
        if 0 <= a < r and 0 <= b < c and g[a][b] != "#" and dist[a][b] == -1:
            dist[a][b] = dist[x][y] + 1
            q.append((a, b))
print(ans)
