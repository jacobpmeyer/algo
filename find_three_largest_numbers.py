"""
array = [141, 1, 17, 7, -17, -27, 18, 541, 8, 7, 7]
should return [18, 141, 541]

don't sort input array
return array is 3 greatest values, sorted
"""

def findThreeLargestNumbers(array):
  greatest = [float("inf") for i in range(3)]

  for num in array:
    greatest = greatestHelper(num, greatest)

  return greatest

def greatestHelper(potentialGreatest, array):
  for idx in reversed(range(3)):
    if potentialGreatest > array[idx]:
      array = array[:idx+1] + [potentialGreatest] + array[idx+1:]
      return array[1:]

  return array
