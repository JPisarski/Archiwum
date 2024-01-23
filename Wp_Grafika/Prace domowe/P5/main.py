from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt


# zadanie 1

diff = Image.open("diff.png")


# Po powiększeniu obrazu widać, że nie jest to idealnie czarny obraz

# a

def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe


statystyki(diff)

# Statystyki wskazują na to, że obraz nie jest idealnie czarny
# (średnia, mediana, odchylenie standardowe oraz maxima różne od 0)

# b

hist = diff.histogram()
plt.title("histogram")
plt.bar(range(256), hist[:256], color='r', alpha=0.5)
plt.bar(range(256), hist[256:2 * 256], color='g', alpha=0.4)
plt.bar(range(256), hist[2 * 256:], color='b', alpha=0.3)
plt.savefig("histogram1.png")
plt.show()

# c

def zlicz_roznice_srednia_RGB(obraz, wsp):
    t_obraz = np.asarray(obraz)
    h, w, d = t_obraz.shape
    zlicz = 0
    for i in range(h):
        for j in range(w):
            if np.mean(t_obraz[i, j, :]) > wsp:
                zlicz = zlicz + 1
    procent = zlicz / (h * w)
    return zlicz, procent


wsp = 10
print("Dla wsp = 10")
zlicz, procent = zlicz_roznice_srednia_RGB(diff, wsp)
print('liczba niepasujących pikseli = ', zlicz)
print('procent niepasujących pikseli = ', procent)
wsp = 5
print("Dla wsp = 5")
zlicz, procent = zlicz_roznice_srednia_RGB(diff, wsp)
print('liczba niepasujących pikseli = ', zlicz)
print('procent niepasujących pikseli = ', procent)
wsp = 1
print("Dla wsp = 1")
zlicz, procent = zlicz_roznice_srednia_RGB(diff, wsp)
print('liczba niepasujących pikseli = ', zlicz)
print('procent niepasujących pikseli = ', procent)


# im mniejszy współczynnik wsp, tym większa liczba niepasujących pikseli (większy procent niepasujących pikseli)
# z danych wyników widać, że to nie jest obraz idealnie czarny

# d

def zlicz_roznice_suma_RGB(obraz, wsp):
    t_obraz = np.array(obraz)
    h, w, d = t_obraz.shape
    zlicz = 0
    for i in range(h):
        for j in range(w):
            if sum(t_obraz[i, j, :]) > wsp:
                zlicz = zlicz + 1
    procent = zlicz / (h * w)
    return zlicz, procent


wsp = 70
print("Dla wsp = 70")
zlicz1, procent1 = zlicz_roznice_suma_RGB(diff, wsp)
print('liczba niepasujących pikseli = ', zlicz1)
print('procent niepasujących pikseli = ', procent1)
wsp = 50
print("Dla wsp = 50")
zlicz1, procent1 = zlicz_roznice_suma_RGB(diff, wsp)
print('liczba niepasujących pikseli = ', zlicz1)
print('procent niepasujących pikseli = ', procent1)
zlicz1, procent1 = zlicz_roznice_suma_RGB(diff, wsp)
wsp = 25
print("Dla wsp = 25")
print('liczba niepasujących pikseli = ', zlicz1)
print('procent niepasujących pikseli = ', procent1)

# im mniejszy współczynnik wsp, tym większa liczba niepasujących pikseli (większy procent niepasujących pikseli)
# z danych wyników widać, że to nie jest obraz idealnie czarny


# zadanie 2

# a

obraz = Image.open("obraz.jpg")
obraz.save("obraz1.jpg")

# b

obraz1 = Image.open("obraz1.jpg")
obraz1.save("obraz2.jpg")
obraz2 = Image.open("obraz2.jpg")
obraz2.save("obraz3.jpg")
obraz3 = Image.open("obraz3.jpg")
obraz3.save("obraz4.jpg")
obraz4 = Image.open("obraz4.jpg")
obraz4.save("obraz5.jpg")
obraz5 = Image.open("obraz5.jpg")

# c Widać dobrze różnicę, jeśli powiększy się ostatni obraz (porównanie1)

porownanie1 = ImageChops.difference(obraz, obraz5)
plt.figure(figsize=(32, 16))
plt.subplot(1, 3, 1)
plt.imshow(obraz)
plt.axis("off")
plt.subplot(1, 3, 2)
plt.imshow(obraz5)
plt.axis("off")
plt.subplot(1, 3, 3)
plt.imshow(porownanie1)
plt.axis("off")
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig("figura1.png")
plt.show()
statystyki(porownanie1)

# d Gołym okiem nie widać, ale istnieje różnica między obrazami.

porownanie2 = ImageChops.difference(obraz4, obraz5)
plt.figure(figsize=(32, 16))
plt.subplot(1, 3, 1, )
plt.imshow(obraz4)
plt.axis("off")
plt.subplot(1, 3, 2)
plt.imshow(obraz5)
plt.axis("off")
plt.subplot(1, 3, 3)
plt.imshow(porownanie2)
plt.axis("off")
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig("figura2.png")
plt.show()
statystyki(porownanie2)

# e Przy każdym kolejnym zapisywaniu obrazu, powiększa się różnica między oryginałem, a nowozapisanym obrazem.


# zadanie 3

# a

def odkoduj(obraz1, obraz2):
    porownanie = ImageChops.difference(obraz1, obraz2)
    tab = np.array(porownanie)
    h, w, d = tab.shape
    for i in range(h):
        for j in range(w):
            if tab[i][j][0] > 0 or tab[i][j][1] > 0 or tab[i][j][2] > 0:
                tab[i][j][0] = 255
                tab[i][j][1] = 255
                tab[i][j][2] = 255
    return Image.fromarray(tab).convert("L")


jesien = Image.open("jesien.jpg")
zakodowany1 = Image.open("zakodowany1.bmp")
odkodowane1 = odkoduj(jesien, zakodowany1)
odkodowane1.show()

#b

zakodowany2 = Image.open("zakodowany2.bmp")
odkodowane2 = odkoduj(jesien, zakodowany2)
odkodowane2.save("kod2.bmp")
odkodowane2.show()

