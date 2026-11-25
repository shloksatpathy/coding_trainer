n = int(input())
a = []
for w in input().split():
    a.append(int(w))
first = a[0]
for x in a:
    if x > first:
        first = x
found = False
second = 0
for x in a:
    if x < first and (not found or x > second):
        second = x
        found = True
if found:
    print(second)
else:
    print("none")
