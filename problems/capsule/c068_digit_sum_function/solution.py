def digit_sum(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


n = int(input())
numbers = input().split()
best = -1
best_sum = -1
for i in range(n):
    x = int(numbers[i])
    if i > 0:
        print(" ", end="")
    print(digit_sum(x), end="")
    if digit_sum(x) > best_sum:
        best_sum = digit_sum(x)
        best = x
print()
print(f"best: {best}")
