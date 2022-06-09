# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array):
    return productSummer(array, 1)

def productSummer(array, depth):
    sum = 0
    for item in array:
        if type(item) is int:
            sum += item
        else:
            sum += productSummer(item, depth + 1)

    return sum * depth


print(productSum([1, 2, 3])) #=> 6
print(productSum([1, 2, [3]])) #=> 12
