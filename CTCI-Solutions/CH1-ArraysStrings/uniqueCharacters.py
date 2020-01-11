# Implement an algorithm to getermine if a string has all unique characters. What if you cannot use addotional data structures
# Loop through the characters, and add them to a hash dict if they dont exist in the dict. If they do and you come across them again, you reutn false
# Time complexity is O(n)

test = 'abcdef'
test2 = 'abcdeff'


def uniqueChars(char):
    characters = {}
    for s in char:
        if s in characters:
            return False
        else:
            characters[s] = True
    return True


print('Starting')

print(uniqueChars(test))
print(uniqueChars(test2))
