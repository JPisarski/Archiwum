from PIL import Image, ImageDraw, ImageFont, ImageColor, ImageChops
import numpy as np
from PIL import ImageOps
import matplotlib.pyplot as plt
from PIL import ImageFilter
from PIL import ImageStat as stat


def statystyki(im):
    s = stat.Stat(im)
    print("średnia: ", s.mean)  # srednia
    print("mediana: ", s.median)  # mediana



im = Image.open("WD1.jpg")
imc = im.convert("CMYK")
c, m, y, k = imc.split()

statystyki(m)
hist = m.histogram()

suma = 0
for i in range (0, 131):
    suma += hist[i]

print("Liczba pikseli o wartości 130:", hist[130])
print("Liczba pikseli o wartości <= 130:", suma)

