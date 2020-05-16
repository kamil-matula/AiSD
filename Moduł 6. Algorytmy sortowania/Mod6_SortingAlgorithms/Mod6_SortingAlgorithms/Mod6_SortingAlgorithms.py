# Kamil Matula gr. D, 10.04.2020
# Moduł VI: Algorytmy sortujące

# FUNKCJE SORTUJĄCE:
def BubbleSort(arr):
    n = len(arr)
    for i in range(n - 1): # za (n-1)-tym razem tylko by sprawdzał
        for j in range(n - i - 1):
            if arr[j + 1] < arr[j]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
    return arr

def CountingSort(arr):
    # Zliczanie ilości wystąpień liczb
    minimum = min(arr)
    maximum = max(arr)
    counter = [0]*(maximum - minimum + 1)
    for i in range(len(arr)): counter[arr[i] - minimum] += 1

    # Wypisanie liczb odpowiednią ilość razy
    j = 0
    for i in range(len(counter)):
        while counter[i] > 0:
            arr[j] = i + minimum
            counter[i] -= 1
            j += 1
    return arr

def HeapSort(arr):
    def MaxHeapBranch(arr, start, stop):
        max_index = start
        lchild_index = 2 * start + 1 # nieparzysty element, który w drzewie byłby lewym dzieckiem
        rchild_index = 2 * start + 2 # parzysty element, który w drzewie byłby prawym dzieckiem
        if lchild_index < stop and arr[lchild_index] > arr[max_index]: max_index = lchild_index
        if rchild_index < stop and arr[rchild_index] > arr[max_index]: max_index = rchild_index
        if max_index != start:
            arr[start], arr[max_index] = arr[max_index], arr[start] # swap wewnątrz tej trójki
            MaxHeapBranch(arr, max_index, stop) # piętro niżej w drzewie
    
    arrlen = len(arr)
    for i in range(arrlen, -1, -1): MaxHeapBranch(arr, i, arrlen) # MaxHeap całego drzewa
    for i in range(arrlen - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # Najmniejszy element na dole, największy na górze
        MaxHeapBranch(arr, 0, i) # i-ty element stoi już na swoim miejscu, sortujemy resztę
    return arr

def MergeSort(arr):
    def Merge(arr, left, medium, right):
        Left = arr[left:(medium+1)]
        Right = arr[(medium+1):(right+1)]
        i = left
        while len(Left) > 0 and len(Right) > 0: # Porównywanie elementów z lewej i prawej połowy
            if Left[0] <= Right[0]: arr[i] = Left.pop(0)
            else: arr[i] = Right.pop(0)
            i += 1
        while len(Left) > 0: # Nadpisanie pozostałości lewej połowy
            arr[i] = Left.pop(0)
            i += 1
        while len(Right) > 0: # Nadpisanie pozostałości prawej połowy
            arr[i] = Right.pop(0)
            i += 1

    def Main(arr, left, right):
        if left < right:
            medium = (left + right) // 2
            Main(arr, left, medium) # Lewa połowa
            Main(arr, medium + 1, right) # Prawa połowa
            Merge(arr, left, medium, right)
    
    Main(arr, 0, len(arr) - 1)
    return arr

def QuickSort(arr):
    def partition(arr, start, stop):
        i = start - 1 # indeks przed początkiem
        pivot = arr[stop] # pivot jako ostatni element listy
        for j in range(start, stop):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[stop] = arr[stop], arr[i+1]
        return i+1

    def Main(arr, start, stop):
        if start < stop:
            PartitionPoint = partition(arr, start, stop)
            Main(arr, start, PartitionPoint - 1) # Część listy przed wyznaczonym elementem
            Main(arr, PartitionPoint + 1, stop) # Część listy po wyznaczonym elemencie

    Main(arr, 0, len(arr) - 1)
    return arr

def ShellSort(arr):
    gap = len(arr) // 2 # nie jest to odstęp optymalny, ale często używany
    while gap > 0:
        for i in range(gap, len(arr)):
            CaughtElement = arr[i]
            j = i
            while j >= gap and arr[j - gap] > CaughtElement: # Zmodyfikowany InsertionSort
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = CaughtElement
        gap = gap // 2
    return arr

# MIERZENIE CZASU - ANALIZA:
import random, time
SortingTimes = 5
listofnumbers1000 = []
for i in range(1000): listofnumbers1000.append(random.randint(1, 1000))
listofnumbers10000 = []
for i in range(10000): listofnumbers10000.append(random.randint(1, 1000))
listofnumbers100000 = []
for i in range(100000): listofnumbers100000.append(random.randint(1, 1000))
print()
print("RAPORT ALGORYTMÓW SORTOWANIA\n".center(110 + 20 * SortingTimes))
timesString = ""
for i in range(SortingTimes): timesString += ("CZAS " + str(i+1)).rjust(20)
print("NAZWA".center(15) + "ILOŚĆ LICZB".center(15) + timesString + "CZAS NAJKRÓTSZY".rjust(20) + "CZAS NAJDŁUŻSZY".rjust(20) + "CZAS ŚREDNI".rjust(20) + "BŁĄD STATYSTYCZNY".rjust(20) + "\n")

def SortIt(arr, function):
    gaps = []
    gapsString = ""
    for sortingtime in range(SortingTimes):
        unsortedlist = [arr[i] for i in range(len(arr))]
        start = time.time()
        sortedlist = function(unsortedlist)
        stop = time.time()
        gaps.append(round((stop - start) * 1000, 5)) # w milisekundach
    for i in range(SortingTimes): gapsString += (str(gaps[i]) + " ms").rjust(20)

    avg = sum(gaps)/SortingTimes
    err = 0
    for i in range(SortingTimes): err += (gaps[i] - avg)*(gaps[i] - avg)
    err = (err/SortingTimes)**(0.5)

    errString = (str(round(err, 5)) + " ms").rjust(20)
    avgString = (str(round(avg, 5)) + " ms").rjust(20)
    minString = (str(round(min(gaps), 5)) + " ms").rjust(20)
    maxString = (str(round(max(gaps), 5)) + " ms").rjust(20)
    print(function.__name__.center(15) + str(len(arr)).center(15) + gapsString + minString + maxString + avgString + errString)

SortIt(listofnumbers1000, BubbleSort)
SortIt(listofnumbers1000, CountingSort)
SortIt(listofnumbers1000, HeapSort)
SortIt(listofnumbers1000, MergeSort)
SortIt(listofnumbers1000, QuickSort)
SortIt(listofnumbers1000, ShellSort)

print()

SortIt(listofnumbers10000, BubbleSort)
SortIt(listofnumbers10000, CountingSort)
SortIt(listofnumbers10000, HeapSort)
SortIt(listofnumbers10000, MergeSort)
SortIt(listofnumbers10000, QuickSort)
SortIt(listofnumbers10000, ShellSort)

print()

#SortIt(listofnumbers100000, BubbleSort)
SortIt(listofnumbers100000, CountingSort)
SortIt(listofnumbers100000, HeapSort)
SortIt(listofnumbers100000, MergeSort)
SortIt(listofnumbers100000, QuickSort)
SortIt(listofnumbers100000, ShellSort)

print()
print("W ostatnim zestawie liczb nie testowano BubbleSorta, ponieważ czas działania wynosił zdecydowanie za długo (kilkanaście - kilkadziesiąt minut).".center(110 + 20 * SortingTimes))
print()
print()