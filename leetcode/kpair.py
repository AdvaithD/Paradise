import collections


def findKPairs(nums, k):
    res = 0
    c = collections.Counter(nums)
    for i in c:
        if k > 0 and i + k in c or k == 0 and c[i] > 1:
            res += 1
    print(res)


test1 = [3, 1, 4, 1, 5]
print('Running test case one')
findKPairs(test1, 2)
# Input: [3, 1, 4, 1, 5], k = 2
# Output is 2
