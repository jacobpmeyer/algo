def moveElementToEnd(array, toMove):
  lastNonMoveEle = len(array) - 1
  pointer = 0

  while lastNonMoveEle == toMove:
    lastNonMoveEle -= 1

  while pointer < lastNonMoveEle:
    while array[lastNonMoveEle] == toMove and pointer < lastNonMoveEle:
      lastNonMoveEle -= 1
    if array[pointer] == toMove:
      array[pointer], array[lastNonMoveEle] = array[lastNonMoveEle], array[pointer]

    pointer += 1

  return array

# Time: O(n)
# Space: O(1)
