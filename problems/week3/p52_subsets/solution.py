n = int(input())
cur = []

def choose(start):
    for i in range(start, n + 1):
        cur.append(i)
        print(*cur)
        choose(i + 1)
        cur.pop()

choose(1)
