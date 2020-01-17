# Check if a linked list is a palindrome
from ListNode import ListNode
unsorted = ListNode(1)
unsorted.next = ListNode(2)
unsorted.next.next = ListNode(2)
unsorted.next.next.next = ListNode(2)
unsorted.next.next.next.next = ListNode(2)
unsorted.next.next.next.next.next = ListNode(1)
unsorted.next.next.next.next.next.next = None


def palindrome(head):
    seen = {}
    while head:
        if head.data in seen:
            seen[head.data] += 1
            head = head.next
        else:
            seen[head.data] = 1
            head = head.next
    for number, count in seen.items():
        mod = count % 2
        if mod != 0:
            return False
    return True


# isPalindrome = palindrome(unsorted)
# print(isPalindrome)


# LOGIC: Create two runners (1x and 2x). Keep adding the slow runner's data to a stack
# until you reach the end of the list.
# Iterate the slow runner from midpoint to end and keep comparing with stack.pop()
# return true if the loop goes through, else return false
def palindromeTwo(head):
    fast, slow = head
    stack = []
    while fast and fast.next:
        stack.push(fast.data)
        fast = fast.next.next
        slow = slow.next
