from PIL import Image, ImageDraw, ImageFont, ImageColor, ImageChops
import numpy as np
from PIL import ImageOps
import matplotlib.pyplot as plt
from PIL import ImageFilter
from PIL import ImageStat as stat

im = Image.open("broken-leg2.jpg")
sz = im.convert("L")
hist = sz.histogram()


def histogram_norm(obraz):
    hist = obraz.histogram()
    w, h = obraz.size
    N = w * h
    hist_norm = []
    for i in hist:
        hist_norm.append(i / N)
    return hist_norm


def histogram_cumul(obraz):
    hist_norm = histogram_norm(obraz)
    hist_cumulative = [hist_norm[0]]
    for i in range(1, len(hist_norm)):
        hist_cumulative.append(hist_cumulative[i - 1] + hist_norm[i])
    return hist_cumulative


plt.title("Histogram  skumulowany")
plt.plot(histogram_cumul(sz))
plt.show()
