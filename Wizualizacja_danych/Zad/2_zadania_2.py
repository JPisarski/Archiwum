#
# #zadanie 1
#
# sporty = ["piłka nożna", "kolarstwo", "siatkówka"]
# sporty.reverse()
# sporty.append("koszykówka")
# sporty.append("tenis")
# print(sporty)
#
# #zadanie 2
#
# skróty = {"tłum.": "tłumaczenie", "przyp.": "przypis","red": "redaktor" }
#
# print(skróty)
#
# #zadanie 3
#
# gry = {1: "Icy Tower", 2: "Pasjans", 3: "World of Tanks"}
#
# print(len(gry))
#
# #zadanie 4
#
# zdanie = input()
#
# print(zdanie.count("a"))
#
# #zadanie 5
#
# import sys
#
# a = int(sys.stdin.readline())
# b = int(sys.stdin.readline())
# c = int(sys.stdin.readline())
#
# wynik =str(a**b + c)
#
# sys.stdout.write(wynik)
#
# #zadanie 6
#
# a = int(input())
# b = int(input())
# c = int(input())
#
#
# if a == b:
#     if a == c:
#         print("Wszystkie liczby są równe")
#     elif a < c:
#         print("Liczba nr 3, czyli %d jest największa" % c)
#     else:
#         print("Liczby nr 1 i nr 2, czyli %d i %d są równe i największe" % (a, b))
# elif b == c:
#     if a == c:
#         print("Wszystkie liczby są równe")
#     elif b < a:
#         print("Liczba nr 1, czyli %d jest największa" % a)
#     else:
#         print("Liczby nr 2 i nr 3, czyli %d i %d są równe i największe" % (b, c))
# elif a == c:
#     if a == b:
#         print("Wszystkie liczby są równe")
#     elif a < b:
#         print("Liczba nr 2, czyli %d jest największa" % b)
#     else:
#         print("Liczby nr 1 i nr 3, czyli %d i %d są równe i największe" % (a, c))
# elif a > b:
#     if a > c:
#         print("Liczba nr 1, czyli %d jest największa" % a)
#     else:
#         print("Liczba nr 3, czyli %d jest największa" % c)
# elif b > a:
#     if b > c:
#         print("Liczba nr 2, czyli %d jest największa" % b)
#     else:
#         print("Liczba nr 3, czyli %d jest największa" % c)
#
# #zadanie 7
#
# liczby = [7, 6.0, 8, 9.5, 10]
#
# licznik = 0
# for x in liczby:
#     liczby[licznik] = x**2
#     licznik += 1
#
# print(liczby)
#
# #zadanie 8
#
# parzyste = []
# x = 0
# while x < 10:
#     z = float(input())
#     if z % 2 == 0:
#         parzyste.append(z)
#     x += 1
#
# print(parzyste)
#
# #zadanie 9
#
# import math
#
#
# try:
#     x = float(input())
#     y = math.sqrt(x)
#     print(y)
# except ValueError:
#     print("Liczba ujemna - błąd")
#
#
#
