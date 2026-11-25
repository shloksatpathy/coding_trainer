n = int(input())
words = []
for i in range(n):
    cmd = input().split()
    if cmd[0] == "add":
        words.append(cmd[1])
    elif cmd[0] == "undo":
        if len(words) > 0:
            words.pop()
    elif len(words) == 0:
        print("(empty)")
    else:
        print(" ".join(words))
