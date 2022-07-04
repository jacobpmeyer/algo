def arrayOfProducts(array):
  zeroes = numOfZeroes(array)
  prod = getProduct(array)
  if zeroes > 1:
    return [0 for i in range(len(array))]
  elif zeroes is 1:
    return handleOneZero(array, prod)
  else:
    return handleNoZeroes(array, prod)


def numOfZeroes(array):
  count = 0
  for num in array:
    if num == 0:
      count += 1

  return count


def getProduct(array):
  prod = 1
  for num in array:
    if num != 0:
      prod *= num

  return prod


def handleOneZero(array, prod):
  for i in range(len(array)):
    if array[i] is 0:
      array[i] = prod
    else:
      array[i] = 0

  return array


def handleNoZeroes(array, prod):
  for i in range(len(array)):
    array[i] = prod // array[i]

  return array
