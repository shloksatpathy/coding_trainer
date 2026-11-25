n = int(input())
groups = {}
for w in input().split():
    key = "".join(sorted(w))
    if key not in groups:
        groups[key] = []
    groups[key].append(w)
for key in groups:
    print(" ".join(groups[key]))
