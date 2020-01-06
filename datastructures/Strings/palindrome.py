def palindrome(s):
    return all(s[i]=s[-i] for i in range(len(s) // 2))

# Notice how it handles both odd and even number of elements in string
# the double slash is for floor division (ex: 8 // 3 = 2)
