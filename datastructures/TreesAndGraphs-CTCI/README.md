## Trees

- **Tree:** Data structure composed of nodes
  - Each tree has a root node (not a requirement in graph theory)
  - Root node has child nodes, and each child node has zero or more child nodes.

## Trees vs Binary Trees vs Binary Search Trees

- **Tree:** Each node can have **any** number of children
- **Binary Tree:** Each node can have **upto two** children
- **Binary Search Tree:** all left descrndents <= n < all right descendents
  - This must be true for all nodes _n_
  - NOTE: It must hold true for all of a _nodes descendents_
- **Balanced vs. Unbalanced:**
- **Complete Binary Trees:** Every level of the tree is fully filled, except for the last level.
- **Full Binary Trees:** Every node has zero or two children.
  - No nodes have only one child.
- **Perfect Binary Trees:**
  - A binary tree that is both full and complete.
  - All leaf nodes will be at the same level (and has the max # of **nodes**)

### Tree Traversals

1. **In-Order:** Left subtree, root note and then right subtree
2. **Pre-Order:** Root, left subtree and then right subtree
3. **Post-Order:** Left subtree, right subtree and then root

# Binary Heaps

- Complete binary tree (totally filled except the rightmost elements on the last level) where each node is smaller than its children.
- **Each node is smaller than the children**
- Two key operations: `insert` and `extract_min`
  - **Insert:** Start by inserting at the bottom rightmost spot (maintains complete tree property)
  - Fix the tree swapping new element w/ prent until we find appropriate spot.
  - _Takes O(log n) times. n is the number of nodes in the heap_
  - **Extracty minimum element:** Minimum element is always at the top. Extracting it is difficult.

# Tries (Prefix Trees)

# Graphs

## DFS and BFS

- **DFS:** Start at the root and explore each branch completely before moving onyo next branch.
  - DFS is preferred if you ant to visit every node in the graph.
- **BFS:** Start at the root and explore each neighbor before going on to any of their children.
  - BFS is preferred to find the shortest path b/w two nodes
