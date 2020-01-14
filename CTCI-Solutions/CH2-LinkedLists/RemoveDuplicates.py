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
# unsorted.next.next.next.next.next.next = None


# print(unsorted)
# Write code to remove duplicates from an unsorted linked list


# def removeDuplicates(list):
#     seen = set()
#     runner = list
#     while runner:
#         if runner in seen:
#             runner.next = runner.next.next
#             return
#         else:
#             seen.add(runner.data)
#             runner = runner.next
#     print(seen)

def duplicates(ll):
    runner = ll
    seen = set()
    seen.add(runner.data)
    while runner.next:
        if runner.next.data in seen:
            runner.next = runner.next.next
        else:
            seen.add(runner.next.data)
            runner = runner.next
    print(seen)
    return ll


res = duplicates(unsorted)

print(res.data, res.next.data, res.next.next.data,
      res.next.next.next.data, res.next.next.next.next.data)
