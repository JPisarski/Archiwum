from PIL import Image, ImageDraw, ImageFont, ImageColor, ImageChops
import numpy as np
from PIL import ImageOps
import matplotlib.pyplot as plt
from PIL import ImageFilter
from PIL import ImageStat as stat


wd = Image.open("WD3.jpg")
wd_cmyk = wd.convert("CMYK")
print("RGB: ", wd.getpixel((200, 100)))
print("CMYK: ", wd_cmyk.getpixel((200, 100)))