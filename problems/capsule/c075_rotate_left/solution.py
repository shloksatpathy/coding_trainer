n = int(input())
a = []
for w in input().split():
    a.append(int(w))
k = int(input())
for i in range(n):
    if i > 0:
        print(" ", end="")
    print(a[(i + k) % n], end="")
print()
