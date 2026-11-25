n = int(input())
a = []
for w in input().split():
    a.append(int(w))
x = int(input())
count = 0
for v in a:
    if v == x:
        count += 1
print(f"count: {count}")
print("positions:", end="")
for i in range(n):
    if a[i] == x:
        print(f" {i + 1}", end="")
if count == 0:
    print(" none", end="")
print()
