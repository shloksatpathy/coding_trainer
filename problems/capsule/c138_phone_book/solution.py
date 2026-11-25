n = int(input())
book = {}
for i in range(n):
    name, number = input().split()
    book[name] = number
q = int(input())
for i in range(q):
    name = input()
    print(f"{name}: {book.get(name, 'not found')}")
