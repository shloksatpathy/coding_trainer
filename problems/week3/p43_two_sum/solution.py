n, target = map(int, input().split())
a = list(map(int, input().split()))
seen = {}
for j, x in enumerate(a):
    if target - x in seen:
        print(seen[target - x], j)
        break
    seen.setdefault(x, j)
