def url(arg):
    array = arg.split()
    res = ""
    print(array)
    for i in array:
        res += '%20' + i
    print(res)


def urlfy(string):
    return string.strip().replace(' ', '%20')
# url("hello my name is advaith and i fucking suck")
# .strip() removes leading and trailing spaces of a string
# We then replace spaces with %20
# .replace() has O(n) time complexity


print(urlfy("hello my name is advaith and i am bad at coding"))
