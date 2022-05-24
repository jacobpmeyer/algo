def sortedSquaredArray(array):
	# Look at the absolute value of two numbers.
	# When the value of the second number is greater than the first, stop checking.
	# Add the lower number to the array and then check the numbers around, adding each to the array until you find the end of the array.
	# cases:
	# 	[1]
	# 	[1, 2]
	# 	[-2]
	# 	[-2, -1]
	# 	[-3, 0]
	# 	[-3, 0, 1]
	# 	[-3, 0, 1, 2]
  #   i = front pointer
  #   j = backwards pointer
  # once i is either at the end of the array or array[i] is no longer negative,
  # the condition to for the backwards pointer is i == 0
  i = 0
  j = -1
  output = []

  while i < len(array) and array[i] < 1:
    i += 1
    j += 1

  while i < len(array) and j >= 0:
    sqrI = array[i] * array[i]
    sqrJ = array[j] * array[j]
    if abs(array[i]) < abs(array[j]):
      output.append(sqrI)
      i += 1
    else:
      output.append(sqrJ)
      j -= 1

  while i < len(array) and i >= 0:
    output.append(array[i] * array[i])
    i += 1

  while j >= 0 and j < len(array):
    output.append(array[j] * array[j])
    j -= 1

  return output
