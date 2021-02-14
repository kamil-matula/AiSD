# 03.03.2020, Kamil Matula
# Zestaw II, algorytm 2: Kolejka z priorytetem

# Z "zawijaniem":
class QueuePrio(object):
    def __init__(self, maxlength, priorities):
        self.maxlength = maxlength
        self.priorities = priorities  #tablica priorytetów; najważniejszy element po lewej, najmniej ważny po prawej
        self.tail = 0
        self.head = 0
        self.count = 0
        self.queue = []
        for i in range(maxlength): self.queue.append("nic")
        self.priorities.append("nic")
    def isFull(self):
        if self.count == self.maxlength: return True
        return False
    def isEmpty(self):
        if self.count == 0: return True
        return False
    def add(self, number):
        if self.isFull() == False:
            if number not in self.priorities:
                print("Nie można dołożyć elementu spoza listy priorytetów!")
                return
            currentIndex = self.head
            priority = self.priorities.index(number)
            while self.priorities.index(self.queue[currentIndex]) < priority:
                currentIndex = (currentIndex + 1) % self.maxlength
            tailIndex = self.tail
            while tailIndex != currentIndex:
                self.queue[tailIndex] = self.queue[tailIndex - 1]
                tailIndex = (tailIndex - 1) % self.maxlength
            self.queue[currentIndex] = number
            print("Do kolejki dołożono " + str(number))
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
kolejka = QueuePrio(4, [0,1,2])
kolejka.show()
kolejka.remove()
kolejka.add(2)
kolejka.show()
kolejka.add(2)
kolejka.show()
kolejka.add(1)
kolejka.show()
kolejka.add(5)
kolejka.add(2)
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
class QueuePrio2(object):
    def __init__(self, maxlength, priorities):
        self.maxlength = maxlength
        self.priorities = priorities
        self.queue = []
        self.tail = 0
    def isFull(self):
        if self.tail == self.maxlength: return True
        return False
    def isEmpty(self):
        if self.tail == 0: return True
        return False
    def add(self, number):
        if self.isFull() == False:
            if number not in self.priorities:
                print("Nie można dołożyć elementu spoza listy priorytetów!")
                return
            currentIndex = 0
            priority = self.priorities.index(number)
            while currentIndex < self.tail and self.priorities.index(self.queue[currentIndex]) < priority:
                currentIndex += 1
            self.queue.insert(currentIndex, number)
            print("Do kolejki dołożono " + str(number))
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