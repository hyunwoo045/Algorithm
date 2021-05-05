import sys
sys.setrecursionlimit(10**6)

class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def preorder(cur, preList):
    preList.append(cur.data[2])
    if cur.left:
        preorder(cur.left, preList)
    if cur.right:
        preorder(cur.right, preList)

def postorder(cur, postList):
    if cur.left:
        postorder(cur.left, postList)
    if cur.right:
        postorder(cur.right, postList)
    postList.append(cur.data[2])

def solution(nodeinfo):
    preList, postList = [], []
    nodeinfo = [(nodeinfo[i][0], nodeinfo[i][1], i+1) for i in range(len(nodeinfo))]
    nodeinfo.sort(key=lambda x: (-x[1], x[0]))
    root = None
    for node in nodeinfo:
        if not root:
            root = Tree(node)
            continue
        parent = root
        while True:
            if node[0] < parent.data[0]:
                if not parent.left:
                    parent.left = Tree(node)
                    break
                parent = parent.left
            elif node[0] > parent.data[0]:
                if not parent.right:
                    parent.right = Tree(node)
                    break
                parent = parent.right
    preorder(root, preList)
    postorder(root, postList)
    return [preList, postList]