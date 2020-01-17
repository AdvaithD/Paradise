## Searching and Sorting

### Searching a sorted array

#### Binary Search
- Elimination based strategy for searching a sorted array.
- Idea is to eliminate half the keys from consideration (by keeping keys in sorted order)
- Easy to implement
  - Trickerier to implement considering the edge cases (this is what you'd ideally need to excel at)
- Iterative Binary search:

```
TODO: complete implementation
def binarysearch(t, A):
    L, U = 0, len(A) - 1
```
---
# Common Sorting Algorithms

1. **Bubble Sort [O(n^2) time O(1) space]:** Start at the beginning of the array and swap teh first two elements if **first > second**, and go onto the next pair. In doing so the smaller items bubble up to the beginning of the list.

2. **Selection Sort[O(n^2) time O(1) space]:** Select smallest element using linear scan and move it to the front element. Then find the second smallest and move it again. Continue doing this until all elements are in place.
   
3. **Merge Sort [O(nlogn) time ~ O(n) space]:** Divide array in half, sort each half and merge them back together.
   
4. **Quick Sort [O(nlogn) time ~ O(logn) space]:** Pick a random element and partition array (elements less thatn pivot, pivot, elements greater than pivot). IOf we repeatedly partition the array around an element the array will eventually become sorted. The runtime depends on how we choose the pivot.
   
5. **Radix Sort [O(kn) runtime]:** 

