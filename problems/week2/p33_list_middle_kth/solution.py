class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

n, k = map(int, input().split())
head = None
for v in reversed(list(map(int, input().split()))):
    head = Node(v, head)
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
lead = trail = head
for _ in range(k):
    lead = lead.next
while lead:
    lead = lead.next
    trail = trail.next
print(slow.val, trail.val)
