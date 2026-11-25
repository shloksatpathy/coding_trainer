def max2(a, b):
    if a > b:
        return a
    return b


def max3(a, b, c):
    return max2(max2(a, b), c)


a, b, c = map(int, input().split())
print(max3(a, b, c))
