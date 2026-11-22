import random

R = random.Random(685)
r, c = 400, 400
g = [["#" if R.random() < 0.25 else "." for _ in range(c)] for _ in range(r)]
g[0][0], g[r - 1][c - 1] = "S", "E"
print(r, c)
print("\n".join("".join(row) for row in g))
