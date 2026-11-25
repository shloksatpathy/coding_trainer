from dataclasses import dataclass


@dataclass
class Line:
    name: str
    total: int
    qty: int


def money(cents):
    return f"{cents // 100}.{cents % 100:02d}"


n = int(input())
lines = []
grand = 0
for i in range(n):
    name, price, qty = input().split()
    lines.append(Line(name, int(price) * int(qty), int(qty)))
    grand += int(price) * int(qty)
lines.sort(key=lambda x: (-x.total, x.name))
for x in lines:
    print(f"{x.name:<10}{x.qty:>5}{money(x.total):>10}")
print(f"{'TOTAL':<15}{money(grand):>10}")
