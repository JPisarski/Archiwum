import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def rysuj_ramke_kolor(w, h, grub, r, g, b):
    t = (h, w, 3)
    tab = np.ones(t, dtype=np.uint8)
    tab[:] = (255, 0, 0)
    z1 = h - grub
    z2 = w - grub
    tab[grub:z1, grub:z2, 0] = r
    tab[grub:z1, grub:z2, 1] = g
    tab[grub:z1, grub:z2, 2] = b
    return tab


Image.fromarray(rysuj_ramke_kolor(120, 60, 10, 100, 200, 300)).show()