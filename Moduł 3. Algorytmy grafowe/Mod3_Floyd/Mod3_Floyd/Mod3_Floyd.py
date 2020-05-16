# Kamil Matula gr. D, 26.03.2020
# Moduł III, algorytm 2: algorytm Floyda

import sys
inf = sys.maxsize #infinity
def Floyd(matrix):
    def printMatrix(matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == inf: matrix[i][j] = "inf"
            print(matrix[i])

    vertices = len(matrix)
    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                matrix[i][j] = min(matrix[i][k] + matrix[k][j], matrix[i][j])
    printMatrix(matrix)


adjecancyMatrix = [[0,5,inf,10],
                   [inf,0,3,inf],
                   [inf,inf,0,1],
                   [inf,inf,inf,0]]
Floyd(adjecancyMatrix)