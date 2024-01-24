import numpy as np
from PIL import Image


def porownaj_obraz(m1, m2):
    if m1.size != m2.size:
        return False
    if m1.mode != m2.mode:
        return False
    t1 = np.array(m1)
    t2 = np.array(m2)
    if t1.shape != t2.shape:
        return False
    if len(t1.shape) == 2:
        h, w = t1.shape
        for x in range(h):
            for y in range(w):
                if t1[x][y] != t2[x][y]:
                    return False
    if len(t1.shape) == 3:
        h, w, t = t1.shape
        for k in range(3):
            for x in range(h):
                for y in range(w):
                    if t1[x][y][k] != t2[x][y][k]:
                        return False
    return True




