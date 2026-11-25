def count(a, i, left):
    if i == len(a):
        if left == 0:
            return 1
        return 0
    return count(a, i + 1, left) + count(a, i + 1, left - a[i])


n, t = map(int, input().split())
a = []
for w in input().split():
    a.append(int(w))
print(count(a, 0, t))
