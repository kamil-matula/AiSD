# 10.03.2020, Kamil Matula gr. D
# Zestaw II, algorytm 6: Lista Cykliczna (jednokierunkowa)

class Node(object):
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    def __str__(self): #(aktualny, następny)
        return "(" + str(self.data) + ", " + str(self.next.data) + ")"

class ListaCyklicznaJed(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def __str__(self):
        tab = []
        currentIndex = 0
        currentNode = self.head
        while currentIndex < self.count:
            tab.append(str(currentNode))
            currentNode = currentNode.next
            currentIndex += 1
        return str(tab)

    def addToList(self, index, element):
        if index < 0 or index > self.count or index != int(index):
            print("Nieprawidłowy indeks!")
        else:
            if index == 0:
                self.head = Node(element, self.head)
                currentIndex = 0
                currentNode = self.head
                while currentIndex < self.count:
                    currentNode = currentNode.next
                    currentIndex += 1
                currentNode.next = self.head
            else:
                currentIndex = 0
                currentNode = self.head
                while currentIndex < index - 1:
                    currentNode = currentNode.next
                    currentIndex += 1
                currentNode.next = Node(element, currentNode.next)
            self.count += 1
    
    def removeFromList(self, index):
        if index < 0 or index > self.count - 1 or index != int(index):
            print("Nieprawidłowy indeks!")
        else:
            if index == 0:
                currentIndex = 0
                currentNode = self.head
                while currentIndex < self.count - 1:
                    currentNode = currentNode.next
                    currentIndex += 1
                self.head = self.head.next
                currentNode.next = self.head
            else:
                currentIndex = 0
                currentNode = self.head
                while currentIndex < index - 1:
                    currentNode = currentNode.next
                    currentIndex += 1
                currentNode.next = currentNode.next.next
            self.count -= 1

    def showAt(self, index):
        if index < 0 or index > self.count or index != int(index):
            print("Nieprawidłowy indeks!")
        else:
            currentIndex = 0
            currentNode = self.head
            while currentIndex < index:
                currentIndex += 1
                currentNode = currentNode.next
            return currentNode.data

    def indexOf(self, element):
        currentIndex = 0
        currentNode = self.head
        while currentIndex < self.count:
            if currentNode.data == element: return currentIndex
            currentIndex += 1
            currentNode = currentNode.next
        return None

#Testy
Lista = ListaCyklicznaJed()
Lista.addToList(0,213)
Lista.addToList(0,32)
Lista.addToList(1,23)
Lista.addToList(3,81)
Lista.addToList(4,5)
Lista.addToList(2,2)
print(Lista)
Lista.removeFromList(5)
Lista.removeFromList(0)
Lista.removeFromList(1)
print(Lista)
print(Lista.showAt(2))
print(Lista.indexOf(213))
print(Lista.indexOf("A"))