from dataclasses import dataclass


@dataclass
class Item:
    id: str
    qty: int


def find(items, key):
    for i in range(len(items)):
        if items[i].id == key:
            return i
    return -1


n = int(input())
items = []
for i in range(n):
    key, qty = input().split()
    items.append(Item(key, int(qty)))
m = int(input())
for i in range(m):
    key, change = input().split()
    k = find(items, key)
    if k == -1:
        print(f"unknown {key}")
    else:
        items[k].qty += int(change)
for it in items:
    print(f"{it.id}: {it.qty}")
