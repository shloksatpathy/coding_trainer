n, t = map(int, input().split())
a = []
for w in input().split():
    a.append(int(w))
first = {}
answer = "none"
for j in range(n):
    if t - a[j] in first:
        answer = f"{first[t - a[j]] + 1} {j + 1}"
        break
    if a[j] not in first:
        first[a[j]] = j
print(answer)
