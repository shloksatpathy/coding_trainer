n = int(input())
count = {}
for w in input().split():
    count[w] = count.get(w, 0) + 1
for w in count:
    print(f"{w}: {count[w]}")
