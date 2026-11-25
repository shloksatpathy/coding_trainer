n = int(input())
k = 1
for i in range(1, n + 1):
    for j in range(i):
        if j > 0:
            print(" ", end="")
        print(k, end="")
        k += 1
    print()
