import random

R = random.Random(80)
r, c = 500, 500
g = [["#" if R.random() < 0.05 else "." for _ in range(c)] for _ in range(r)]
print(r, c)
print("\n".join("".join(row) for row in g))
