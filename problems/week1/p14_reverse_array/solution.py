n = int(input())
a = list(map(int, input().split()))
i, j = 0, n - 1
while i < j:
    a[i], a[j] = a[j], a[i]
    i += 1
    j -= 1
print(*a)
