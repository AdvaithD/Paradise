class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# Pre-Order
def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

# Post-Order


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)

# In-Order


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


# Test Tree
#      1
#     / \
#    2   3
#   /     \
#  4       5

test = Node(1)
test.left = Node(2)
test.right = Node(3)
test.left.left = Node(4)
test.left.right = Node(5)

print("preorder")
preorder(test)

print("\n postorder")
postorder(test)

print("\n inorder")
inorder(test)
