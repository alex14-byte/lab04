
def lib(data):
    res = set()
    for i in data:
        for j in data:
            if i is not j:
                res |= set(i) & set(j)
    return res

