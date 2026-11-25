def absolute(x):
    if x < 0:
        return -x
    return x


def distance(a, b):
    return absolute(a - b)


n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(distance(a, b))
