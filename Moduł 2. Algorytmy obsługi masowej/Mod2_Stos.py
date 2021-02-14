# 01.06.2020, Kamil Matula gr. D
# Zestaw II, algorytm 3: Stos - POPRAWA

class Stack(object):
    def __init__(self, maxlength):
        self.maxlength = maxlength   # statyczna wielkość stosu
        self.tail = 0                # indeks pierwszego wolnego miejsca w tablicy/stosie
        self.stack = ["nic" for i in range(maxlength)] # "pusta" tablica
    def isFull(self):
        if self.tail >= self.maxlength: return True
        return False
    def isEmpty(self):
        if self.tail == 0: return True
        return False
    def add(self, number):
        if self.isFull() == False:
            self.stack[self.tail] = number
            self.tail += 1
            print("Dodano element " + str(number))
        else: print("Stos jest pełny - nie można dodać elementu " + str(number) + "!")
    def remove(self):
        if self.isEmpty() == False:
            print("Usunięto element " + str(self.stack[self.tail - 1]))
            self.stack[self.tail - 1] = "nic"
            self.tail -= 1
        else: print("Stos jest pusty - nie można nic usunąć!")
    def topOne(self):
        if self.isEmpty() == False: return(self.stack[self.tail - 1])
        else: return("Stos jest pusty - nie ma elementu na wierzchu!")
    def show(self):
        print ("Stos: " + str(self.stack))

#Testy
stos = Stack(7)
stos.show()
stos.remove()
stos.add(5)
stos.show()
stos.add(4)
stos.add(3)
stos.add(2)
stos.add(1)
stos.add(5)
stos.add(2)
stos.show()
stos.add(3)
stos.show()
stos.remove()
stos.show()
print("Element na wierzchu: " + str(stos.topOne()))