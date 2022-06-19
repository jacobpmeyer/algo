"""
array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33

should return 3, then index of 33 in this array.

look at middle element.
if middle element == target, return index of middle element.
if middle element > target, run b search on left half of array.
if middle element < target, run b search on right half of array.

mid = (len(array) - 1) // 2
we take one off the end for indexing and we floor the array

return -1 if not found.
"""

def binarySearch(array, target):
  return binarySearchRecurs(array, target)

def binarySearchRecurs(array, target):
  if not array:
    return - 1
  if len(array) == 1 and array[0] != target:
    return -1

  midIdx = (len(array) - 1) // 2
  midEle = array[midIdx]

  if midEle == target:
    return midIdx
  elif target > midEle:
    nextCall = binarySearchRecurs(array[midIdx+1:], target)
    return midIdx + 1 + nextCall if nextCall >= 0 else nextCall
  else:
    return binarySearchRecurs(array[:midIdx], target)




