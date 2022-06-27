def isMonotonic(array):
  direction = "UP"

  i = 0
  while i < len(array) - 1 and array[i] == array[i + 1]:
    i += 1

  if i < len(array) - 1 and array[i] > array[i + 1]:
    direction = "DOWN"

  while i < len(array) - 1:
    if direction == "UP" and array[i] > array[i + 1]:
      return False
    elif direction == "DOWN" and array[i] < array[i + 1]:
      return False
    i += 1

  return True
