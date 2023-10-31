# zadanie_1


def polacz(litera, nazwisko):
    return litera+"."+nazwisko


print(polacz("J", "Pisarski"))

# zadanie_2


def polacz_wersja_druga(imie, nazwisko):
    return imie[0].upper()+"."+nazwisko[0].upper()+nazwisko[1:]


print(polacz_wersja_druga("jakub", "pisarski"))

# zadanie_3


def rok(pierwsze, ostatnie, wiek):
    return int(str(pierwsze)+str(ostatnie))-wiek


print(rok(20, 22, 20))

# zadanie_4


def polacz_wersja_trzecia(imie, nazwisko, funkcja):
    if funkcja=="funkcja_z_zadania_drugiego":
        return imie[0].upper()+"."+nazwisko[0].upper()+nazwisko[1:]
    elif funkcja=="funkcja_z_zadania_pierwszego":
        return imie[0]+ "." + nazwisko


print(polacz_wersja_trzecia("jakub", "pisarski", "funkcja_z_zadania_drugiego"))
print(polacz_wersja_trzecia("jakub", "pisarski", "funkcja_z_zadania_pierwszego"))

# zadanie_5


def dzielenie_liczb_dodatnich(p, d):
    if p>0 and d>0  and d!=0:
         return p/d


print(dzielenie_liczb_dodatnich(25, 5))

# zadanie_6

suma = 0
while suma<100:
    x = int(input("Podaj liczbę "))
    suma += x
print("Suma podanych liczb przekroczyła 100")

# zadanie_7


def krotka(a):
    return tuple(a)


print(krotka([1, 2, 3, 4, 5]))

# zadanie_8

a = []
b = "TAK"
x = int(input("Ile liczb chcesz dodać?: "))
for m in range(x):
    c = int(input("Podaj liczbę: "))
    a.append(c)
d = tuple(a)
print(d)

# zadanie_9


def dzien(x):
    t = ["poniedziałek", "wtorek", "środa", "czwartek", "piątek", "sobota", "niedziela"]
    return t[x-1]

print(dzien(7))

# zadanie_10


def palindrom(tekst):
    odwrotny = tekst[::-1]
    if tekst == odwrotny:
        return True
    else:
        return False


print(palindrom("MAM"))
