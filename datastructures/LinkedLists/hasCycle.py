def hasCycle(head):
    # Initiate fast and slow to head
    fast = slow = head
    # While fast and the 2 nodes ahead of it exist
    while fast and fast.next and fast.next.next:
        # iterate slow by 1, fast by two
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            slow = head
            while slow is not fast:
                slow, fast = slow.next, fast.next
            return slow
    return null


# UNNECESSARY CODE
#  if (head.data is None):
#         print('List is empty')
#         return false
#     else:
