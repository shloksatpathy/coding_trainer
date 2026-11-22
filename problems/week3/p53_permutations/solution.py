n = int(input())
a = sorted(map(int, input().split()))
used = [False] * n
cur = []

def go():
    if len(cur) == n:
        print(*cur)
        return
    for i in range(n):
        if not used[i]:
            used[i] = True
            cur.append(a[i])
            go()
            cur.pop()
            used[i] = False

go()
