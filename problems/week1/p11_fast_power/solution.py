x, n, m = map(int, input().split())
result, base = 1 % m, x % m
while n > 0:
    if n & 1:
        result = result * base % m
    base = base * base % m
    n >>= 1
print(result)
