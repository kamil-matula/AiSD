# 03.03.2020, Kamil Matula gr. D
# Zestaw II, algorytm 3: Stos

class Stack(object):
    def __init__(self, length):
        self.length = length - 1     #liczba miejsc w stosie (liczone od 0)
        self.tail = 0                #indeks pierwszego wolnego miejsca w tablicy/stosie
        self.stack = []
    def isFull(self):
        if self.tail > self.length: return True
        return False
    def isEmpty(self):
        if self.tail == 0: return True
        return False
    def add(self, number):
        if self.isFull() == False:
            self.stack.append(number)
            self.tail += 1
            print("Dodano element " + str(number))
        else: print("Stos jest pełny - nie można dodać elementu " + str(number) + "!")
    def remove(self):
        if self.isEmpty() == False:
            print("Usunięto element " + str(self.stack[self.tail - 1]))
            self.stack.pop(self.tail - 1)
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