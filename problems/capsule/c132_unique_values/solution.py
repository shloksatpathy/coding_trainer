n = int(input())
a = []
for w in input().split():
    a.append(int(w))
seen = set()
out = []
for x in a:
    if x not in seen:
        seen.add(x)
        out.append(str(x))
print(" ".join(out))
print(f"distinct: {len(out)}")
