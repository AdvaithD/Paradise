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


print(urlfy("hello my name is advaith and i fucking suck"))
