def longestPeak(array):
  if len(array) < 3:
    return 0

  longestPeak = 0
  i = 1
  while i < len(array) - 1:
    left = i - 1
    right = i + 1
    if array[i] > array[left] and array[i] > array[right]:
      while left > 0 and array[left] > array[left - 1]:
        left -= 1

      while right < len(array) - 1 and array[right] > array[right + 1]:
        right += 1

      currentPeak = right - left + 1
      if currentPeak > longestPeak:
        print(left, right)
        longestPeak = currentPeak
    i = right

  return longestPeak
