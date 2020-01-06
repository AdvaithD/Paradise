## Stacks

- Last-in, first-out semantics for inserts and deletes
- Two operations
  - `push()` - Add an item to the top of the stack
  - `pop()` - Remove item from the top of the stack

### Sample use case: print linked list in reverse (arg: head of the LL)

```
def print_linked_list_in_reverse(head):
    let stack = []
    while head:
        stack.append(head.data)
        head = head.next
    while stack:
        print(stack.pop())
```

1. Create an array
2. While head is not null, keep pushing (`.append()`) and iterating
3. After stack is complete
   1. Keep popping until its empty and print

We need to learn to notice when **LIFO** is applicable

### Stack libarry

- Some problems require a custom stack class, if not just use the `list` type
- `s.append()`: push element to stack
- `s.pop()`: Remove and return element at top of stack
- `s[-1]`: Retrieves but doesn't remove from top of stack
- `len(s) == 0` test if stack is empty

## Queues

- First-in, first-out order
- Two operations: enqueue and dequeue
- Queues are ideal **when order needs to be preserved** (what does this mean?)

### Queue library

- Some problems require own class, otherwise use the `collections.deque` class
- `q.append()`: pushes element onto the queue,
- `q[0]`: Retrieve the element at the front of the queue. `q[-1]` returns the last element
- `q.popleft()`: Remove and return first element of the queue (its faster than `.pop(0)` - [proof](https://stackoverflow.com/questions/32543608/deque-popleft-and-list-pop0-is-there-performance-difference))

### Sample problem

```
Given a binary tree, return an array consisting of the keys at the same level. Keys should appear in the order of the corresponding nodes’ depths, breaking ties from left to right.
```
