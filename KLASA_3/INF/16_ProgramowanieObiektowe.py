import math

### Przykład 1. ###
class Prostokat:
    def __init__(self, dlugosc, szerokosc):
        self.a = dlugosc
        self.b = szerokosc

    def pole(self):
        return self.a * self.b

    def obwod(self):
        return self.a * 2 + self.b * 2

def Zad_2():
    prostokat = Prostokat(3, 5)
  
    print("Pole prostakąta o bokach: ", prostokat.a, " i ", prostokat.b, "wynosi: ", prostokat.pole())
    print("Obwód prostakąta o bokach: ", prostokat.a, " i ", prostokat.b, "wynosi: ", prostokat.obwod())

### Przykład 2. ###
class ProstokatExtra(Prostokat):
    def __init__(self, x, y):
        super().__init__(x, y)

    def wyswietlPole(self):
        print("Pole prostakąta o bokach: ", self.a, " i ", self.b, "wynosi: ", self.pole())

def Zad_3():
    prostokat = ProstokatExtra(3, 5)
    prostokat.wyswietlPole()

### Przykład 3. ###
class Prostokad_3:
    a = 0
    b = 0

    def pole(self):
        return self.a * self.b

def Zad_4():
    prostokat = Prostokad_3()
    prostokat.a = int(input("Podaj a: "))
    prostokat.b = int(input("Podaj b: "))

    print("Pole prostokąta wynosi:", prostokat.pole())

class Osoba:
    imie = ""
    nazwisko = ""
    wzrost = 0
    waga = 0

    def __init__(self, imie, nazwisko, wzrost, waga):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wzrost = wzrost
        self.waga = waga

    def powitanie(self):
        print(f"Witaj {self.imie} {self.nazwisko}!\n")

    def informacje(self):
        print(f"Imię i nazwisko: {self.imie} {self.nazwisko}")
        print(f"Wzrost: {self.wzrost}")
        print(f"Waga: {self.waga}\n")

def Zad_5():
    osoba = Osoba("Liam", "Mairi", 185, 93)

    osoba.powitanie()
    osoba.informacje()

class Trojkat:
    a = 0
    b = 0
    c = 0
    wysokosc = 0

    def __init__(self, a, b, c, wysokosc):
        self.a = a
        self.b = b
        self.c = c
        self.wysokosc = wysokosc

### Nie działa poprawnie!!! 
    def poleHerona(self):
        p = (self.a + self.b + self.c) / 2
        pole = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        print(f"Pole trójkąta: {pole}\n")
##
    
    def pole(self):
        pole = (self.a * self.wysokosc) / 2
        print(f"Pole trójkąta: {pole}\n")

    def obwod(self):
        obwod = self.a + self.b + self.c
        print(f"Obwód trójkąta: {obwod}\n")

def Zad_6():
    trojkat = Trojkat(20, 23, 21, 5) # 24

    trojkat.pole()
    trojkat.obwod()
