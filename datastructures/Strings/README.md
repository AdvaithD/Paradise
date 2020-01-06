- String can be viewed as a special kind of array
- We treat strings and arrays seperately because of certrin operations that are commonly appplied to strings
  - comparison, joining, splitting, searching for substrings, replacing one string by another, parsing etc
- Advanced string processing algos often use **Hash tables** and **dynamic programming**
- Strings are immutable
  - `s = s[1:] or s += '123'` imply creating a new array of chars and then assigning back to s
  - Concantenating a single character *n* times to a string in a for loop has *O(n^2)* complexity
- String libraries
  - key operators are `s[3], len(s), s+ t, s[2:4], s in t, s.strip(), s.startswith(), s.endswith(), s.join(), s.tolower()`

## Problems covered
1. Palindrome - a string that is the same when reversed