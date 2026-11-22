class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

head = tail = None
for _ in range(int(input())):
    cmd = input().split()
    if cmd[0] == "push_front":
        node = Node(int(cmd[1]))
        node.next = head
        head = node
        if tail is None:
            tail = node
    elif cmd[0] == "push_back":
        node = Node(int(cmd[1]))
        if tail is None:
            head = tail = node
        else:
            tail.next = node
            tail = node
    elif cmd[0] == "pop_front":
        if head is None:
            print("Empty")
        else:
            print(head.val)
            head = head.next
            if head is None:
                tail = None
    elif cmd[0] == "pop_back":
        if head is None:
            print("Empty")
        elif head is tail:
            print(head.val)
            head = tail = None
        else:
            cur = head
            while cur.next is not tail:
                cur = cur.next
            print(tail.val)
            cur.next = None
            tail = cur
    else:
        vals, cur = [], head
        while cur:
            vals.append(cur.val)
            cur = cur.next
        print(*vals if vals else ["Empty"])
