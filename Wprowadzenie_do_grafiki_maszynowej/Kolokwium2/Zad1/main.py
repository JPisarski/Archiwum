from PIL import Image, ImageDraw, ImageFont, ImageColor, ImageChops
import numpy as np
from PIL import ImageOps
import matplotlib.pyplot as plt
from PIL import ImageFilter
from PIL import ImageStat as stat


w = 200
h = 400

obraz = Image.new("RGB", (200, 400), "lavender")


rys = ImageDraw.Draw(obraz)
rys.arc((0, 0, w, w), start=270, end=90, fill=(0, 0, 200), width=4)
rys.pieslice(((0, 0), (w, w)), start=90, end=270, fill="#ddddaa")
rys.polygon(((int(w/2), int(h/2)), (w, int(3*h/4)), (int(w/2), h), (0, int(3*h/4))), fill="#00ffaa")
del rys

obraz.show()
obraz.save('obraz1.png')