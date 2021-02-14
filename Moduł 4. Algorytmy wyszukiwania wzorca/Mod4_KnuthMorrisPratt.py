# Kamil Matula gr. D, 07.04.2020
# Moduł IV, algorytm 1: algorytm Knutha-Morrisa-Pratta

def KMP(text, pattern):
    def GeneratePrefixTable(pattern):
        PreTable = [0] * len(pattern)
        longest = 0
        for i in range (1, len(pattern)):
            while longest > 0 and pattern[longest] != pattern[i]: 
                longest = PreTable[longest]
            if pattern[longest] == pattern[i]: longest += 1
            PreTable[i] = longest
        return PreTable

    pattern = pattern.upper()
    text = text.upper()
    longest = 0
    showIt = [" "] * len(text)
    found = False

    # Przeszukiwanie
    PreTable = GeneratePrefixTable(pattern)
    for i in range (len(text)):
        while longest > 0 and pattern[longest] != text[i]: 
            longest = PreTable[longest]
        if pattern[longest] == text[i]: longest += 1
        if longest == len(pattern): 
            showIt[i - len(pattern) + 1] = "^"
            found = True
            longest = PreTable[longest - 1]

    # Wyświetlenie rezultatów:
    print(" Wyszukuję wzorzec: " + pattern)
    print(" W tekście: " + text)
    print(" Nie znaleziono!") if found == False else print("            " + "".join(showIt))

# Testowanie
pattern = "ACACAGTT"
text = "ACAT ACGACACAGTACGACACAGT"
KMP(text,pattern)
print()
pattern = "abcabcacab"
text = "babcbabcabcaabcabcabcacabc"
KMP(text, pattern)