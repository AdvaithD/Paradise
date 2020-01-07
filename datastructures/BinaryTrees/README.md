# Binary Trees

- For any node there exists a unique sequence of nodes from the root to the node(search path)
- A node is an ancestor of `d` if it lies on the `search path` from root to node.
- If a node is an `acestor` of d, d is a `descendant` of that node.
- Node with no descendants is called a `leaf`
- **Depth of a node** - Number of nodes on the search path from `root` to `n` (excluding n)
  - Depth starts from 0
- **Height of a binary tree** - Maximum depth of any node in that tree
- **Level of a tree** - All nodes at the same depth


![](https://i.gyazo.com/5c237a99fd775454714736130384c44f.png)


### Traversing
- Key computation on a binary tree is traversing all the `nodes`


### Tips
- **Recursive algos** are well suited for tree related problems.
- 