import lib


def test():
    data = [[1, 2, 3], [3, 4, 5], [5, 6, 7], [7, 8, 9], [1, 2, 3]]
    res = lib.lib(data)
    check = False
    expected = {1, 2, 3, 5, 7}
    if expected == res:
        check = True
    return check
