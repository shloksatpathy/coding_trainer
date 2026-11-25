def perm(cur, used, n):
    if len(cur) == n:
        for i in range(n):
            if i > 0:
                print(" ", end="")
            print(cur[i], end="")
        print()
        return
    for x in range(1, n + 1):
        if not used[x]:
            used[x] = True
            cur.append(x)
            perm(cur, used, n)
            cur.pop()
            used[x] = False


n = int(input())
perm([], [False] * (n + 1), n)
