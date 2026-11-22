n = int(input())
a = list(map(int, input().split()))

def sift_down(i, size):
    while True:
        c = 2 * i + 1
        if c >= size:
            return
        if c + 1 < size and a[c + 1] > a[c]:
            c += 1
        if a[c] <= a[i]:
            return
        a[i], a[c] = a[c], a[i]
        i = c

for i in range(n // 2 - 1, -1, -1):
    sift_down(i, n)
print(*a)
for end in range(n - 1, 0, -1):
    a[0], a[end] = a[end], a[0]
    sift_down(0, end)
print(*a)
