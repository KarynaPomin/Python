# Zad 1
def Podciagi(Ciag):
    n = len(Ciag)

    for dl in range(1, n + 1):
        for indexPocz in range(n - dl + 1):
            print(Ciag[indexPocz : indexPocz + dl])

def Zad_1():
    plik = open("liczby.txt", "r")
    Ciag = list(map(int, plik.read().split()))

    Podciagi(Ciag)

Zad_1()
