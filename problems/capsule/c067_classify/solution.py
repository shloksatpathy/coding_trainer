def classify(n):
    if n < 0:
        return "negative"
    if n == 0:
        return "zero"
    if n < 10:
        return "small"
    if n < 100:
        return "medium"
    return "large"


n = int(input())
for w in input().split():
    print(classify(int(w)))
