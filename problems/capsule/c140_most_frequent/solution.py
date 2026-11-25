n = int(input())
a = []
for w in input().split():
    a.append(int(w))
count = {}
for x in a:
    count[x] = count.get(x, 0) + 1
best = None
for x in count:
    if best is None or count[x] > count[best] or (count[x] == count[best] and x < best):
        best = x
print(f"value: {best}")
print(f"count: {count[best]}")
print(f"distinct: {len(count)}")
