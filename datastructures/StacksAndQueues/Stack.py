def print_linked_list_in_reverse(head):
    let stack = []
    while head:
        stack.append(head.data)
        head = head.next
    while stack:
        print(stack.pop())
