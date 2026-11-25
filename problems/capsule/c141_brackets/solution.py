line = input()
stack = []
ok = True
for ch in line:
    if ch in "([{":
        stack.append(ch)
    elif ch in ")]}":
        if len(stack) == 0 or "([{".index(stack[-1]) != ")]}".index(ch):
            ok = False
            break
        stack.pop()
if ok and len(stack) == 0:
    print("yes")
else:
    print("no")
