def firstDuplicateValue(array):
  seenNums = {}
  i = 0
  while i < len(array):
    if seenNums.get(array[i]) is True:
      return array[i]
    else:
      seenNums[array[i]] = True
    i += 1

  return -1

# Time: O(n)
# Space: O(n)

a = [2, 1, 5, 2, 3, 3, 4]

b = [2, 1, 5, 3, 3, 2, 4]
