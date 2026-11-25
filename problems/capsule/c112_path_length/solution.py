import math
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


def distance(p, q):
    return math.sqrt((q.x - p.x) ** 2 + (q.y - p.y) ** 2)


n = int(input())
pts = []
for i in range(n):
    x, y = map(int, input().split())
    pts.append(Point(x, y))
total = 0
for i in range(1, n):
    total += distance(pts[i - 1], pts[i])
print(f"{total:.2f}")
