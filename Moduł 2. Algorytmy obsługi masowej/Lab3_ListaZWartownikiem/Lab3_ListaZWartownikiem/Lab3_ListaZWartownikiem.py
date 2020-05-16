# 10.03.2020, Kamil Matula gr. D
# Zestaw II, algorytm 7: Lista (jednokierunkowa) z Wartownikiem

class Node(object):
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    def __str__(self): #(aktualny, następny)
        return "(" + str(self.data) + ", " + str(self.next.data) + ")"

class ListaJedZWar(object):
    def __init__(self):
        self.war = Node()
        self.war.next = self.war

    def __str__(self):
        tab = []
        currentNode = self.war.next
        while currentNode.data != None:
            tab.append(str(currentNode))
            currentNode = currentNode.next
        return str(tab)

    def addToList(self, index, element):
        if index < 0 or index > self.count() or index != int(index):
            print("Nieprawidłowy indeks!")
        elif index == 0:
            self.war.next = Node(element, self.war.next)
        else:
            currentIndex = 0
            currentNode = self.war.next
            while currentIndex < index - 1:
                currentNode = currentNode.next
                currentIndex += 1
            currentNode.next = Node(element, currentNode.next)
    
    def removeFromList(self, index):
        if index < 0 or index > self.count() - 1 or index != int(index):
            print("Nieprawidłowy indeks!")
        elif index == 0:
            self.war.next = self.war.next.next
        else:
            currentIndex = 0
            currentNode = self.war.next
            while currentIndex < index - 1:
                currentNode = currentNode.next
                currentIndex += 1
            currentNode.next = currentNode.next.next

    def showAt(self, index):
        if index < 0 or index > self.count() or index != int(index):
            print("Nieprawidłowy indeks!")
        else:
            currentIndex = 0
            currentNode = self.war.next
            while currentIndex < index:
                currentIndex += 1
                currentNode = currentNode.next
            return currentNode.data

    def indexOf(self, element):
        currentIndex = 0
        currentNode = self.war.next
        while currentNode.data != None:
            if currentNode.data == element: return currentIndex
            currentIndex += 1
            currentNode = currentNode.next
        return None

    def count(self):
        currentIndex = 0
        currentNode = self.war.next
        while currentNode.data != None:
            currentIndex += 1
            currentNode = currentNode.next
        return currentIndex

Lista = ListaJedZWar()
Lista.addToList(0,213)
Lista.addToList(0,32)
Lista.addToList(1,23)
Lista.addToList(3,81)
Lista.addToList(4,5)
Lista.addToList(2,2)
print(Lista)
print("Wartownik: " + str(Lista.war.data) + ", " + str(Lista.war.next.data))
Lista.removeFromList(5)
Lista.removeFromList(0)
Lista.removeFromList(1)
print(Lista)
print("Wartownik: " + str(Lista.war.data) + ", " + str(Lista.war.next.data))
print(Lista.showAt(2))
print(Lista.indexOf(213))
print(Lista.indexOf("A"))