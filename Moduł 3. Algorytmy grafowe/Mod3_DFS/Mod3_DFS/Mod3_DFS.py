# Kamil Matula gr. D, 25.03.2020
# Moduł III, algorytm 4: DFS

# UWAGA: Ta implementacja działa tylko dla grafów of wierzchołkach liczbowych

def DFS(adjacency, start):
    firstVertex = list(adjacency.keys())[0]
    states = ["nieodwiedzony"] * len(adjacency)
    visitedInOrder = []

    def visit(vertex):
        states[vertex - firstVertex] = "odwiedzony"
        visitedInOrder.append(vertex)
        for otherOne in adjacency[vertex]:
            if states[otherOne - firstVertex] == "nieodwiedzony":
                visit(otherOne)
      
    visit(start)
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

DFS(adjacencyList, 1)