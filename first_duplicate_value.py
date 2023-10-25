# O(n) Time | O(n) Space
def firstDuplicateValue(array):
    dups = {}
    for i in array:
        if i in dups:
            return i
        else:
            dups[i] = True

    return -1

# O(n) Time | O(1) Space
def firstDuplicateValue(array):
    for num in array:
        absVal = abs(num)
        if array[absVal - 1] < 0:
            return absVal
        array[absVal - 1] *= -1
    return -1
