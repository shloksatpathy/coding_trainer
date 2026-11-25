r, c = map(int, input().split())
g = []
for i in range(r):
    g.append(input())
moves = input()
row = 0
col = 0
moved = 0
for m in moves:
    nr = row
    nc = col
    if m == "U":
        nr -= 1
    elif m == "D":
        nr += 1
    elif m == "L":
        nc -= 1
    else:
        nc += 1
    if nr >= 0 and nr < r and nc >= 0 and nc < c and g[nr][nc] == ".":
        row = nr
        col = nc
        moved += 1
print(f"at {row + 1} {col + 1}")
print(f"moved: {moved}")
