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
- q.append
- q[0]
- q.popleft()