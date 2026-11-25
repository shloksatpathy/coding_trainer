n = int(input())
a = []
for w in input().split():
    a.append(int(w))
count = [0] * 10
for v in a:
    count[v] += 1
for v in range(10):
    if count[v] > 0:
        print(f"{v}: {count[v]}")
