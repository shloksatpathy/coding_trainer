n = int(input())
digits = 1
while n >= 10:
    n //= 10
    digits += 1
print(digits)
