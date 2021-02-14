# 03.03.2020, Kamil Matula gr. D
# Zestaw II, algorytm 1: Kolejka

# Z "zawijaniem":
class Queue(object):
    def __init__(self, maxlength):
        self.maxlength = maxlength
        self.tail = 0               #indeks pierwszego wolnego miejsca
        self.head = 0               #indeks pierwszego zajetego miejsca
        self.count = 0
        self.queue = []
        for i in range(maxlength): self.queue.append("nic")
    def isFull(self):
        if self.count == self.maxlength: return True
        return False
    def isEmpty(self):
        if self.count == 0: return True
        return False
    def add(self, number):
        if self.isFull() == False:
            print("Do kolejki dołożono " + str(number))
            self.queue[self.tail] = number
            self.tail = (self.tail + 1) % self.maxlength
            self.count += 1
        else: print("Kolejka jest pełna - nie można dołożyć elementu " + str(number) + "!")
    def remove(self):
        if self.isEmpty() == False:
            print("Z kolejki usunięto " + str(self.queue[self.head]))
            self.queue[self.head] = "nic"
            self.head = (self.head + 1) % self.maxlength
            self.count -= 1
        else: print("Kolejka jest pusta - nie można usunąć elementu z jej początku!")
    def firstOne(self):
        if self.isEmpty() == False:
            print("Na początku kolejki znajduje się " + str(self.queue[self.head]))
        else: print("Kolejka jest pusta - nie ma elementu na jej początku!")
    def lastOne(self):
        if self.isEmpty() == False:
            print("Na końcu kolejki znajduje się " + str(self.queue[(self.tail - 1) % self.maxlength]))
        else: print("Kolejka jest pusta - nie ma elementu na jej końcu!")
    def show(self):
        print(self.queue)

# Testy:
kolejka = Queue(5)
kolejka.show()
kolejka.remove()
kolejka.add(5)
kolejka.add(4)
kolejka.add(3)
kolejka.add(2)
kolejka.add(1)
kolejka.add(0)
kolejka.show()
kolejka.firstOne()
kolejka.lastOne()
kolejka.remove()
kolejka.show()
kolejka.remove()
kolejka.add(0)
kolejka.show()


# Bez "zawijania":
"""
class Queue2(object):
    def __init__(self, maxlength):
        self.maxlength = maxlength - 1  #ilosc miejsc w tablicy/kolejce liczona od 0
        self.queue = []
        self.tail = 0                   #indeks pierwszego wolnego miejsca
    def isFull(self):
        if self.tail > self.maxlength: return True
        return False
    def isEmpty(self):
        if self.tail == 0: return True
        return False
    def add(self, number):
        if self.isFull() == False: 
            print("Do kolejki dołożono " + str(number))
            self.queue.append(number)
            self.tail += 1
        else: print("Kolejka jest pełna - nie można dołożyć elementu " + str(number) + "!")
    def remove(self):
        if self.isEmpty() == False: 
            print("Z kolejki usunięto " + str(self.queue[0]))
            self.queue.pop(0)
            self.tail -= 1
        else: print("Kolejka jest pusta - nie można usunąć elementu z jej początku!")
    def firstOne(self):
        if self.isEmpty() == False: print("Na początku kolejki znajduje się " + str(self.queue[0]))
        else: print("Kolejka jest pusta - nie ma elementu na jej początku!")
    def lastOne(self):
        if self.isEmpty() == False: print("Na końcu kolejki znajduje się " + str(self.queue[(self.tail - 1)]))
        else: print("Kolejka jest pusta - nie ma elementu na jej końcu!")
    def show(self):
        print(self.queue)
"""