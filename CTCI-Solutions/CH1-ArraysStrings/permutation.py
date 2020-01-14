# Given two strings write a method to deide if one is a permutation of the other

# Go through the first string
# Increment the key value pair in the has table for each occurence of a string
# Decrement the key value pair in the hash table for each alphabet in the second string
# end of loop, if length of char values are zero return true


def permutation(a, b):
    if len(a) != len(b):
        return False
    chars = {}
    for x in a:
        if x not in chars:
            chars[x] = 1
        else:
            chars[x] += 1
    for i in b:
        if i in chars:
            chars[i] -= 1
            if chars[i] == 0:
                del chars[i]
            elif chars[i] < 0:
                return False
        else:
            return False
    if len(chars.values()) == 0:
        return True


print('starting permutation test')
print(permutation('heloo', 'ooleh'))
