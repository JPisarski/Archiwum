#
# #zadanie 1
#
# import random
#
# liczby = [random.randint(0, 30) for x in range(10)]
# liczby_razy_2 = [x*2 for x in liczby]
#
# plik = open("cyferki.txt", "w+")
# plik.writelines((str(liczby_razy_2)))
# plik.close()
#
# #zadanie 2
#
# plik = open("cyferki.txt", "r")
# dane = plik.readlines()
# plik.close()
# print(dane)
#
# #zadanie 3
#
# tekst = ["""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum
# has been the industry's standard dummy text ever since the 1500s, when an unknown printer
# took a galley of type and scrambled it to make a type specimen book."""]
#
# with open("przykład.txt", "w+") as plik:
#     plik.writelines(tekst)
#
# with open("przykład.txt", "r+") as plik:
#     for x in plik:
#         print(x, end="")
#
# #zadanie 4
#
# class NaZakupy:
#     def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
#         self.nazwa_produktu = nazwa_produktu
#         self.ilosc = ilosc
#         self.jednostka_miary = jednostka_miary
#         self.cena_jed = cena_jed
#
#     def wyswietl_produkt(self):
#         print("Nazwa: "+ self.nazwa_produktu)
#         print("Ilość: " + str(self.ilosc) + " " + self.jednostka_miary)
#         print("Cena za 1 " + self.jednostka_miary + ": " + str(self.cena_jed) + " zł")
#
#     def ile_produktu(self):
#         print(str(self.ilosc) +" "+ self.jednostka_miary)
#
#     def ile_kosztuje(self, ile):
#         return self.cena_jed*ile
#
#
# Ziemniaki = NaZakupy("ziemniaki", 10, "kg", 2)
# Ziemniaki.wyswietl_produkt()
# Ziemniaki.ile_produktu()
# print(Ziemniaki.ile_kosztuje(10))
#
# #zadanie 5
#
# class CiagiArytmetyczne:
#
#     def __init__(self, wyraz_1, r, ilosc):
#         self.wyraz_1 = wyraz_1
#         self.r = r
#         self.ilosc = ilosc
#         self.c = [self.wyraz_1+self.r*(x-1) for x in range(1, self.ilosc+1)]
#
#     def wyswietl_dane(self):
#         print(self.c)
#
#     def pobierz_elementy(self, *c):
#         self.c = [x for x in c]
#
#     def pobierz_parametry(self, wyraz_1, r, ilosc):
#         self.wyraz_1 = wyraz_1
#         self.r = r
#         self.ilosc = ilosc
#         self.c = [self.wyraz_1 + self.r * (x - 1) for x in range(1, self.ilosc + 1)]
#
#     def policz_sume(self):
#         return sum(self.c)
#
#     def policz_elementy(self):
#         return ((self.c[-1]-self.wyraz_1)/self.r)+1
#
#
# Ciag1 = CiagiArytmetyczne(1, 1, 5)
# Ciag1.wyswietl_dane()
# Ciag1.pobierz_elementy(6, 8, 10)
# Ciag1.wyswietl_dane()
# Ciag1.pobierz_parametry(10, 10, 5)
# Ciag1.wyswietl_dane()
# print(Ciag1.policz_sume())
# print(Ciag1.policz_elementy())

# #zadanie 6
#
# class Robaczek:
#     def __init__(self, x, y, krok):
#         self.x = x
#         self.y = y
#         self.krok = krok
#
#     def idź_w_górę(self, ile_kroków):
#         self.y = self.y + ile_kroków * self.krok
#
#     def idź_w_dół(self, ile_kroków):
#         self.y = self.y - ile_kroków * self.krok
#
#     def idź_w_lewo(self, ile_kroków):
#         self.x = self.x - ile_kroków * self.krok
#
#     def idź_w_prawo(self, ile_kroków):
#         self.x = self.x + ile_kroków * self.krok
#
#     def pokaż_gdzie_jesteś(self):
#         print("x: " + str(self.x))
#         print("y: " + str(self.y))
#
#
# Sprawdzam = Robaczek(0, 0, 10)
# Sprawdzam.idź_w_górę(6)
# Sprawdzam.idź_w_prawo(6)
# Sprawdzam.idź_w_lewo(1)
# Sprawdzam.idź_w_dół(1)
# Sprawdzam.pokaż_gdzie_jesteś()
#







