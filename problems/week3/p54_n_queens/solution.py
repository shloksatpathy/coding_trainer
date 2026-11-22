n = int(input())
cols, d1, d2 = [False] * n, [False] * (2 * n), [False] * (2 * n)
cur, first, count = [], [], 0

def place(r):
    global count, first
    if r == n:
        count += 1
        if not first:
            first = [c + 1 for c in cur]
        return
    for c in range(n):
        if not cols[c] and not d1[r + c] and not d2[r - c + n]:
            cols[c] = d1[r + c] = d2[r - c + n] = True
            cur.append(c)
            place(r + 1)
            cur.pop()
            cols[c] = d1[r + c] = d2[r - c + n] = False

place(0)
print(count)
print(*first if first else ["None"])
