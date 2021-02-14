# Kamil Matula, gr. D, 10.05.2020
# Moduł VII, Algorytm 7: Artificial Bee Colony Algorithm / Algorytm Pszczeli

# Na podstawie: https://en.wikipedia.org/wiki/Artificial_bee_colony_algorithm

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

class Bee(object):
    def __init__(self, position):
        self.position = position

def BeeAlgorithm(Function, leftEnd, rightEnd, dimension, searchingMinimum = True):
    generationCount = 50          # liczba generacji
    populationCount = 30          # liczba pszczół
    population = [Bee(RandomNumbers(leftEnd, rightEnd, dimension)) for i in range(populationCount)] # początkowa populacja

    t = 0
    while t <= generationCount:
        # Przemieszczanie się pszczół-robotnic:
        for bee in population:
            # Poszukują lepszej pozycji wielokrotnie zanim wrócą do ula:
            for i in range(15):
                alfa = random.uniform(-1,1)
                candidatePosition = bee.position[:]
                randomBee = Bee(bee.position)
                while randomBee.position == bee.position: 
                    randomBee = random.choice(population)
                k = random.randint(0, dimension - 1)
                candidatePosition[k] += alfa * (bee.position[k] - randomBee.position[k])
                candidatePosition[k] = max(min(candidatePosition[k], rightEnd), leftEnd)
                
                # Aktualizacja pozycji, jeśli znaleziono lepsze miejsce:
                if searchingMinimum == False and Function(candidatePosition) > Function(bee.position):
                    bee.position = candidatePosition[:]
                elif searchingMinimum == True and Function(candidatePosition) < Function(bee.position): 
                    bee.position = candidatePosition[:]

        # Sortowanie i wybór najbogatszych w nektar pozycji - najmniej bogate odpadają
        # (liczenie prawdopodobieństwa jest tu raczej niepotrzebne):
        population.sort(key=lambda x: Function(x.position))
        if searchingMinimum == False: population.reverse()
        population = population[:(populationCount // 3)]

        # Zwiadowcy znajdują jedzenie w nowych miejscach:
        population.extend([Bee(RandomNumbers(leftEnd, rightEnd, dimension)) \
                         for i in range(populationCount - len(population) + 1)])

        t += 1

    # Zwrócenie najlepszego rozwiązania:
    bestVector = population[0].position
    for x in range (len(bestVector)): bestVector[x] = round(bestVector[x], 5)
    extremum = "MAXIMUM" if searchingMinimum == False else "MINIMUM"
    print("         ### ", str(Function.__name__).upper() + "'S", extremum, " ###\n   x  =", bestVector, \
        "\n f(x) =", round(Function(bestVector), 5), "\n")

BeeAlgorithm(Sum_Squares, -10, 10, 5, True)
BeeAlgorithm(Weierstrass, -10, 10, 5, True)
BeeAlgorithm(Sum_Squares, -10, 10, 5, False)
BeeAlgorithm(Weierstrass, -10, 10, 5, False)