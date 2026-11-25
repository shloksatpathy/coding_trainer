n = int(input())
for r in range(1, n + 1):
    for col in range(1, n + 1):
        print(f"{r * col:4d}", end="")
    print()
