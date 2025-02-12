## Linked Lists

- Ordered collection of values. Sequenceof nodes such that each node contains an object and a reference to the next node in the list.
- First node is *head* and last node is *tail* (tail's next field is null)


- Two types of list-related problems
  - Implement your own list
  - Exploit the standard list library

- Basic API - search, insert delete for singly linked list
- List problems are usually simple bruteforce solutions that use O(n) space
  - usually have a subtler solution that uses existing list nodes to reduce space complexity to O(1)

- Problems w/ lists are more about **cleanly coding** what is required.
  - Consider using a dummy head
  - Don't forget update next 
  - Try to use two iterators for singly linked lists (one ahead of other / one advancing quicker than the other)


### Problem #1
Write a program that takes the head of a singly linked list and returns null if there does not exist a cycle,and the node at the start of the cycle, if a cycle is present. (You do not know the length of the list in advance.)
**Essentially:** Does a linkedlist loop back?

How do we solve this??
1. Simplest way (if space is not an issue)
   1. Explore nodes via next field starting from head and store visited nodes in a **hash table (this comes in clutch hella study this a lot)**
   2. Cycle exists if we visit a node that already exists in the **hash table**
   3. No cycle implies the search ends at the tail.
   4. O(n) space and

2. What if we dont want to use *additional storage* (no hash map) and that does not modify list
   1. Traverse list in two loops. (slow iterator and fast iterator design pattern)
   2. 