class ListNode():
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


# Idk about this, doesnt seem elegant
unsorted = ListNode(3)
unsorted.next = ListNode(4)
unsorted.next.next = ListNode(5)
unsorted.next.next.next = ListNode(6)
unsorted.next.next.next.next = ListNode(7)
unsorted.next.next.next.next.next = ListNode(2)
unsorted.next.next.next.next.next.next = ListNode(1)
unsorted.next.next.next.next.next.next.next = None


def partitionOne(list, pivot):
    beforeStart = null
    beforeEnd = null
    afterStart = null
    afterEnd = null

    while list:
        node = list
        node.next = null
        if node.data < pivot:
            if beforeStart:
                beforeStart.next = node
            else:
                beforeStart = node
                beforeEnd = node
        else:
            if afterStart:
                afterStart.next = node
            else:
                afterStart = node
                afterEnd = node
        node = list.next


def partitionTwo(list, pivot):
    head = None
    tail = None

    while list:
        node = list
        node.next = None
        if node.data > pivot:
            if tail:
                tail.next = node
            else:
                tail = node
        elif node.data < pivot:
            if head:
                head.next = node
            else:
                head = node
        list = list.next
        # After loop
    head.next = tail
    return head


res = partitionTwo(unsorted, 5)

print(res.data, res.next.data, res.next.next.data,
      res.next.next.next.data, res.next.next.next.next.data)
