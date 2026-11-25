g = []
for i in range(3):
    g.append(input())


def wins(p):
    for i in range(3):
        if g[i][0] == p and g[i][1] == p and g[i][2] == p:
            return True
        if g[0][i] == p and g[1][i] == p and g[2][i] == p:
            return True
    if g[0][0] == p and g[1][1] == p and g[2][2] == p:
        return True
    return g[0][2] == p and g[1][1] == p and g[2][0] == p


full = True
for row in g:
    for ch in row:
        if ch == ".":
            full = False
if wins("X"):
    print("X wins")
elif wins("O"):
    print("O wins")
elif full:
    print("draw")
else:
    print("in progress")
