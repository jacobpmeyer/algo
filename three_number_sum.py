"""
Three number sum

Write a function that takes in a non-empty array of distinct integers and an
integer representing a target sum. The function should find all triplets in
the array that sum up to the target sum and return a two-dimensional array of
all these triplets. The numbers in each triplet should be ordered in ascending
order, and the triplets themselves should be ordered in ascending order with
respect to the numbers they hold.

array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0
"""

def threeNumberSum(array, targetSum):
  threes = []

  array.sort()

  for top, _ in enumerate(array):
    front = top + 1
    back = len(array) - 1

    while front < back:
      total = [array[top], array[front], array[back]]
      if sum(total) == targetSum:
        threes.append(total)
        front += 1
        back -= 1
      elif sum(total) < targetSum:
        front += 1
      else:
        back -= 1

  return threes


array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0

print(threeNumberSum(array, targetSum))

# Time: O(n^2)
# Space: O(n)
# n = length of array
