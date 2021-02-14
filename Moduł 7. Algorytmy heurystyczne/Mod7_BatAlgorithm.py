# Kamil Matula, gr. D, 12.05.2020
# Moduł VII, Algorytm 5: Bat Algorithm / Algorytm Nietoperza

# Na podstawie: https://github.com/buma/BatAlgorithm oraz https://www.hindawi.com/journals/acisc/2019/9864090/

import random
def RandomNumbers(leftend, rightend, n):
    return [random.uniform(leftend, rightend) for number in range(n)]

def Sum_Squares(numberList):
    sum = 0
    for i in range(len(numberList)): sum += (i+1) * numberList[i] ** 2
    return sum

def Weierstrass(numberList):
    sum = 0
    for i in range(len(numberList)): sum += (abs(numberList[i] + 0.5)) ** 2
    return sum

class Bat(object):
    def __init__(self, position):
        self.position = position
        self.velocity = [0.0] * len(position)

def BatAlgorithm(Function, leftEnd, rightEnd, dimension, searchingMinimum = True):
    generationCount = 500      # liczba generacji
    populationCount = 100      # liczba nietoperzy
    freqMin = 0.0              # częstotliwość minimalna
    freqMax = 2.0              # częstotliwość maksymalna
    loudness = 0.5             # głośność: liczba z przedziału [0; 1]
    pulseRate = 0.5            # współczynnik emisyjności impulsów: liczba z przedziału [0; 1]
    epsilon = 0.001            # współczynnik randomizacji
    

    population = [Bat(RandomNumbers(leftEnd, rightEnd, dimension)) for i in range(populationCount)] # początkowa populacja

    # Wyznaczamy lidera nietoperzy:
    population.sort(key=lambda x: Function(x.position))
    if searchingMinimum == False: population.reverse()
    leaderPosition = population[0].position[:]

    t = 0
    while t <= generationCount:
        # Przemieszczanie się nietoperzy:
        for bat in population:
            # Wyznaczenie wartości pulsacji i prędkości oraz wybór nowej pozycji:
            pulsation = freqMin + (freqMax - freqMin) * random.random()
            newPosition = bat.position[:]
            for k in range(dimension): 
                bat.velocity[k] += (bat.position[k] - leaderPosition[k]) * pulsation
                newPosition[k] = max(min(newPosition[k] + bat.velocity[k], rightEnd), leftEnd)

            # Lot w okolice lidera:
            if random.random() > pulseRate:
                for k in range(dimension):
                    newPosition[k] = leaderPosition[k] + epsilon * random.normalvariate(0, 1)
                    newPosition[k] = max(min(newPosition[k], rightEnd), leftEnd)

            # Aktualizacja pozycji nietoperza i pozycji lidera:
            if searchingMinimum == True:
                if Function(newPosition) <= Function(bat.position) and random.random() < loudness:
                    bat.positon = newPosition[:]
                if Function(newPosition) <= Function(leaderPosition):
                    leaderPosition = newPosition[:]
            else:
                if Function(newPosition) >= Function(bat.position) and random.random() < loudness:
                    bat.positon = newPosition[:]
                if Function(newPosition) >= Function(leaderPosition):
                    leaderPosition = newPosition[:]

        t += 1

    # Zwrócenie najlepszego rozwiązania:
    bestVector = leaderPosition
    for x in range (len(bestVector)): bestVector[x] = round(bestVector[x], 5)
    extremum = "MAXIMUM" if searchingMinimum == False else "MINIMUM"
    print("         ### ", str(Function.__name__).upper() + "'S", extremum, " ###\n   x  =", bestVector, \
        "\n f(x) =", round(Function(bestVector), 5), "\n")

BatAlgorithm(Sum_Squares, -10, 10, 5, True)
BatAlgorithm(Weierstrass, -10, 10, 5, True)
BatAlgorithm(Sum_Squares, -10, 10, 5, False)
BatAlgorithm(Weierstrass, -10, 10, 5, False)