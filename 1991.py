class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


N = int(input())
nodes = [0] * 26
for _ in range(N):
    val, left, right = input().split()
    nodes[ord(val) - 65] = Node(val, left, right)


def preorder(node):
    print(node.val, end="")
    if node.left != ".":
        preorder(nodes[ord(node.left) - 65])
    if node.right != ".":
        preorder(nodes[ord(node.right) - 65])


def inorder(node):
    if node.left != ".":
        inorder(nodes[ord(node.left) - 65])
    print(node.val, end="")
    if node.right != ".":
        inorder(nodes[ord(node.right) - 65])


def postorder(node):
    if node.left != ".":
        postorder(nodes[ord(node.left) - 65])
    if node.right != ".":
        postorder(nodes[ord(node.right) - 65])
    print(node.val, end="")


preorder(nodes[0])
print()
inorder(nodes[0])
print()
postorder(nodes[0])
