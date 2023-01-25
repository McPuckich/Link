matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
tmatrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        tmatrix[j][i] = matrix[i][j]
print(matrix)
print(tmatrix)
