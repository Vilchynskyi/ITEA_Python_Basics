# calc sum of the matrix
if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6,], [7, 8, 9]]
    sum = 0
    for row in matrix:
        for i in row:
            print(i)
            sum += i
    print('Sum of matrix =', sum)
