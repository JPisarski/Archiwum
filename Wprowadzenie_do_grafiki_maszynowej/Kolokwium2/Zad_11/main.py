from PIL import Image, ImageDraw, ImageFont, ImageColor, ImageChops
import numpy as np
from PIL import ImageOps
import matplotlib.pyplot as plt
from PIL import ImageFilter
from PIL import ImageStat as stat


def statystyki(im):
    s = stat.Stat(im)
    print("mediana: ", s.median)  # mediana


im = Image.open("WD1.jpg")
im1 = im.resize((500, 400), Image.LANCZOS)
print(im1.size)

srodek = (350, 110)
dlugosc_boku = 71
k = 71 // 2

tab = np.array(im1)
wycinek = Image.fromarray(tab[110-k:110+k, 350-k:350+k])
wycinek.show()
print(wycinek.size)

print(wycinek.size)

statystyki(wycinek)
