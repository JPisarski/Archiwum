import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

mix = Image.open("mix211.png")
obraz = Image.open("obraz11.jpg")
r, g, b = obraz.split()





Image.merge("RGB", (b, g, r)).show()