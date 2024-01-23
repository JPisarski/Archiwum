from PIL import Image
import numpy as np
from PIL import ImageChops, ImageOps
from PIL import ImageStat as stat
import matplotlib.pyplot as plt

# zadanie 1

obraz = Image.open("zeby.png")
print(obraz.mode)
obraz = obraz.convert("L")
print(obraz.mode)


# zadanie 2
# 2.1


def histogram_norm(obraz):
    hist = obraz.histogram()
    w, h = obraz.size
    N = w * h
    hist_norm = []
    for i in hist:
        hist_norm.append(i / N)
    return hist_norm


# 2.2

def histogram_cumul(obraz):
    hist_norm = histogram_norm(obraz)
    hist_cumulative = [hist_norm[0]]
    for i in range(1, len(hist_norm)):
        hist_cumulative.append(hist_cumulative[i - 1] + hist_norm[i])
    return hist_cumulative


# 2.3

def histogram_equalization(obraz):
    hist_cumulative = histogram_cumul(obraz)
    obraz1 = obraz.point(lambda i: int(255 * hist_cumulative[i]))
    return obraz1


obraz_wyrownany = histogram_equalization(obraz)
obraz_wyrownany.save("equalized.png")

# 2.4


plt.figure(figsize=(32, 16))
plt.subplot(2, 2, 1)
plt.title("Histogram")
plt.plot(obraz.histogram())
plt.subplot(2, 2, 2)
plt.title("Histogram znormalizowany")
plt.plot(histogram_norm(obraz))
plt.subplot(2, 2, 3)
plt.title("Histogram skumulowany")
plt.plot(histogram_cumul(obraz))
plt.subplot(2, 2, 4)
plt.title("Histogram po wyrównaniu")
plt.plot(obraz_wyrownany.histogram())
plt.subplots_adjust(wspace=0.5, hspace=0.5)
plt.savefig("fig1.png")

# 2.5

def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe


statystyki(obraz)
print()
statystyki(obraz_wyrownany)
print()

# obraz po wyrównaniu histogramu ma mniejszą średnią, medianę oraz odchylenie standardowe
# zmieniła się też minimalna wartość pikseli na 0
# można z tego wywnioskować, że obraz stał się trochę ciemniejszy

# zadanie 3

obraz_wyrownany1 = ImageOps.equalize(obraz)
obraz_wyrownany1.save("equalized1.png")

# 3.1

plt.figure(figsize=(32, 16))
plt.subplot(1, 3, 1)
plt.title("Obraz wejściowy")
plt.imshow(obraz, "gray")
plt.axis("off")
plt.subplot(1, 3, 2)
plt.title("Obraz z punktu 2")
plt.imshow(obraz_wyrownany, "gray")
plt.axis("off")
plt.subplot(1, 3, 3)
plt.title("Obraz z punktu 3")
plt.imshow(obraz_wyrownany1, "gray")
plt.axis("off")
plt.subplots_adjust(wspace=0.5, hspace=0.5)
plt.savefig("fig2.png")

# 3.2

statystyki(obraz_wyrownany)
print()
statystyki(ImageChops.difference(obraz_wyrownany, obraz_wyrownany1))

# wartość obrazu obraz_wyrownany1 ma mniejszą średnią, medianę oraz większe odchylenie standardowe
# w punkcie 2, jeśli wartość piksela była ułamkiem, to stosowano fukcję int() - np. 9.9 -> 9
# natomiast w punkcie 3, jeśli wartość piksela była ułamkiem, to stosowano inną funkcję.


# zadanie 4

def konwertuj1(obraz, w_r, w_g, w_b):
    w, h = obraz.size
    tab = np.array(obraz)
    tab1 = np.zeros((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            tab1[i, j] = round(tab[i, j, 0] * w_r + tab[i, j, 1] * w_g + tab[i, j, 2] * w_b)
    return Image.fromarray(tab1)


# 4.1

mgla = Image.open("mgla.jpg")
mgla_szary = konwertuj1(mgla, 0.299, 0.587, 0.114)
mgla_szary.save("mgla_L1.png")
mgla_l = mgla.convert("L")
mgla_l.save("mgla_L.png")
print(mgla.mode)
print(mgla_szary.mode)
print(mgla_l.mode)
print()

# 4.2

statystyki(mgla_szary)
print()
statystyki(mgla_l)
print()

# Statystyki się nieznacznie różnią

# 4.3


def konwertuj2(obraz, w_r, w_g, w_b):
    w, h = obraz.size
    tab = np.array(obraz)
    tab1 = np.zeros((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            tab1[i, j] = int(tab[i, j, 0] * w_r + tab[i, j, 1] * w_g + tab[i, j, 2] * w_b)
    return Image.fromarray(tab1)


mgla_szary1 = konwertuj2(mgla, 0.299, 0.587, 0.114)
mgla_szary1.save("mgla_L2.png")
print(mgla_szary1.mode)
print()
statystyki(mgla_szary1)
statystyki(mgla_l)

# Różnice są większe. Minimalna wartość pikseli wzrosła na 1. Średnia oraz odchylenie standardowe zmalało.