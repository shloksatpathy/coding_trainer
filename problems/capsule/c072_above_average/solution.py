n = int(input())
a = []
for w in input().split():
    a.append(int(w))
total = 0
for x in a:
    total += x
print(f"average: {total / n:.2f}")
found = 0
for x in a:
    if x * n > total:
        if found > 0:
            print(" ", end="")
        print(x, end="")
        found += 1
if found == 0:
    print("none")
else:
    print()
