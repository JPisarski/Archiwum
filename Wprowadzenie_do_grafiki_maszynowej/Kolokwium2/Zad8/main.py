from PIL import Image, ImageDraw, ImageFont, ImageColor, ImageChops
import numpy as np
from PIL import ImageOps
import matplotlib.pyplot as plt
from PIL import ImageFilter
from PIL import ImageStat as stat


im = Image.open("steve.png").convert("RGBA")

w, h = im.size

txt = Image.new('RGBA', im.size, (0, 0, 0, 0))
fnt = ImageFont.truetype("STIXGeneralBol.ttf", 20)
d = ImageDraw.Draw(im)
kolor = im.getpixel((240, 140))
x = kolor[0]
y = kolor[1]
z = kolor[2]
tekst = "Jakub\nPisarski"
d.text((w-70, h-50), tekst, font=fnt, fill=(x, y, z, 100), align="right")

im.show()
im.save("imie_na_obrazku.png")

