class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

def build(s):
    head = None
    for ch in s:
        head = Node(ord(ch) - 48, head)
    return head

a, b = input().split()
x, y = build(a), build(b)
dummy = tail = Node(0)
carry = 0
while x or y or carry:
    total = carry + (x.val if x else 0) + (y.val if y else 0)
    tail.next = Node(total % 10)
    tail = tail.next
    carry = total // 10
    x = x.next if x else None
    y = y.next if y else None
digits, cur = [], dummy.next
while cur:
    digits.append(str(cur.val))
    cur = cur.next
print("".join(reversed(digits)))
