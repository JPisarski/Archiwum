import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

obraz = Image.open("obraz9.jpg")


def zmien_wartosci_pikseli(obraz):
    obraz1 = obraz.copy()
    w, h = obraz.size
    for i, j in [(i, j) for i in range(w) for j in range(h)]:
        p = obraz.getpixel((i, j))
        obraz1.putpixel((i, j), (p[0] + 100, p[1], int(p[2]*0.5)))
    return obraz1


obraz2 = zmien_wartosci_pikseli(obraz)
obraz2.save("obraz3.png")


# poniższa funkcja zmienia wartości pikseli tak, że rozjaśnia kanał R o 100, kanał G zostawia taki jaki był, a kanał B dzieli przez 2 i stosuje podłogę
