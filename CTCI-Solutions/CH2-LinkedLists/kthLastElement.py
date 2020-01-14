class ListNode():
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


unsorted = ListNode(5)
unsorted.next = ListNode(4)
unsorted.next.next = ListNode(5)
unsorted.next.next.next = ListNode(2)
unsorted.next.next.next.next = ListNode(3)
unsorted.next.next.next.next.next = ListNode(6)
unsorted.next.next.next.next.next.next = None


# Horrible solution cause its so trivial, we already know this isn't good enough
def kLastNodeBadSolution(head, k):
    # compute size
    size = 0
    runner = head
    while runner.next:
        size += 1
        runner = runner.next
    # need to find (size - k)th element
    counter = 0
    while counter != (size - k):
        counter += 1
        head = head.next
    print(head.data)


# kLastNodeBadSolution(unsorted, 3)

def kLastOptimal(head, k):
    r1 = head
    r2 = head
    for i in range(k+1):
        r2 = r2.next

    while r2:
        r1 = r1.next
        r2 = r2.next
    print(r1.data)


kLastOptimal(unsorted, 2)
