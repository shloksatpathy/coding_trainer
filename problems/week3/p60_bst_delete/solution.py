class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def insert(n, v):
    if n is None:
        return Node(v)
    if v < n.val:
        n.left = insert(n.left, v)
    elif v > n.val:
        n.right = insert(n.right, v)
    return n

def delete(n, key):
    if n is None:
        return None
    if key < n.val:
        n.left = delete(n.left, key)
    elif key > n.val:
        n.right = delete(n.right, key)
    elif n.left is None:
        return n.right
    elif n.right is None:
        return n.left
    else:
        s = n.right
        while s.left:
            s = s.left
        n.val = s.val
        n.right = delete(n.right, s.val)
    return n

def pre(n, out):
    if n:
        out.append(n.val)
        pre(n.left, out)
        pre(n.right, out)
    return out

input()
root = None
for v in map(int, input().split()):
    root = insert(root, v)
input()
for k in map(int, input().split()):
    root = delete(root, k)
out = pre(root, [])
print(*out if out else ["Empty"])
