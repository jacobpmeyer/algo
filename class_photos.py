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


# I didn't fully understand this problem. I was thinking of many rows,
# alternating between red and blue.
# The problem was actually asking to have two rows and that the back row
# at each index be taller than the front row at the same index.

# Below is clearly a better solve given the above comment, but my first itteration
# definitely works and would work for the problem I'd imagined too, whereas
# the solve below would not.
def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort(reverse = True)
    blueShirtHeights.sort(reverse = True)

    shortColorInFirstRow = "RED" if redShirtHeights[0] < blueShirtHeights[0] else "BLUE"

    for idx in range(len(redShirtHeights)):
        redShirtHeight = redShirtHeights[idx]
        blueShirtHeight = blueShirtHeights[idx]

        if shortColorInFirstRow == "RED":
            if redShirtHeight >= blueShirtHeight:
                return False
        else:
            if blueShirtHeight >= redShirtHeight:
                return False

    return True
