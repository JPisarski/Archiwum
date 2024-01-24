from PIL import Image, ImageDraw, ImageFont, ImageColor, ImageChops
import numpy as np
from PIL import ImageOps
import matplotlib.pyplot as plt
from PIL import ImageFilter
from PIL import ImageStat as stat


im = Image.open("WD1.jpg")
fnt = ImageFont.truetype("DejaVuSans-BoldOblique.ttf", 14)
d = ImageDraw.Draw(im)
tekst = "idź wyprostowany wśród\ntych co na kolanach\nwśród odwróconych plecami\ni obalonych w proch"
d.text((0, 0), tekst, font=fnt, fill="#663399")

im.show()
im.save("obraz_z_napisem.png")
