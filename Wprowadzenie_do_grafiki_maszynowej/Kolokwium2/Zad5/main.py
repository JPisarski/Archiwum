from PIL import Image, ImageDraw, ImageFont, ImageColor, ImageChops
import numpy as np
from PIL import ImageOps
import matplotlib.pyplot as plt
from PIL import ImageFilter
from PIL import ImageStat as stat

maska = Image.open("mmaska3.jpg")
maskal = maska.convert("L")
im = Image.open("WD3.jpg")
obraz = Image.open("obraz.png")

w, h = im.size

maskal = maskal.resize((w, h), 3)
obraz = obraz.resize((w, h), 3)

obraz.paste(im, (0, 0), maskal)
obraz.show()
obraz.save("obraz_z_maska.png")
