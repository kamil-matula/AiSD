# Kamil Matula gr. D, 08.04.2020
# Moduł V, algorytm 2: algorytm Huffmana

translationDictionary = {}

class Letter(object):
    def __init__(self, letter):
        self.letter = letter
        self.frequency = 1
        self.code = ""
    def updateCode(self, number):
        self.code = number + self.code
    def updateDict(self):
        translationDictionary[self.letter] = self.code

class Node(object):
    def __init__(self, leftChild = None, rightChild = None):
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.frequency = leftChild.frequency + rightChild.frequency
        self.leftChild.updateCode("0")
        self.rightChild.updateCode("1")
        self.code = ""
    def updateCode(self, number):
        self.code = number + self.code
        self.leftChild.updateCode(number)
        self.rightChild.updateCode(number)
    def updateDict(self):
        self.leftChild.updateDict()
        self.rightChild.updateDict()

def HuffmanMakeATree(sentence):
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
    tab.sort(key = Frequency)

    # Tworzenie drzewa:
    while len(tab) > 2:
        currentNode = Node(tab[0], tab[1])
        tab = tab[2:]
        for i in range(len(tab)):
            if tab[i].frequency >= currentNode.frequency:
                tab.insert(i, currentNode)
                break
            if i == len(tab) - 1: tab.append(currentNode)
    root = Node(tab[0], tab[1])
    return root

def HuffmanEncode(sentence):
    translationDictionary.clear()
    root = HuffmanMakeATree(sentence)
    root.updateDict()
    print(translationDictionary)

    encodedSentence = ""
    for sign in sentence:
        for item in translationDictionary.keys():
            if sign == item: 
                encodedSentence += translationDictionary[item]
    print(encodedSentence)

def HuffmanDecode(encodedsentence, dict):
    decodedsentence = ""
    while len(encodedsentence) > 0:
        for j in dict.keys():
            if encodedsentence.startswith(dict[j]):
                encodedsentence = encodedsentence[len(dict[j]):]
                decodedsentence += j
    print(decodedsentence)

# Testowanie:
sentence = "aaaaabbbbbbbbbccccccccccccdddddddddddddeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffff"
HuffmanEncode(sentence)
print()
sentence = "ciasteczko"
HuffmanEncode(sentence)
print()
HuffmanDecode("10111011111100110101010011000001", translationDictionary)