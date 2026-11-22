back, fwd = [], []
cur = "home"
while True:
    cmd = input().split()
    if cmd[0] == "Q":
        break
    if cmd[0] == "visit":
        back.append(cur)
        cur = cmd[1]
        fwd.clear()
    elif cmd[0] == "back" and back:
        fwd.append(cur)
        cur = back.pop()
    elif cmd[0] == "forward" and fwd:
        back.append(cur)
        cur = fwd.pop()
    print(cur)
