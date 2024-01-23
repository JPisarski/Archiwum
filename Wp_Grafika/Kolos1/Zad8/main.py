from PIL import Image


def kwadrat_srednia(obraz, m, n, k):  # m,n - srodek kwadratu, k - długość boku kwadratu, liczba nieparzysta
    d = int(k / 2)
    suma = []
    ile = 0
    ilepikseli = 0
    for z in range(3):
        for a in range(k):
            for b in range(k):
                x = m + a - d
                y = n + b - d
                ilepikseli += 1
                ile += obraz.getpixel((x, y))[z]
        suma.append(ile / ilepikseli)
        ile = 0
        ilepikseli = 0
    return suma


obraz = Image.open("obraz9.jpg")
print(kwadrat_srednia(obraz, 60, 170, 5))
