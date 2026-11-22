from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def build(tokens):
    if not tokens or tokens[0] == "N":
        return None
    root = Node(int(tokens[0]))
    q, i = deque([root]), 1
    while q and i < len(tokens):
        node = q.popleft()
        if tokens[i] != "N":
            node.left = Node(int(tokens[i]))
            q.append(node.left)
        i += 1
        if i < len(tokens) and tokens[i] != "N":
            node.right = Node(int(tokens[i]))
            q.append(node.right)
        i += 1
    return root

def pre(n, out):
    if n:
        out.append(n.val)
        pre(n.left, out)
        pre(n.right, out)
    return out

def ino(n, out):
    if n:
        ino(n.left, out)
        out.append(n.val)
        ino(n.right, out)
    return out

def post(n, out):
    if n:
        post(n.left, out)
        post(n.right, out)
        out.append(n.val)
    return out

root = build(input().split())
print(*pre(root, []))
print(*ino(root, []))
print(*post(root, []))
