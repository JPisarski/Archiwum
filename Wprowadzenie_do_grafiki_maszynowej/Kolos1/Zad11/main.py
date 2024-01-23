import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


obraz = Image.open("obraz1.jpg")
tab = np.array(obraz)
print(obraz.format)
print(tab.itemsize)
print(obraz.getpixel((363, 225)))
print(tab[310, 250])