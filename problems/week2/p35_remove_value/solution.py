class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

n, x = map(int, input().split())
head = None
for v in reversed(list(map(int, input().split()))):
    head = Node(v, head)
dummy = Node(0, head)
cur = dummy
while cur.next:
    if cur.next.val == x:
        cur.next = cur.next.next
    else:
        cur = cur.next
out, cur = [], dummy.next
while cur:
    out.append(cur.val)
    cur = cur.next
print(*out if out else ["Empty"])
