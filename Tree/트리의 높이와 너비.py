import sys
input = sys.stdin.readline


class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def inorder(node):  # left -> root -> right
    global cur
    if node.left != -1:
        level[node.left] = level[node.data] + 1
        inorder(tree[node.left])
    cur += 1
    if level_min[level[node.data]] > cur:
        level_min[level[node.data]] = cur
    if level_max[level[node.data]] < cur:
        level_max[level[node.data]] = cur
    if node.right != -1:
        level[node.right] = level[node.data] + 1
        inorder(tree[node.right])


n = int(input())
tree = {}
parent = [-1 for _ in range(n+1)]
for _ in range(n):
    v, l, r = map(int, input().split())
    tree[v] = Node(v, l, r)
    if l != -1:
        parent[l] = v
    if r != -1:
        parent[r] = v

for i in range(1, n + 1):
    if parent[i] == -1:
        root = i
        break
level = [0 for _ in range(n+1)]
level_min = [n for _ in range(n+1)]
level_max = [0 for _ in range(n+1)]
level[root] = 1
cur = 0
inorder(tree[root])
print(level_min)
print(level_max)
'''
print(level)
print(level_min)
print(level_max)
'''
res = 0
res_idx = 0
for i in range(1, n+1):
    diff = level_max[i] - level_min[i] + 1
    if res < diff:
        res = diff
        res_idx = i
print(res_idx, res)