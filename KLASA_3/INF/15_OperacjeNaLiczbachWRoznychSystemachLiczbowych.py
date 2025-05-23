# Wersja z funkcją wbudowaną
def Zad_2_1():
    liczba1 = int(input("Podaj liczbę binarną: "), 2)
    liczba2 = int(input("Podaj liczbę binarną: "), 2)
    suma = liczba1 + liczba2
    print(bin(suma)[2:])

# Wersja bez funkcji wbudowanych
def Zad_2_2():
    bin1 = input("Podaj liczbę binarną: ")
    bin2 = input("Podaj liczbę binarną: ")
    dl_bin1 = len(bin1)
    dl_bin2 = len(bin2)
    wynik = ""

    if (dl_bin1 > dl_bin2):
        bin2 = "0" * (dl_bin1 - dl_bin2) + bin2
        dl_bin2 = dl_bin1
    else:
        bin1 = "0" * (dl_bin2 - dl_bin1) + bin1
        dl_bin1 = dl_bin2
    print(bin1, bin2)

    przeniesienie = 0
    for i in range(dl_bin1 - 1, -1, -1):
        cyfraWyniku = int(bin1[i]) + int(bin2[i]) + przeniesienie

        if (cyfraWyniku > 1):
            przeniesienie = 1
            cyfraWyniku = cyfraWyniku % 2
        else:
            przeniesienie = 0

        wynik = str(cyfraWyniku) + wynik
    if (przeniesienie == 1):
        wynik = "1" + wynik

    print(wynik)

# !!! nie dokońcozone
# Wersja z funkcją wbudowanych
def Zad_3_1():
    p = int(input("Podaj podstawę: "))
    liczba1 = int(input("Podaj liczbę binarną: "), p)
    liczba2 = int(input("Podaj liczbę binarną: "), p)

    if (p >= 2 and p <= 9):
        suma = liczba1 + liczba2
        print(bin(suma)[2:])

# Wersja bez funkcji wbudowanych
def PtoDec(liczba, p):
    if liczba == 0:
        return "0"
    wynik = ""
    while liczba > 0:
        cyfra = str(liczba % p)
        if (int(cyfra) > 9):
            match int(cyfra):
                case 10:
                    cyfra = "A"
                case 11:
                    cyfra = "B"
                case 12:
                    cyfra = "C"
                case 13:
                    cyfra = "D"
                case 14:
                    cyfra = "E"
                case 15:
                    cyfra = "F" 

        wynik = cyfra + wynik
        liczba //= p
    return wynik

def Zad_3_2():
    p = int(input("Podaj podstawę: "))
    liczba = int(input(f"Podaj liczbę dec: "))

    print(f"Liczba o podstawie: {PtoDec(liczba, p)}")
