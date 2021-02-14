# Kamil Matula gr. D, 08.04.2020
# Moduł V, algorytm 1: szyfr Cezara

def CaesarCipherEnglish(decision, move, sentence): # Wersja prostsza: alfabet angielski, małe litery - nic poza tym
    alphabet = "abcdefghijklmnopqrstuvwxyz" #angielski alfabet
    encodedsentence = ""
    if move != int(move) or move < 0:
        print(" Wrong input!")
        return
    for sign in sentence:
        if sign not in alphabet:
            print(" Wrong input!")
            return

    if decision == 1:
        for letter in sentence:
            newindex = (alphabet.index(letter) + move) % len(alphabet)
            encodedsentence += alphabet[newindex]
    elif decision == 2:
        for letter in sentence:
            newindex = (alphabet.index(letter) - move) % len(alphabet)
            encodedsentence += alphabet[newindex]
    else:
        print(" Wrong input!")
        return

    print(" Input:", sentence)
    print(" Move:", "+" + str(move) if decision == 1 else "-" + str(move))
    print(" Output:", encodedsentence)
    print()

def CaesarCipherASCII(decision, move, sentence): # Wersja lepsza: poruszanie się po znakach ASCII (32-127)
    encodedsentence = ""
    if move != int(move):
        print(" Wrong input!")
        return

    if decision == 1:
        for letter in sentence:
            newvalue = (ord(letter) + move) % 127 # bez DELETE
            if newvalue < 32: newvalue += 32      # bez kodów z początku ASCII
            encodedsentence += chr(newvalue)
    elif decision == 2:
        for letter in sentence:
            newvalue = (ord(letter) - move) % 127
            if newvalue < 32: newvalue += 95
            encodedsentence += chr(newvalue)
    else:
        print(" Wrong input!")
        return

    print(" Input:", sentence)
    print(" Move:", "+" + str(move) if decision == 1 else "-" + str(move))
    print(" Output:", encodedsentence)
    print()

# Testowanie:
CaesarCipherEnglish(1, 5, "abcxyz") #fghcde
CaesarCipherEnglish(2, 3, "def")    #abc
CaesarCipherASCII(1, 5, "ABCabX")   #FGHfg]
CaesarCipherASCII(2, 3, "DeF dEf")  #AbC|aBc