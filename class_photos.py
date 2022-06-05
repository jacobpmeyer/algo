# Sort the two lists
# Determine list has highest value
# alternate between lists
# After checking a row, chech that next tallest row is in OTHER list
#   If it is not, return false
# If the check successfully iterates through both lists, return true
# [5, 8, 1, 3, 4]
# [6, 9, 2, 4, 5]

# [2, 4, 5, 6, 9]
# [1, 3, 4, 5, 8]
#

def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()

    i = len(redShirtHeights) - 1
    j = len(redShirtHeights) - 1

    taller = redShirtHeights
    shorter = blueShirtHeights

    if taller[i] == shorter[i]:
        return False
    elif taller[i] < shorter[i]:
        taller = blueShirtHeights
        shorter = redShirtHeights

    while i >= 0 and j >= 0:
        if i >= j:
            if not rowChecker(taller[i], shorter[j]):
                return False
            i = checkAndMoveIndex(i, taller, 0)
        else:
            if not rowChecker(shorter[j], taller[i]):
                return False
            j = checkAndMoveIndex(j, shorter, 1)
    return True

def rowChecker(tallerRow, shorterRow):
    if tallerRow < shorterRow:
        return False
    else:
        return True

def checkAndMoveIndex(idx, array, stop):
    idx -= 1
    while array[idx] == array[idx + 1] and idx >= stop:
        idx -= 1
    return idx
