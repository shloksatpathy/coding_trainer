def power(base, exp):
    result = 1
    for i in range(exp):
        result *= base
    return result


base, exp = map(int, input().split())
print(power(base, exp))
