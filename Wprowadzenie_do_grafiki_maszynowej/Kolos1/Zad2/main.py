import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# w podanych plikach nie było obrazka maska3.jpg tylko maska3.jpg

obraz = Image.open("obraz1.jpg")
maska = Image.open("maska3.png")

obraz1 = obraz.copy()
w, h = obraz.size
wm, hm = maska.size
m = w - wm
n = 0

for i in range(wm):
    for j in range(hm):
        if i + m < w and j + n < h:
            if maska.getpixel((i, j)) == 0:
                kolor = obraz.getpixel((i + m, j + n))
                obraz1.putpixel((i + m, j + n), (kolor[0] + 160, kolor[1] + 180, kolor[2] - 180))

obraz = obraz1.copy()
obraz.save("obraz_z_maską.png")
obraz.show()


