def firstDuplicateValue(array):
    dups = {}
    for i in array:
        if i in dups:
            return i
        else:
            dups[i] = True

    return -1
