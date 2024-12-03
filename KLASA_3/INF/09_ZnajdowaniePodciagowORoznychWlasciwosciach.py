plik = open("liczby.txt", "r")
Ciag = list(map(int, plik.read().split()))

# Zad 1
def WyswietlLiczbyPoSpacji(Tab):
    print(' '.join(map(str, Tab)))

def Podciagi(Ciag):
    n = len(Ciag)

    for dl in range(1, n + 1):
        for indexPocz in range(n - dl + 1):
            WyswietlLiczbyPoSpacji(Ciag[indexPocz : indexPocz + dl])

def Podciagi_1(Ciag):
    n = len(Ciag)

    for dl in range(1, n + 1):
        for indexPocz in range(n - dl + 1):
            indexKon = indexPocz + dl - 1

            for i in range(indexPocz, indexKon + 1):
                print(Ciag[i], end=' ')
            print()

# Zad 2
def Zad_2(Ciag):
    n = len(Ciag)

    for indexPocz in range(n + 1):
        for i in range(indexPocz, n + 1):
            WyswietlLiczbyPoSpacji(Ciag[indexPocz : i])

# Zad 3
def SumaCyfr(s):
    suma = 0

    for i in range(len(s)):
        a = int(s[i])
        while a > 0:
            suma += a % 10
            a //= 10

    return suma
def Zad_3(Ciag):
    n = len(Ciag)

    for indexPocz in range(n - 4):
        for i in range(indexPocz + 1, indexPocz + 6):
            print(SumaCyfr(Ciag[indexPocz: i]), end=" - ")
            WyswietlLiczbyPoSpacji(Ciag[indexPocz : i])

# Zad 4
# Zad 5

# Zad 6 i 9
def CzyCiagJestRosnacy(C):
    for i in range(len(C) - 1):
        if C[i] > C[i + 1]:
            return False
    return True

def Zad_6_9():
    C = list(map(int, input("Podaj ciąg po spacji: ").split(" ")))

    if CzyCiagJestRosnacy(C):
        print("Tak")
    else:
        print("Nie")

# Zad 7 i 8
def CzyCiagJesMalejacy(C):
    for i in range(len(C) - 1):
        if C[i] < C[i + 1]:
            return False
    return True

def Zad_7_8():
    C = list(map(int, input("Podaj ciąg po spacji: ").split(" ")))

    if CzyCiagJesMalejacy(C):
        print("Tak")
    else:
        print("Nie")

# Zad 10
def CzyCiagJestMonotoniczny(C):
    for i in range(1, len(C)):
        if C[1] != C[i]:
            return False
    return True

def Zad_10():
    C = list(map(int, input("Podaj ciąg po spacji: ").split(" ")))

    if CzyCiagJestMonotoniczny(C):
        print("Tak")
    else:
        print("Nie")

# Zad 11
def NajdluzszyCiagJestRosnacy(C):
    N = []
    Temp = []

    for i in range(len(C) - 1):
        if C[i] < C[i + 1]:
            Temp.append(C[i])
        else:
            if len(Temp) > len(N):
                N = Temp
            Temp = []
    return N
    
def Zad_11():
    print(len(NajdluzszyCiagJestRosnacy(Ciag)))

# Zad 12
def Zad_12():
    print(NajdluzszyCiagJestRosnacy(Ciag))
