"""
The lesson in this one is to name variables in a meaningful way.
Using i and j messes me up more than anything on these sorting algorithms.
"""
def selectionSort(array):
  for i in range(len(array)):
    smallestIdx = i

    # I could do i + 1 here for a micro optimization
    # Worth pointing out, but I don't think it makes the code easier to read.
    for currentIdx in range(i, len(array)):
      if array[currentIdx] < array[smallestIdx]:
        smallestIdx = currentIdx
    array[i], array[smallestIdx] = array[smallestIdx], array[i]

  return array

# Space is O(1) because we are modifying the array in place.
# Time is O(n^2) where n is the length of the array.
