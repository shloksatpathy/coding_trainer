def fact_iter(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

def fact_rec(n):
    return 1 if n <= 1 else n * fact_rec(n - 1)

n = int(input())
print(fact_iter(n), fact_rec(n))
