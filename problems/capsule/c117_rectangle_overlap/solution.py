from dataclasses import dataclass


@dataclass
class Rect:
    x1: int
    y1: int
    x2: int
    y2: int


def overlap_area(a, b):
    w = min(a.x2, b.x2) - max(a.x1, b.x1)
    h = min(a.y2, b.y2) - max(a.y1, b.y1)
    if w <= 0 or h <= 0:
        return 0
    return w * h


r = []
for i in range(2):
    x1, y1, x2, y2 = map(int, input().split())
    r.append(Rect(x1, y1, x2, y2))
print(overlap_area(r[0], r[1]))
