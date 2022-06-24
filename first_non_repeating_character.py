def firstNonRepeatingCharacter(string):
  singleChars = {}

  for i, char in enumerate(string):
    if singleChars.get(char) is None:
      singleChars[char] = []
    singleChars[char].append(i)

  singleArr = []

  for array in singleChars.values():
    if len(array) == 1:
      singleArr.append(array[0])

  if len(singleArr) == 0:
    return -1

  return min(singleArr)

print(firstNonRepeatingCharacter("bllebaa"))
