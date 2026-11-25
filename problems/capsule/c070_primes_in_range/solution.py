def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


a, b = map(int, input().split())
found = 0
for x in range(a, b + 1):
    if is_prime(x):
        if found > 0:
            print(" ", end="")
        print(x, end="")
        found += 1
if found == 0:
    print("none")
else:
    print()
