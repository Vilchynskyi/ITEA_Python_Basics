# calc sum of the upper diagonal of the matrix
if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6,], [7, 8, 9]]
    k = 0
    diagonal_sum = 0
    for row in matrix:
        for i in row[k:]:
            print(i)
            diagonal_sum += i
        k += 1
    print(diagonal_sum)
