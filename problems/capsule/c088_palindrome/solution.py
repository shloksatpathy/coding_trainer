w = input()
i = 0
j = len(w) - 1
same = True
while i < j:
    if w[i] != w[j]:
        same = False
        break
    i += 1
    j -= 1
if same:
    print("yes")
else:
    print("no")
