a, b = map(int, input().split())
print(f"before: a={a} b={b}")
t = a
a = b
b = t
print(f"after: a={a} b={b}")
