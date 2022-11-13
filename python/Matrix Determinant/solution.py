def determinant(matrix):
    result = 0
    len_matrix = len(matrix)

    if len_matrix == 1:
        return matrix[0][0]

    if len_matrix == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    for j in range(len_matrix):
        minor = [row[:j] + row[j + 1:] for row in matrix[1:]]
        result += (-1)**j * matrix[0][j] * determinant(minor)
    return result
