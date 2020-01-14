# Implement a method to perform basic string compression usint the counts of repeated characters.
# If the compressed string would not be smaller than original string, return the original string
import collections


def compression(string):
    counts = collections.Counter(string)
    # print(counts.values())
    res = ''
    for i in counts.keys():
        res += (i + str(counts[i]))
    print(min(res, string))


compression('aabbbccc')

# expected output: a2b3c3
