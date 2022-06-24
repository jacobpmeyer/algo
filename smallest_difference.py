"""
Smallest Difference

Write a function that takes in two non-empty arrays of integers, finds the
pair of numbers (one from each array) whose absolute difference is closest to
zero, and returns an array containing these two numbers, with the number from
the first array in the first position.

Note that the absolute difference of two integers is the distance between
them on the real number line. For example, the absolute difference of -5 and 5
is 10, and the absolute difference of -5 and -4 is 1.

You can assume that there will only be one pair of numbers with the smallest
difference.

Sample input:
arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

Sample output:
[28, 26]
"""

def smallestDifference(arrayOne, arrayTwo):
  left, right = 0, 0

  arrayOne.sort()
  arrayTwo.sort()

  smallest = [arrayOne[left], arrayTwo[right]]

  while left < len(arrayOne) and right < len(arrayTwo):
    dif = abs(arrayOne[left] - arrayTwo[right])
    if dif < abs(smallest[0] - smallest[1]):
      smallest[0], smallest[1] = arrayOne[left], arrayTwo[right]

    if left + 1 < len(arrayOne) and abs(arrayOne[left + 1] - arrayTwo[right]) < dif:
      left += 1
    else:
      right += 1

  return smallest

# Time: O(nlog(n) + nlog(m)) where n is len(arrayOne) and m is len(arrayTwo)
# Space: O(1)
