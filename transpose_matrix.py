def transposeMatrix(matrix):
    output = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]

    for i, row in enumerate(matrix):
        for j, ele in enumerate(row):
            output[j][i] = ele

    return output
