#
# #zadanie 1
#
# lista_A = [1-x for x in range(1, 11)]
# print(lista_A)
#
# lista_B = [4**x for x in range(0, 8)]
# print(lista_B)
#
# lista_C = [x for x in lista_B if x % 2 == 0]
# print(lista_C)
#
# #zadanie 2
#
# import random
#
# lista_1 = []
# while len(lista_1) < 10:
#     lista_1.append(random.randint(0, 100))
#
# print(lista_1)
#
# lista_2 = [x for x in lista_1 if x % 2 == 0]
# print(lista_2)
#
# # zadanie 3
#
# produkty = {"jaja": "sztuki", "cukier": "kg", "chleb": "bochenek", "keczup": "słoik"}
#
#
# lista_nowa = [x for x in produkty.keys() if produkty[x] == "sztuki"]
# print(lista_nowa)
#
# # #zadanie 4
#
# def prostokątny(a, b, c):
#     if (a**2 + b**2 == c**2) or  (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
#         print("Jest prostokątny.")
#     else:
#         print("Nie jest prostokątny.")
#
#
# a = int(input("Podaj 1 bok:"))
# b = int(input("Podaj 2 bok:"))
# c = int(input("Podaj 3 bok:"))
#
# prostokątny(a, b, c)
#
# #zadanie 5
#
# def pole_trapezu(a=1, b=1, h=1):
#     return (a+b)*h/2
#
#
# print(pole_trapezu())
# print(pole_trapezu(20, 20, 5))
#
# #zadanie 6
#
# def iloczyn(a=1, b=4, ile=10):
#     if a == 0:
#         return 0
#     else:
#         ciag = []
#         for x in range(ile):
#             ciag.append(a*(b**x))
#         print(ciag)
#         iloczyn = 1
#         for x in ciag:
#             iloczyn *=x
#     return iloczyn
#
#
# print(iloczyn(1, 2, 5))
# print(iloczyn(10, 1, 10))
#
# #zadanie 7
#
# def iloczyn_2(*ciag):
#     if len(ciag) == 0:
#         return 0
#     else:
#         iloczyn = 1
#         for x in ciag:
#             iloczyn *= x
#     return iloczyn
#
#
# print(iloczyn_2(1, 2, 3, 4, 5, 6))
# print(iloczyn_2())
# print(iloczyn_2(10, 10))
#
# #zadanie 8
#
# def zakupy(** pl):
#     print("Wszystkich produktów jest", len(pl.keys()))
#     return sum(pl.values())
#
#
# print(zakupy(jaja=50, bułka=55, mleko=20))
#
# #zadanie 9
#
# from ciągi import *
#
# print(ciągi_arytmetyczne.n_wyraz(1, 1, 100))
# print(ciągi_geometryczne.n_wyraz(1, 5, 4))
#

