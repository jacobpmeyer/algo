def generateDocument(characters, document):
  charsDict = {}

  for char in characters:
    if not charsDict.get(char):
      charsDict[char] = 0

    charsDict[char] += 1

  for char in document:
    if not charsDict.get(char):
      return False
    if charsDict[char] == 0:
      return False
    else:
      charsDict[char] -= 1

  return True

  """
  Time = O(n + k)
  Space = O(c) where c is the number of unique characters
  """
