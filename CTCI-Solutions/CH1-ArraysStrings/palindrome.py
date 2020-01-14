def isPermutationOfAPalindrome(string):
    let count = {}
    for letter in string.replace(' ', ''):
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    for x in coun.values():
        oddcount += x % 2
        if oddcount > 1:
            return False
    return True


print('Checking the permutation of a palindrome')

isPermutationOfAPalindrome('Tact Coa')
