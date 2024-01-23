import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# rozumiem te polecenie, że obraz ma mieć wymiary h, w (czyli tablica obrazu wymiary w, h)


def szary(w, h):
    tab = np.ones((w, h), dtype=np.uint8)
    for i in range(w):
        for j in range(h):
            tab[i, j] = (i + 3 * j) % 256
    return tab


obraz = Image.open("obraz9.jpg")
w, h= obraz.size
obraz_szary = Image.fromarray(szary(h, w))
obraz_szary.show()

r, g, b = obraz.split()
obraz1 = Image.merge("RGB", (r, obraz_szary, b))
obraz1.save("mix.png")
obraz1.show()
