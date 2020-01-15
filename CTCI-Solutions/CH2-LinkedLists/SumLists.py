class ListNode():
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


def sumlists(list1, list2):
    sum = new Node()
    node1, node2 = Node(), Node()
    carry = 0
