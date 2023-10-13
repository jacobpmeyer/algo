def moveElementToEnd(array, toMove):
    left = 0
    right = len(array) - 1
    while left < right:
        while left < right and array[left] != toMove:
            left += 1

        while left < right and array[right] == toMove:
            right -= 1

        swap = array[left]
        array[left] = array[right]
        array[right] = swap

    return array

# Time: O(n)
# Space: O(1)
