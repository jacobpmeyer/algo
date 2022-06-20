"""
Good ole bubble sort

If memory serves, we will start with an unordered array and end up with a sorted
array in ascending order.

We accomplish this by iterating over the input array,
check each index against the next index,
if the next number is less than current, switch the values.
We keep doing this until the end of the array and then start all over.
If we pass over the array once without changing the positions of any values,
then we are done.

O(super slow)

fr though I think it's O(n^2), because worst case is that the array is
sorted in descending order, meaning the number of passes over the array would be
n - 1, which reduces to n

space is O(1), because we aren't creating any new arrays, but we might have
to make a few variables to keep track of state
"""
def bubbleSort(array):
  sorted = False

  while not sorted:
    sorted = True
    for i in range(len(array) - 1): # ranges in Python are exclusive
      currentEle = array[i]
      nextEle = array[i + 1]
      if currentEle > nextEle:
        array[i] = nextEle
        array[i + 1] = currentEle
        sorted = False

  return array
