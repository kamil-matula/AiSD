# Kamil Matula, gr. D, 15.05.2020

import random, math, sys
def RandomNumbers(leftend, rightend, n):
    return [random.uniform(leftend, rightend) for number in range(n)]

def Sum_Squares(numberList):
    x = numberList[0]
    y = numberList[1]
    return x ** 2 + 2 * y ** 2

def Weierstrass(numberList):
    x = numberList[0]
    y = numberList[1]
    return (abs(x + 0.5)) ** 2 + (abs(y + 0.5)) ** 2

def TheOne(numberList):
    x = numberList[0]
    y = numberList[1]
    return (math.sin(x**2) + math.cos(y**2) - 10) ** 2 + 5 * (x-y) ** 2

class Bee(object):
    def __init__(self, position):
        self.position = position

def BeeAlgorithm(Function, leftEnd, rightEnd, searchingMinimum = True):
    generationCount = 100       # liczba generacji
    populationCount = 30        # liczba pszczół
    dimension       = 2         # wymiar wektorów
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
    print("x  = " + str(bestVector) + "\nf(x) = " + str(round(Function(bestVector), 5)) + "\n")

if sys.argv[1] == "0": functionName = Sum_Squares
elif sys.argv[1] == "1": functionName = Weierstrass
else: functionName = TheOne
searchingMinimum = True if sys.argv[4] == "0" else False
BeeAlgorithm(functionName, float(sys.argv[2].replace(",", ".")), float(sys.argv[3].replace(",", ".")), searchingMinimum)