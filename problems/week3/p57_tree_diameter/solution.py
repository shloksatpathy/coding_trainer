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

import sys
sys.setrecursionlimit(10000)
best = 0

def height(n):
    global best
    if n is None:
        return 0
    hl, hr = height(n.left), height(n.right)
    best = max(best, hl + hr)
    return 1 + max(hl, hr)

height(build(input().split()))
print(best)
