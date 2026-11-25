n = int(input())
a = []
for w in input().split():
    a.append(int(w))
seen = set()
answer = "none"
for x in a:
    if x in seen:
        answer = x
        break
    seen.add(x)
print(answer)
