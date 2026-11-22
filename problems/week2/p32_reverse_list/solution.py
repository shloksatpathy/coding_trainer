import sys
sys.setrecursionlimit(10000)

class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

def reverse_iter(head):
    prev = None
    while head:
        head.next, prev, head = prev, head, head.next
    return prev

def reverse_rec(head):
    if head is None or head.next is None:
        return head
    new_head = reverse_rec(head.next)
    head.next.next = head
    head.next = None
    return new_head

n = int(input())
head = None
for v in reversed(list(map(int, input().split()))):
    head = Node(v, head)
head = reverse_iter(head)
print(*to_list(head))
head = reverse_rec(head)
print(*to_list(head))
