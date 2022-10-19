
def lib():
    data = [[1, 2, 3], [3, 4, 5], [5, 6, 7], [7, 8, 9], [1, 2, 3]]

    res = set()

    for i in data:
        for j in data:
            if i is not j:
                res |= set(i) & set(j)

    print (res)

