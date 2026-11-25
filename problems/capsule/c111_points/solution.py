from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


x1, y1, x2, y2 = map(int, input().split())
p = Point(x1, y1)
q = Point(x2, y2)
dx = q.x - p.x
dy = q.y - p.y
print(f"dx: {dx}")
print(f"dy: {dy}")
print(f"manhattan: {abs(dx) + abs(dy)}")
