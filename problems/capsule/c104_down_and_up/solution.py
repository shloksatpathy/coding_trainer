def down_up(n):
    if n == 0:
        return
    print(n)
    down_up(n - 1)
    print(n)


n = int(input())
down_up(n)
