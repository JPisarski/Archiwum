from PIL import Image, ImageDraw, ImageFont, ImageColor, ImageChops
import numpy as np
from PIL import ImageOps
import matplotlib.pyplot as plt
from PIL import ImageFilter
from PIL import ImageStat as stat

im = Image.open("choinka2.jpg")

w, h = im.size
print(im.size)

im1 = im.resize((int(w/2), int(h/2)), 3)
print(im1.size)

im2 = im1.rotate(120, expand=1, fillcolor=(0, 255, 255))
im2.show()
