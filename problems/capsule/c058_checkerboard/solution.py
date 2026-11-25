n = int(input())
for r in range(n):
    for col in range(n):
        if (r + col) % 2 == 0:
            print("#", end="")
        else:
            print(".", end="")
    print()
