# calc sum of diagonal elements of the matrix
if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6,], [7, 8, 9]]
    print('Matrix', matrix)
    diagonal_sum = 0
    length = len(matrix)
    for i in range(length):
        diagonal_sum += matrix[i][i]
    print('Sum of diagonal elements of the matrix =', diagonal_sum)
