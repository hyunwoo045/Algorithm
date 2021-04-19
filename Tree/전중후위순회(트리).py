class Node:
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right


def preorder(node): # root -> left -> right
    print(node.item, end='')
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])


def inorder(node):  # left -> root -> right
    if node.left != '.':
        inorder(tree[node.left])
    print(node.item, end='')
    if node.right != '.':
        inorder(tree[node.right])


def postorder(node):  # left -> right -> root
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    print(node.item, end='')


if __name__ == "__main__":
    n = int(input())
    tree = {}
    root = ''
    for i in range(n):
        parent, left, right = map(str, input().split())
        tree[parent] = Node(parent, left, right)
        if i == 0:
            root = parent
    preorder(tree[root])
    print()
    inorder(tree[root])
    print()
    postorder(tree[root])