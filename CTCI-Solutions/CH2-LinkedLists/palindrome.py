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


isPalindrome = palindrome(unsorted)
print(isPalindrome)
