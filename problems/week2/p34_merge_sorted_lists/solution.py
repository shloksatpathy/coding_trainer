class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

def read_list():
    input()
    head = None
    for v in reversed(list(map(int, input().split()))):
        head = Node(v, head)
    return head

a, b = read_list(), read_list()
dummy = tail = Node(0)
while a and b:
    if a.val <= b.val:
        tail.next, a = a, a.next
    else:
        tail.next, b = b, b.next
    tail = tail.next
tail.next = a or b
out, cur = [], dummy.next
while cur:
    out.append(cur.val)
    cur = cur.next
print(*out)
