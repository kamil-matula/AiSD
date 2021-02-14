# Kamil Matula, gr. D, 08.05.2020
# Moduł VII, Algorytm 1: Simulated Annealing Algorithm / Algorytm Wyżarzania

# Na podstawie: https://learnwithpanda.com/2020/04/04/python-code-of-simulated-annealing-optimization-algorithm/

import random, math
def RandomNumbers(leftend, rightend, n):
    return [random.uniform(leftend, rightend) for i in range(n)]

def Sum_Squares(numberList):
    sum = 0
    for i in range(len(numberList)): sum += (i+1) * numberList[i] ** 2
    return sum

def Weierstrass(numberList):
    sum = 0
    for i in range(len(numberList)): sum += (abs(numberList[i] + 0.5)) ** 2
    return sum


def Annealing(Function, leftEnd, rightEnd, dimension, searchingMinimum = True):
    coolingCoefficient = 0.9      # współczynnik chłodzenia; przez niego będzie mnożona co iterację temperatura
    absoluteTemperature = 1000    # temperatura startowa; będzie co iterację zmniejszana
    iterations = 1000             # liczba iteracji

    # Jako wektor inicjalizacyjny bierzemy 5 liczb z przedziału [leftEnd; rightEnd]
    # Staje się on jednocześnie aktualnie najlepszym rozwiązaniem
    bestVector = RandomNumbers(leftEnd, rightEnd, dimension)
    bestFitness = Function(bestVector)
    currentTemperature = absoluteTemperature

    for i in range(iterations):
        # Powtarzamy wielokrotnie, żeby uzyskać jak najlepszy krok podczas jednej iteracji:
        for j in range(50): 

            # Losujemy nowy wektor w sąsiedztwie aktualnie najlepszego
            newVector = bestVector[:]
            k = random.randint(0, dimension - 1)
            newVector[k] += 0.001 * random.uniform(leftEnd, rightEnd)
            newVector[k] = max(min(newVector[k], rightEnd), leftEnd)
            newFitness = Function(newVector)

            # Jeśli prawdopodobieństwo jest mniejsze od wylosowanej liczby z przedziału [0;1), nie zmieniamy nic
            if searchingMinimum == True:
                if newFitness > bestFitness:
                    # Prawdopodobieństwo funkcji o rozkładzie dwumianowym liczone jest zgodnie z równaniem termodynamiki procesu:
                    delta = newFitness - bestFitness
                    probability = math.exp( -delta / currentTemperature)
                    if random.random() > probability: 
                        continue
            else:
                 if newFitness < bestFitness:
                    # Prawdopodobieństwo funkcji o rozkładzie dwumianowym liczone jest zgodnie z równaniem termodynamiki procesu:
                    delta = newFitness - bestFitness
                    probability = math.exp( delta / currentTemperature)
                    if random.random() > probability: 
                        continue

            bestVector = newVector
            bestFitness = Function(bestVector)

        currentTemperature *= coolingCoefficient # zmniejszamy temperaturę

    for x in range (len(bestVector)): bestVector[x] = round(bestVector[x], 5)
    extremum = "MAXIMUM" if searchingMinimum == False else "MINIMUM"
    print("         ### ", str(Function.__name__).upper() + "'S", extremum, " ###\n   x  =", bestVector, \
        "\n f(x) =", round(bestFitness, 5), "\n")

Annealing(Sum_Squares, -10, 10, 5, True)
Annealing(Weierstrass, -10, 10, 5, True)
Annealing(Sum_Squares, -10, 10, 5, False)
Annealing(Weierstrass, -10, 10, 5, False)