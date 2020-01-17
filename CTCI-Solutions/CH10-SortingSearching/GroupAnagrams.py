import unittest


def groupAnagrams(parameter_list):
    pairs = [(s, sorted(s)) for s in parameter_list]
    pairs.sort(key=lambda x: x[1])
    final = [x[0] for x in pairs]
    return final


class Test(unittest.TestCase):
    def test_group_anagrams(self):
        strings = ["cat", "bat", "rat", "arts", "tab", "tar", "car", "star"]
        self.assertEqual(groupAnagrams(strings), [
            "bat", "tab", "car", "cat", "arts", "star", "rat", "tar"])


if __name__ == "__main__":
    unittest.main()


# How did we solve this?
# We took each string in the array, used `sorted()` to pair it thru tuples to their anagrams
# then we sort the list of tuples by the sorted string.
