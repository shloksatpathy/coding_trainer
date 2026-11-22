n = int(input())
fib = [0, 1]
while len(fib) < n:
    fib.append(fib[-1] + fib[-2])
print(*fib[:n])
a, b, k = 0, 1, 1
while a + b < 2 ** 64:
    a, b, k = b, a + b, k + 1
print(k)
