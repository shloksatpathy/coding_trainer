n = int(input())
first = True
for i in range(1, n + 1):
    if i % 3 == 0:
        continue
    if not first:
        print(" ", end="")
    print(i, end="")
    first = False
print()
