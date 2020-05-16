# Kamil Matula, gr. D, 09.05.2020
# Moduł VII, Algorytm 4: Cuckoo Search / Algorytm Kukułki

import random
def RandomNumbers(leftend, rightend, n):
    return [random.uniform(leftend, rightend) for number in range(n)]

def CuckooMove(startPosition, leftend, rightend):
    import math
    newPosition = startPosition[:]
    for i in range(10):
        k = random.randint(0, len(startPosition) - 1)
        newPosition[k] += random.normalvariate(0, 1) * 0.01
        newPosition[k] = max(min(newPosition[k], rightend), leftend)
    return newPosition

def Sum_Squares(numberList):
    sum = 0
    for i in range(len(numberList)): sum += (i+1) * numberList[i] ** 2
    return sum

def Weierstrass(numberList):
    sum = 0
    for i in range(len(numberList)): sum += (abs(numberList[i] + 0.5)) ** 2
    return sum

def CuckooSearch(Function, leftEnd, rightEnd, dimension, searchingMinimum = True):
    generationCount = 10000       # liczba generacji
    nestCount       = 10          # liczba wszystkich gniazd
    nests = [RandomNumbers(leftEnd, rightEnd, dimension) for i in range(nestCount)] # początkowe gniazda
    adoptProbability = 0.8        # szansa na przyjęcie kukułczego jaja przez właściciela gniazda
    
    t = 0
    while t <= generationCount:
        indexOfStartNest = random.randint(0, nestCount - 1)               # wybieram losowe gniazdo
        startNest = nests[indexOfStartNest]
        newNest = CuckooMove(startNest, leftEnd, rightEnd)  # przemieszczam kukułkę na inne (nieodkryte) gniazdo
        if searchingMinimum == True:
            if Function(newNest) < Function(startNest) and random.random() < adoptProbability: # wyrzucam intruza / adoptuję jajo  
                nests[indexOfStartNest] = newNest
        else:
            if Function(newNest) > Function(startNest) and random.random() < adoptProbability:
                nests[indexOfStartNest] = newNest

        # Niszczą się najgorsze gniazda, a w ich miejsce pojawiają się nowe:
        nests.sort(key=lambda x: Function(x))
        if searchingMinimum == False: nests.reverse()
        nests = nests[:(nestCount//2)]
        newNests = [RandomNumbers(leftEnd, rightEnd, dimension) for i in range(nestCount - len(nests) + 1)]
        nests.extend(newNests)
        t += 1

    # Wybór najlepszego rozwiązania:
    bestVector = nests[0]
    for x in range (len(bestVector)): bestVector[x] = round(bestVector[x], 5)
    extremum = "MAXIMUM" if searchingMinimum == False else "MINIMUM"
    print("         ### ", str(Function.__name__).upper() + "'S", extremum, " ###\n   x  =", bestVector, \
        "\n f(x) =", round(Function(bestVector), 5), "\n")

CuckooSearch(Sum_Squares, -10, 10, 5, True)
CuckooSearch(Weierstrass, -10, 10, 5, True)
CuckooSearch(Sum_Squares, -10, 10, 5, False)
CuckooSearch(Weierstrass, -10, 10, 5, False)