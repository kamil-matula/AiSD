# 25.02.2020, Kamil Matula
# Lab1, Algorytm 1: Wyszukiwanie największego elementu w zbiorze

def maxElem(lista):
    max = lista[0]
    for i in range(1,len(lista)):
        if lista[i] > max:
            max = lista[i]
    return max

def prepareList(input):
    lista = input.replace("[","").replace("]","").replace(" ","").split(',') 
    for i in range(len(lista)): 
        lista[i] = float(lista[i])
        if lista[i] == int(lista[i]): lista[i] = int(lista[i])
    return lista

lista = prepareList(input("Wprowadź listę: ")) #np. [5,4,3,2,1] lub [5, 4, 3, 2, 1] lub bez nawiasów
print("Największy element tej listy to", maxElem(lista))