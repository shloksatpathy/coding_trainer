n = int(input())
queue = []
head = 0
for i in range(n):
    cmd = input().split()
    if cmd[0] == "join":
        queue.append(cmd[1])
    elif head < len(queue):
        print(f"served {queue[head]}")
        head += 1
    else:
        print("nobody waiting")
if head == len(queue):
    print("waiting: none")
else:
    print("waiting: " + " ".join(queue[head:]))
