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

def valid(n, lo, hi):
    if n is None:
        return True
    if not (lo < n.val < hi):
        return False
    return valid(n.left, lo, n.val) and valid(n.right, n.val, hi)

print("Valid" if valid(build(input().split()), float("-inf"), float("inf")) else "Invalid")
