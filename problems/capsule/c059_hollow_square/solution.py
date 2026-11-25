n = int(input())
for r in range(n):
    for col in range(n):
        if r == 0 or r == n - 1 or col == 0 or col == n - 1:
            print("#", end="")
        else:
            print(" ", end="")
    print()
