# Kamil Matula, gr. D, 10.05.2020
# Moduł VII, Algorytm 9: Particle Swarm Optimization / Algorytm Roju Cząstek

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

class Particle(object):
    def __init__(self, position):
        self.position = position
        self.velocity = [0] * len(position)
        self.bestPosition = position

def ParticleSwarm(Function, leftEnd, rightEnd, dimension, searchingMinimum = True):
    generationCount = 200        # liczba generacji
    populationCount = 100        # liczba cząsteczek
    swarmPosRate    = 1.6        # współczynniki korekcji
    particlePosRate = 1.2
    velocityRate    = 0.1
    population = [Particle(RandomNumbers(leftEnd, rightEnd, dimension)) for i in range(populationCount)] # początkowa populacja

    # Wybór najlepszej cząsteczki:
    population.sort(key=lambda x: Function(x.position))
    if searchingMinimum == False: population.reverse()
    recentBestPosition = population[0].position

    t = 0
    while t <= generationCount:
        # Przemieszczanie się cząsteczek:
        for particle in population:
            for j in range(dimension):
                alfa = random.random()
                beta = random.random()
                # Aktualizacja prędkości:
                particle.velocity[j] = velocityRate * particle.velocity[j] \
                    + particlePosRate * alfa * (particle.bestPosition[j] - particle.position[j]) \
                    + swarmPosRate * beta * (recentBestPosition[j] - particle.position[j])
                # Aktualizacja pozycji (z uwzględnieniem przedziału):
                particle.position[j] = max(min(particle.position[j] + particle.velocity[j], rightEnd), leftEnd)
            # Aktualizacja najlepszej dotąd pozycji danej cząsteczki:
            if searchingMinimum == False:
                if Function(particle.position) > Function(particle.bestPosition): 
                    particle.bestPosition = particle.position[:]
            else:
                if Function(particle.position) < Function(particle.bestPosition): 
                    particle.bestPosition = particle.position[:]

        # Sortowanie cząsteczek i wybór najlepszej cząsteczki:
        population.sort(key=lambda x: Function(x.position))
        if searchingMinimum == False: 
            population.reverse()
            if Function(population[0].position) > Function(recentBestPosition): 
                recentBestPosition = population[0].position[:]
        else:
            if Function(population[0].position) < Function(recentBestPosition): 
                recentBestPosition = population[0].position[:]
        t += 1

    # Zwrócenie najlepszego rozwiązania:
    bestVector = recentBestPosition
    for x in range (len(bestVector)): bestVector[x] = round(bestVector[x], 5)
    extremum = "MAXIMUM" if searchingMinimum == False else "MINIMUM"
    print("         ### ", str(Function.__name__).upper() + "'S", extremum, " ###\n   x  =", bestVector, \
        "\n f(x) =", round(Function(bestVector), 5), "\n")

ParticleSwarm(Sum_Squares, -10, 10, 5, True)
ParticleSwarm(Weierstrass, -10, 10, 5, True)
ParticleSwarm(Sum_Squares, -10, 10, 5, False)
ParticleSwarm(Weierstrass, -10, 10, 5, False)