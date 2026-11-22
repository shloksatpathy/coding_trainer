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

root = build(input().split())
levels, q = [], [root]
while q:
    levels.append([n.val for n in q])
    q = [c for n in q for c in (n.left, n.right) if c]
print(f"height={len(levels)}")
for lv in levels:
    print(*lv)
