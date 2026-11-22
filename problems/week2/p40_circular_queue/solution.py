k, q = map(int, input().split())
buf, head, count = [0] * k, 0, 0
for _ in range(q):
    cmd = input().split()
    if cmd[0] == "enq":
        if count == k:
            print("Full")
        else:
            buf[(head + count) % k] = int(cmd[1])
            count += 1
    elif cmd[0] == "deq":
        if count == 0:
            print("Empty")
        else:
            print(buf[head])
            head = (head + 1) % k
            count -= 1
    elif cmd[0] == "front":
        print(buf[head] if count else "Empty")
    else:
        print(count)
