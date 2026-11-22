counts = {}
for w in input().split():
    counts[w] = counts.get(w, 0) + 1
for w, c in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
    print(w, c)
