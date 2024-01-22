from PIL import Image
import numpy as np


# zadanie 1

def fun1(w, h, grub, kolor):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    ile = 0
    m = min(w, h)
    dokad = int(m / (2 * grub))
    for i in range(0, dokad):
        tab[ile * grub: h - (ile * grub), ile * grub: w - (ile * grub)] = kolor % 256
        ile += 1
        kolor += 25
    return Image.fromarray(tab)


obrazek1 = fun1(200, 200, 10, 10)
obrazek1.save("obraz1_1.jpg")
obrazek1.save("obraz1_1.png")


def fun2(w, h, grub, kolor):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(w / grub)
    for k in range(ile):
        for g in range(grub):
            i = k * grub + g
            for j in range(h):
                tab[j, i] = kolor % 256
        kolor += 25
    return Image.fromarray(tab)


obrazek2 = fun2(200, 200, 10, 10)
obrazek2.save("obraz1_2.jpg")
obrazek2.save("obraz1_2.png")


def negatyw_szary(obraz):
    tab = np.asarray(obraz)
    h, w = tab.shape
    tab_neg = tab.copy()
    for i in range(h):
        for j in range(w):
            tab_neg[i, j] = 255 - tab[i, j]
    return Image.fromarray(tab_neg)


obrazek1_n = negatyw_szary(obrazek1)
obrazek1_n.save("obraz1_1N.jpg")
obrazek1_n.save("obraz1_1N.png")

obrazek2_n = negatyw_szary(obrazek2)
obrazek2_n.save("obraz1_2N.jpg")
obrazek2_n.save("obraz1_2N.png")


# zadanie 2

def fun1_kolor(w, h, grub, kolor):
    t = (h, w, 3)
    tab = np.zeros(t, dtype=np.uint8)
    ile = 0
    m = min(w, h)
    dokad = int(m / (2 * grub))
    r = kolor[0]
    g = kolor[1]
    b = kolor[2]
    for i in range(0, dokad):
        tab[ile * grub: h - (ile * grub), ile * grub: w - (ile * grub)] = [r, g, b]
        ile += 1
        r = (r + 25) % 256
        g = (g + 30) % 256
        b = (b + 35) % 256
    return Image.fromarray(tab)


obrazek1_kolor = fun1_kolor(100, 100, 5, [100, 200, 0])
obrazek1_kolor.save("obraz2.jpg")
obrazek1_kolor.save("obraz2.png")

def fun2_kolor(w, h, grub, kolor):
    t = (h, w, 3)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(w / grub)
    r = kolor[0]
    gr = kolor[1]
    b = kolor[2]
    for k in range(ile):
        for g in range(grub):
            i = k * grub + g
            for j in range(h):
                tab[j, i] = [r, gr, b]
        r = (r + 25) % 256
        gr = (gr + 30) % 256
        b = (b + 35) % 256
    return Image.fromarray(tab)


obrazek2_kolor = fun2_kolor(100, 100, 5, [250, 100, 10])
obrazek2_kolor.save("obraz22.jpg")
obrazek2_kolor.save("obraz22.png")


def negatyw_kolor(obraz):
    tab = np.asarray(obraz)
    h, w, z = tab.shape
    tab_neg = tab.copy()
    for i in range(h):
        for j in range(w):
            tab_neg[i, j, 0] = 255 - tab[i, j, 0]
            tab_neg[i, j, 1] = 255 - tab[i, j, 1]
            tab_neg[i, j, 2] = 255 - tab[i, j, 2]
    return Image.fromarray(tab_neg)


obrazek1_kolor_n = negatyw_kolor(obrazek1_kolor)
obrazek1_kolor_n.save("obraz2N.jpg")
obrazek1_kolor_n.save("obraz2N.png")
obrazek2_kolor_n = negatyw_kolor(obrazek2_kolor)
obrazek2_kolor_n.save("obraz2N2.jpg")
obrazek2_kolor_n.save("obraz2N2.png")

# zadanie 3

def fun3(tablica, grub):
    h, w = tablica.shape
    t = (h, w, 3)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(h/grub)
    r = 200
    g = 0
    b = 10
    for k in range(ile):
        for m in range(grub):
            i = k * grub + m
            for j in range(w):
                if tablica[i, j] == False:
                    tab[i, j] = [r, g, b]
                else:
                    tab[i, j] = [255, 255, 255]
        r = (r + 50) % 256
        g = (g + 2) % 256
        b = (b + 15) % 256
    return tab


obrazek3 = Image.open("inicjaly.bmp")
tab3 = fun3(np.asarray(obrazek3), 5)
obraz3 = Image.fromarray(tab3)
obraz3.save("obraz3.jpg")
obraz3.save("obraz3.png")

# obrazy obraz3.jpg i obraz3.png nie są identyczne. Przyczyną jest to, że Format obrazu PNG  przy zapisie wykonuje
# bezstratną kompresję, co oznacza, że będzie cięższym plikiem w porównaniu do identycznego JPG, ale będzie też
# wyglądał lepiej od niego. Ma 48-bitową głębię kolorów oraz kanał alfa – czyli, mówiąc
# ludzkim głosem – obsługuje przezroczystość. Natomiast Format obrazu JPEG znany też jako JPG
# to też nazwa algorytmu kompresującego plik przy zapisie – dzięki
# czemu obraz jest lekki i szybko się wczytuje. Oszczędność na wadze pliku odbija się jednak niekorzystnie na
# jakości, no i jotpegi nie obsługują przezroczystości.


# zadanie 4

lista = np.ones((2, 2), dtype=np.uint8)
lista[0][0] = 328
print(lista[0][0])
lista[0][1] = -1
print(lista[0][1])
lista[1][0] = -24
print(lista[1][0])
lista[1][1] = -257
print(lista[1][1])

# typ uint8 w przypadku, gdy podana wartość koloru przekracza 255, to zmienia się w resztę z dzielenia przez 256
# x > 255 , to x = x % 256
# typ uint8 w przypadku, gdy podana wartość koloru jest ujemna, to zmienia się w 256+x i tak w kółko, aż liczba
# będzie nieujemna x < 0, to x = 256+x tak długo, aż x będzie nieujemny

# zadanie 5

# Widać różnice między obrazami zapisanymi w formatach jpg i png, zwłaszcza po powiększeniu obrazu. Obraz w formacie png
# wygląda lepiej od tego samego obrazu zapisanego w formacie jpg. Przyczyny są takie jakie napisałem w zadaniu 3:
# Format PNG przy zapisie wykonuje bezstratną kompresję. Natomiast Format obrazu JPEG znany też jako JPG
# to też nazwa algorytmu kompresującego plik przy zapisie – dzięki
# czemu obraz jest lekki i szybko się wczytuje. Oszczędność na wadze pliku odbija się jednak niekorzystnie na
# jakości, no i jotpegi nie obsługują przezroczystości.
