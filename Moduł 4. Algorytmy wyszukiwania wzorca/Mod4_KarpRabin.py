# Kamil Matula gr. D, 07.04.2020
# Moduł IV, algorytm 3: algorytm Karpa-Rabina

# Funkcję haszującą zaimplementowano na podstawie https://eduinf.waw.pl/inf/alg/001_search/0052.php.
# Jest to suma iloczynów wartości ASCII liczby i wielkości alfabetu podniesionej do kolejnej potęgi.
# Kod opracowano na podstawie https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/.

def KR(text, pattern):
    textlength = len(text)
    patternlength = len(pattern)
    primenumber = 97
    alphabetlength = 256
    patternhash = 0
    texthash = 0
    pattern = pattern.upper()
    text = text.upper()
    showIt = [" "] * len(text)
    found = False

    # Haszowanie wzorca i pierwszego fragmentu tekstu
    for i in range(patternlength):
        patternhash += (ord(pattern[i])*(alphabetlength**(patternlength-1-i))) % primenumber
        texthash += (ord(text[i])*(alphabetlength**(patternlength-1-i))) % primenumber
    patternhash = patternhash % primenumber
    texthash = texthash % primenumber

    # Przeszukiwanie tekstu
    for i in range(textlength - patternlength + 1):
        # Sprawdzenie, czy jest zgodność
        if patternhash == texthash:
            for j in range(patternlength):
                if text[i+j] != pattern[j]: break
            if j == patternlength - 1:             
                showIt[i] = "^"
                found = True

        # Dodajemy nową literę i usuwamy starą
        if i < textlength - patternlength:
            d = (alphabetlength**(patternlength-1)) % primenumber
            texthash = (ord(text[i+patternlength]) + alphabetlength*(texthash-d*ord(text[i]))) % primenumber

    # Wyświetlenie rezultatów
    print(" Wyszukuję wzorzec: " + pattern)
    print(" W tekście: " + text)
    print(" Nie znaleziono!") if found == False else print("            " + "".join(showIt))


# Testowanie
text = "GEEKS FOR GEEKS"
pattern = "GEEK"
KR(text, pattern)
print()
text = "PRZYKŁADOWY TEKST"
pattern = "skład"
KR(text,pattern)