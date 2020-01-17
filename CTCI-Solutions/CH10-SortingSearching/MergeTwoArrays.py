# Given two sorted arrays, A and B.
# A has large enough buffer at the end to hold B [len(b)]
# Write a method to merge B into A in sorted array.

# a and b are the two arrays


import unittest


def mergeArrays(A, B):
    index = len(A) - 1
    indexA = len(A) - len(B) - 1
    indexB = len(B) - 1

    while indexB >= 0:
        if indexA > 0 and A[indexA] > B[indexB]:
            A[index] = A[indexA]
            index -= 1
            indexA -= 1
        else:
            A[index] = B[indexB]
            index -= 1
            indexB -= 1
    return A


a1 = [33, 44, 55, 66, 88, 99, None, None, None]
b1 = [11, 22, 77]

# res = mergeArrays(a1, b1)

# print(res)


class Test(unittest.TestCase):
    def testSortedMerge(self):
        a = [33, 44, 55, 66, 88, 99, None, None, None]
        b = [11, 22, 77]
        res = mergeArrays(a, b)
        self.assertEqual(res, [11, 22, 33, 44, 55, 66, 77, 88, 99])


if __name__ == "__main__":
    unittest.main()
