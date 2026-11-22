n, k = map(int, input().split())
a = list(map(int, input().split()))

def reverse(i, j):
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

k %= n
reverse(0, n - 1)
reverse(0, k - 1)
reverse(k, n - 1)
print(*a)
