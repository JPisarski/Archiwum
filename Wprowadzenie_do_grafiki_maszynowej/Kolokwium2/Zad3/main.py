from PIL import Image, ImageDraw, ImageFont, ImageColor, ImageChops
import numpy as np
from PIL import ImageOps
import matplotlib.pyplot as plt
from PIL import ImageFilter
from PIL import ImageStat as stat

im = Image.open("WD1.jpg")
im_f = Image.open('wd_filtr1.png')


def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe


im1 = im.filter(ImageFilter.BLUR)
im2 = im.filter(ImageFilter.Kernel(size=(5, 5), scale=100, offset=0, kernel=(1, 1, 1, 1, 1, 1, 5, 5, 5, 1, 1, 5, 44, 5, 1, 1, 5, 5, 5, 1, 1, 1, 1, 1, 1)))

# pasuje im3
im3 = im.filter(ImageFilter.Kernel(size=(3, 3), scale=13, offset=0, kernel=(1, 1, 1, 1, 5, 1, 1, 1, 1)))

im4 = im.filter(ImageFilter.Kernel(size=(5, 5), scale=16, offset=0, kernel=(1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1)))
im5 = im.filter(ImageFilter.Kernel(size=(3, 3), scale=6, offset=0, kernel=(0, -1, 0, -1, 10, -1, 0, -1, 0)))

# pasuje im6
im6 = im.filter(ImageFilter.SMOOTH)

im7 = im.filter(ImageFilter.DETAIL)
im8 = im.filter(ImageFilter.SMOOTH_MORE)

# trzeba 8 razy odpalić kod, podmieniając obrazek (obecnie jest sprawdzany obrazek im6)
roznica = ImageChops.difference(im_f, im6)

# sprawdzamy wizualnie, czy się różnią (metoda niedokładna)
# roznica.show()

# sprawdzamy po statystykach, czy się różnią (metoda dokładna)
statystyki(roznica)


# odp: im3 i im6 pasują
