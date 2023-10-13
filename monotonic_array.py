def isMonotonic(array):
    if len(array) <= 1:
        return True

    startIdx = 0
    while startIdx + 1 < len(array) and array[startIdx] == array[startIdx + 1]:
        startIdx += 1

    if startIdx == len(array) - 1:
        return True

    direction = ""

    if array[startIdx] > array[startIdx + 1]:
        direction = "down"
    else:
        direction = "up"

    for i in range(startIdx, len(array) - 1):
        if array[i] < array[i + 1] and direction == "down":
            return False
        if array[i] > array[i + 1] and direction == "up":
            return False

    return True
