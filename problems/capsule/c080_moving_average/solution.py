n, k = map(int, input().split())
a = []
for w in input().split():
    a.append(int(w))
window = 0
for i in range(k):
    window += a[i]
print(f"{window / k:.2f}", end="")
for i in range(k, n):
    window += a[i] - a[i - k]
    print(f" {window / k:.2f}", end="")
print()
