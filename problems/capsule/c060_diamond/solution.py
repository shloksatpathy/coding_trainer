n = int(input())
for k in range(1, 2 * n):
    if k <= n:
        i = k
    else:
        i = 2 * n - k
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()
