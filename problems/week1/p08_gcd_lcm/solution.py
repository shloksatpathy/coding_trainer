def gcd_iter(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_rec(a, b):
    return a if b == 0 else gcd_rec(b, a % b)

a, b = map(int, input().split())
g = gcd_iter(a, b)
assert g == gcd_rec(a, b)
print(g, a // g * b)
