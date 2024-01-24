from PIL import Image, ImageDraw, ImageFont, ImageColor, ImageChops
import numpy as np
from PIL import ImageOps
import matplotlib.pyplot as plt
from PIL import ImageFilter
from PIL import ImageStat as stat


def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def rgb_to_hex(red, green, blue):
    return '#%02x%02x%02x' % (red, green, blue)


kolory_text = open('kolory.txt', 'w')
for n, hex in ImageColor.colormap.items():
    if len(hex) == 3:
        hex = rgb_to_hex(hex[0], hex[1], hex[2])
    kolory_text.write(str(n) + ' ' + str(hex) + ' ' + str(hex_to_rgb(hex)))
    kolory_text.write('\n')

kolory_text.close()

# w pliku kolory.txt szukamy odpowiedzi
