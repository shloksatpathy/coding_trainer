tokens = input().split()
total = 0
term = int(tokens[0])
for i in range(1, len(tokens), 2):
    op = tokens[i]
    x = int(tokens[i + 1])
    if op == "*":
        term *= x
    else:
        total += term
        if op == "+":
            term = x
        else:
            term = -x
print(total + term)
