# 25.02.2020, Kamil Matula
# Lab1, Algorytm 2: Odwrotna Notacja Polska

#Odwrotna Notacja Polska: z infiksowej do postfiksowej
def ONP(wyrazenie):
    print("W notacji infiksowej: ", wyrazenie)
    dane = wyrazenie.split(" ")
    priorytety = {"(": 0, "+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    stos = []
    wynik = []
    for i in dane:
        if i in priorytety:
            if len(stos) == 0 or i == "(":
                stos.append(i)
            elif priorytety.get(i) == priorytety.get(stos[len(stos) - 1]):
                wynik.append(stos[len(stos) - 1])
                stos.pop(len(stos) - 1)
                stos.append(i)
            elif priorytety.get(i) > priorytety.get(stos[len(stos) - 1]):
                stos.append(i)
            else: # mniejszy priorytet
                wynik.append(stos[len(stos) - 1])
                stos.pop(len(stos) - 1)
                if (len(stos) > 0):
                    if priorytety.get(i) == priorytety.get(stos[len(stos) - 1]):
                        wynik.append(stos[len(stos) - 1])
                        stos.pop(len(stos) - 1)
                stos.append(i)
        elif i == ")": 
            while stos[len(stos) - 1] != "(":
                wynik.append(stos[len(stos) - 1])
                stos.pop(len(stos) - 1)
            stos.pop(len(stos) - 1)
        else: wynik.append(i)
    while (len(stos) > 0): # opróżniamy stos jak już się skończy działanie
        wynik.append(stos[len(stos) - 1])
        stos.pop(len(stos) - 1)
    print("W notacji postfiksowej: ", ' '.join(wynik))


#Odwrotna Notacja Polska: z postfiksowej na infiksową
def ONPReverse(wyrazenie):
    dzialania = ["+", "-", "*", "/", "^"]
    stos = []
    dane = wyrazenie.split(" ")
    print("W notacji postfiksowej: ", wyrazenie)
    for i in dane:
        if i in dzialania:
            a, b = stos[len(stos) - 2], stos[len(stos) - 1]
            del stos[-2:]
            stos.append("(" + a + i + b + ")")
        else: stos.append(i)
    print("W notacji infiksowej: ", ' '.join(stos))

wyrazenie = "3 + 4 * 2 / ( 1 - 5 ) ^ 2"
ONP(wyrazenie)
print()
wyrazenie = "7 2 * 3 1 * + 3 4 * + 1 1 / -"
ONPReverse(wyrazenie)