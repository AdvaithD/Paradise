# Given a node somewhere in the middle (not exactly) of a linked list
# Please find a way to delete the node
# Why is this imp: this is important because head is not given access


def deleteNode(node):
    # Take data from the next node
    nextNode = node.next.data
    # Change current nodes data to the next node's data
    node.data = nextNode
    # Skip the next node
    node.next = node.next.next


# Essentially, copy the next node's data to the node you want to delete
# Then change current node's 'next' pointer to skip 1 node
# Step 1: a -> b -> c -> d -> e -> f(we are given c)
# Step 2: a -> b -> d -> d -> e -> f(copy d to c's node)
# Step 3: a -> b -> d -> e -> f(change d(previously c) to point to e and not d)
# Step 4: wow u did this without access to the head element 👏
