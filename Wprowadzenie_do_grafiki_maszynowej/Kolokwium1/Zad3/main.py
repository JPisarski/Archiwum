import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

tab = np.loadtxt("tab1.txt", dtype=np.bool_)
w = tab.shape[0]
h = tab.shape[1]
tab1 = np.zeros((w, h, 3), dtype=np.uint8)
for i in range(w):
    for j in range(h):
        if tab[i, j] == 1:
            tab1[i, j] = (0, 0, 100)
        else:
            tab1[i, j] = (255, 255, 155)

obraz = Image.fromarray(tab1)
obraz.save("obraz_rgb.png")
obraz.show()
