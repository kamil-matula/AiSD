# Kamil Matula gr. D, 26.03.2020
# Moduł III, algorytm 1: algorytm Dijkstry

import sys
def Dijkstra(matrix, start):
    def currentMinimum(shortest, found):
        minimum = sys.maxsize
        for i in range(len(shortest)):
            if shortest[i] < minimum and i not in found:
                minimum = shortest[i]
        return shortest.index(minimum)

    def showthePath(shortest, path):
        for i in range(1, len(shortest)):
            temp = [i]
            current = i
            while path[current] != temp[0]:
                temp.insert(0, path[current])
                current = path[current]
            print("PATH: ", temp, " => LENGTH: ", shortest[i])

    shortest = [sys.maxsize]*len(matrix)
    path = [start]*len(matrix)
    found = []
    goingFrom = start

    while len(found) < len(matrix):
        found.append(goingFrom)
        for goingTo in range(1, len(matrix)):
            if goingTo not in found:
                if matrix[goingFrom][goingTo] != 0:
                    if shortest[goingFrom] == sys.maxsize:
                        shortest[goingTo] = matrix[goingFrom][goingTo]
                        path[goingTo] = goingFrom
                    elif shortest[goingFrom] + matrix[goingFrom][goingTo] < shortest[goingTo]:
                        shortest[goingTo] = matrix[goingFrom][goingTo] + shortest[goingFrom]
                        path[goingTo] = goingFrom
        goingFrom = currentMinimum(shortest, found)
    showthePath(shortest,path)

adjacencyMatrix = [[0,10,0,30,0,0,0],
                   [10,0,12,0,0,0,0],
                   [0,12,0,5,40,0,0],
                   [30,0,5,0,0,0,25],
                   [0,0,40,0,0,20,10],
                   [0,0,0,0,20,0,5],
                   [0,0,0,25,10,5,0]]

Dijkstra(adjacencyMatrix, 0)