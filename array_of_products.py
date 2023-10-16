def arrayOfProducts(array):
    # [5, 1, 4, 2]
    # [1, 5, 5, 20]
    # [8, 8, 2, 1]

    leftProducts = [1 for i in range(len(array))]
    rightProducts = [1 for i in range(len(array))]
    products = [1 for i in range(len(array))]

    for i in range(1, len(array)):
        leftProducts[i] = array[i - 1] * leftProducts[i - 1]

    for j in reversed(range(len(array) - 1)):
        rightProducts[j] = array[j + 1] * rightProducts[j + 1]

    for i in range(len(array)):
        products[i] = leftProducts[i] * rightProducts[i]

    return products
