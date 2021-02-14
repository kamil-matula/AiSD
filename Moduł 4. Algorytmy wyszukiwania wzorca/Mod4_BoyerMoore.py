# Kamil Matula gr. D, 07.04.2020
# Moduł IV, algorytm 2: algorytm Boyera-Moore'a

def BM(text, pattern):
    def GenerateCharsTable(pattern):
        lettersandvalues = {}
        for i in range (patternlength):
            lettersandvalues[pattern[i]] = max(1, patternlength - i - 1)
        return lettersandvalues
    
    pattern = pattern.upper()
    text = text.upper()
    patternlength = len(pattern)
    textlength = len(text)
    i = 0
    showIt = [" "] * len(text)
    found = False

    # Przeszukiwanie tekstu
    letters = GenerateCharsTable(pattern)
    while i <= textlength - patternlength:
        j = patternlength - 1
        while pattern[j] == text[i+j] and j > 0: j-= 1
        if j == 0: 
            showIt[i] = "^"
            found = True
            i += patternlength
        elif text[i+j] in pattern: i += letters[text[i+j]]
        else: i += patternlength

    # Wyświetlenie rezultatów
    print(" Wyszukuję wzorzec: " + pattern)
    print(" W tekście: " + text)
    print(" Nie znaleziono!") if found == False else print("            " + "".join(showIt))
        
        
# Testowanie
text = "this is a test that is tested"
pattern = "test"
BM(text, pattern)
print()
pattern = "set"
BM(text, pattern)