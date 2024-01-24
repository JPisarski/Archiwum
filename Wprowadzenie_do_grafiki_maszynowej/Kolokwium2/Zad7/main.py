from PIL import Image, ImageDraw, ImageFont, ImageColor, ImageChops
import numpy as np
from PIL import ImageOps
import matplotlib.pyplot as plt
from PIL import ImageFilter
from PIL import ImageStat as stat


obraz = Image.open("WD2.jpg")
w, h = obraz.size

nowy = Image.new("L", (w, h), 0)

rys = ImageDraw.Draw(nowy)
rys.polygon(((0, int(h/2)), (int(w/2), 0), (w, int(h/2)), (0, h)), fill=255)
del rys

r, g, b = obraz.split()
obraz1 = Image.merge("RGBA", (r, g, b, nowy))
obraz1.show()
obraz1.save("obraz1.png")

