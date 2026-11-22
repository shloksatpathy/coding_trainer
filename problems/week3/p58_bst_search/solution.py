class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def insert(root, v):
    if root is None:
        return Node(v)
    cur = root
    while True:
        if v == cur.val:
            return root
        side = "left" if v < cur.val else "right"
        nxt = getattr(cur, side)
        if nxt is None:
            setattr(cur, side, Node(v))
            return root
        cur = nxt

def inorder(n, out):
    if n:
        inorder(n.left, out)
        out.append(n.val)
        inorder(n.right, out)
    return out

input()
root = None
for v in map(int, input().split()):
    root = insert(root, v)
input()
queries = list(map(int, input().split()))
print(*inorder(root, []))
for x in queries:
    cur = root
    while cur and cur.val != x:
        cur = cur.left if x < cur.val else cur.right
    print("Found" if cur else "Not found")
