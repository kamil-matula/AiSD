# Kamil Matula gr. D, 08.04.2020
# Moduł V, algorytm 3: algorytm Shannona-Fano

translationDictionary = {}

class Letter(object):
    def __init__(self, letter):
        self.letter = letter
        self.frequency = 1
        self.code = ""
    def updateCode(self, number):
        self.code += number
    def updateDict(self):
        translationDictionary[self.letter] = self.code

class Node(object):
    def __init__(self, leftChild = None, rightChild = None):
        self.code = ""
        if isinstance(leftChild, list):
            for letter in leftChild: letter.updateCode("0")
            self.leftChild = DivideList(leftChild)
        else:
            leftChild.updateCode("0")
            self.leftChild = leftChild
        if isinstance(rightChild, list):
            for letter in rightChild: letter.updateCode("1")
            self.rightChild = DivideList(rightChild)
        else:
            rightChild.updateCode("1")
            self.rightChild = rightChild
    def updateCode(self, number):
        self.code += number
        self.leftChild.updateCode(number)
        self.rightChild.updateCode(number)
    def updateDict(self):
        self.leftChild.updateDict()
        self.rightChild.updateDict()

def ShannonFanoMakeATree(sentence):
    def Frequency(x): return x.frequency
    # Pobranie liter:
    tab = []
    tab.append(Letter(sentence[0]))
    for i in range (1, len(sentence)):
        for j in range(0, len(tab)):
            if tab[j].letter == sentence[i]:
                tab[j].frequency += 1
                break
            if j == len(tab) - 1: 
                tab.append(Letter(sentence[i]))
    tab.sort(key = Frequency, reverse=True)

    # Tworzenie drzewa:
    root = DivideList(tab)
    return root

def ShannonFanoEncode(sentence):
    translationDictionary.clear()
    root = ShannonFanoMakeATree(sentence)
    root.updateDict()
    print(translationDictionary)

    encodedSentence = ""
    for sign in sentence:
        for item in translationDictionary.keys():
            if sign == item: 
                encodedSentence += translationDictionary[item]
    print(encodedSentence)

def ShannonFanoDecode(encodedsentence, dict):
    decodedsentence = ""
    while len(encodedsentence) > 0:
        for j in dict.keys():
            if encodedsentence.startswith(dict[j]):
                encodedsentence = encodedsentence[len(dict[j]):]
                decodedsentence += j
    print(decodedsentence)

def DivideList(tab):
    def ReturnDifference(x): return x[1]
    def CalculateDifference(tab, index):
        sumLeft = 0
        sumRight = 0
        for item in tab[:i]: sumLeft += item.frequency
        for item in tab[i:]: sumRight += item.frequency
        return abs(sumLeft - sumRight)

    if len(tab) == 2:
        return Node(tab[0], tab[1])
    else:
        # Znajdź "najbliższe" sobie elementy:
        Differences = []
        for i in range(len(tab)):
            Differences.append((i, CalculateDifference(tab,i)))
        Differences.sort(key = ReturnDifference)
        DivisionPlace = Differences[0][0]

        # Podziel tablicę:
        if len(Differences[:DivisionPlace]) == 1: return Node(tab[0], tab[1:])
        elif len(Differences[DivisionPlace:]) == 1: return Node(tab[:-1], tab[-1])
        else: return Node(tab[:DivisionPlace], tab[DivisionPlace:])

# Testowanie:
ShannonFanoEncode("MISSISSIPPI") # powinno być: {S: 0, I: 10, P, 110, M: 111} - i jest
print()
ShannonFanoEncode("aabbbbcccccc") # powinno być: {a: 11, b:10, c:0} - i jest
print()
ShannonFanoDecode("111110101010000000", translationDictionary)