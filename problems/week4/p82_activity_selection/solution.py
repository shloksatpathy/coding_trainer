n = int(input())
acts = sorted((tuple(map(int, input().split())) for _ in range(n)), key=lambda a: a[1])
count, last = 0, float("-inf")
for s, e in acts:
    if s >= last:
        count += 1
        last = e
print(count)
