# Kamil Matula gr. D, 25.03.2020
# Moduł III, algorytm 3: BFS

# UWAGA: Ta implementacja działa tylko dla grafów o wierzchołkach liczbowych

def BFS(adjacency, start):
    firstVertex = list(adjacency.keys())[0]
    states = ["nieodwiedzony"] * len(adjacency)
    queue = []
    visitedInOrder = []

    states[start - firstVertex] = "odwiedzony"
    queue.append(start)

    while len(queue) != 0:
        head = queue.pop(0)
        visitedInOrder.append(head)
        for otherOne in adjacency[head]:
            if states[otherOne - firstVertex] == "nieodwiedzony":
                queue.append(otherOne)
                states[otherOne - firstVertex] = "odwiedzony"
    return(print(visitedInOrder))

adjacencyList = {1: [2,3,4],
                 2: [1,5,6],
                 3: [1,7],
                 4: [1],
                 5: [2],
                 6: [2,8,9],
                 7: [3],
                 8: [6],
                 9: [6]}

BFS(adjacencyList, 1)