class ListNode():
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

# Searching a list for a key
# O(n) complexity


def search_list(L, key):
    while L and L.data != key:
        L = L.next
    return L

# Insert a new node after a specified node
# Make the new node point to old node's next
# Point old node to new node, thereby inserting it in between ez game ez life
# O(1) complexity


def insert_after(node, new_node):
    new_node.next = node.next
    node.next = new_node

# Delete the node after this, assume its not a tail
# Basically using .next to point to the node that comes after the deleted node
# O(1) complexity


def delete_after(node):
    node.next = node.next.next
