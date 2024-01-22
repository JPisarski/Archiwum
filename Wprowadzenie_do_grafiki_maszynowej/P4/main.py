from PIL import Image
import numpy as np
from PIL import ImageChops
import matplotlib.pyplot as plt

# zadanie 1

im1 = Image.open("../P4/obraz.jpg")

# zadanie 2

# a

tab1 = np.array(im1)
t_r = tab1[:, :, 0]
t_g = tab1[:, :, 1]
t_b = tab1[:, :, 2]
im_r = Image.fromarray(t_r)
im_g = Image.fromarray(t_g)
im_b = Image.fromarray(t_b)

# b

im2 = Image.merge("RGB", (im_r, im_g, im_b))
porownanie = ImageChops.difference(im1, im2)

# c

plt.figure(figsize=(32, 16))
plt.subplot(1, 3, 1)
plt.imshow(im1)
plt.axis("off")
plt.subplot(1, 3, 2)
plt.imshow(im2)
plt.axis("off")
plt.subplot(1, 3, 3)
plt.imshow(porownanie)
plt.axis("off")
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig("fig1.png")
plt.show()

# zadanie 3

r, g, b = im1.split()
im3 = Image.merge("RGB", (r, b, g))

# a

im3.save("im3.jpg")
im3.save("im3.png")

# b

im3_jpg = Image.open("../P4/im3.jpg")
im3_png = Image.open("../P4/im3.png")
porownanie2 = ImageChops.difference(im3_jpg, im3_png)



# c

plt.figure(figsize=(32, 16))
plt.subplot(1, 3, 1)
plt.imshow(im3_jpg)
plt.axis("off")
plt.subplot(1, 3, 2)
plt.imshow(im3_png)
plt.axis("off")
plt.subplot(1, 3, 3)
plt.imshow(porownanie2)
plt.axis("off")
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig("fig2.png")
plt.show()

# widać lekką różnicę

# zadanie 4

obraz1_1jpg = Image.open("obraz1_1.jpg")
obraz1_1png = Image.open("obraz1_1.png")
porownanie3 = ImageChops.difference(obraz1_1jpg, obraz1_1png)

obraz1_1Njpg = Image.open("obraz1_1N.jpg")
obraz1_1Npng = Image.open("obraz1_1N.png")
porownanie4 = ImageChops.difference(obraz1_1Njpg, obraz1_1Npng)

obraz1_2jpg = Image.open("obraz1_2.jpg")
obraz1_2png = Image.open("obraz1_2.png")
porownanie5 = ImageChops.difference(obraz1_2jpg, obraz1_2png)

obraz1_2Njpg = Image.open("obraz1_2N.jpg")
obraz1_2Npng = Image.open("obraz1_2N.png")
porownanie6 = ImageChops.difference(obraz1_2Njpg, obraz1_2Npng)

plt.figure(figsize=(32, 16))
plt.subplot(4, 3, 1)
plt.imshow(obraz1_1jpg, "gray")
plt.axis("off")
plt.subplot(4, 3, 2)
plt.imshow(obraz1_1png, "gray")
plt.axis("off")
plt.subplot(4, 3, 3)
plt.imshow(porownanie3, "gray")
plt.axis("off")

plt.subplot(4, 3, 4)
plt.imshow(obraz1_1Njpg, "gray")
plt.axis("off")
plt.subplot(4, 3, 5)
plt.imshow(obraz1_1Npng, "gray")
plt.axis("off")
plt.subplot(4, 3, 6)
plt.imshow(porownanie4, "gray")
plt.axis("off")

plt.subplot(4, 3, 7)
plt.imshow(obraz1_2jpg, "gray")
plt.axis("off")
plt.subplot(4, 3, 8)
plt.imshow(obraz1_2png, "gray")
plt.axis("off")
plt.subplot(4, 3, 9)
plt.imshow(porownanie5, "gray")
plt.axis("off")

plt.subplot(4, 3, 10)
plt.imshow(obraz1_2Njpg, "gray")
plt.axis("off")
plt.subplot(4, 3, 11)
plt.imshow(obraz1_2Npng, "gray")
plt.axis("off")
plt.subplot(4, 3, 12)
plt.imshow(porownanie6, "gray")
plt.axis("off")

plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig("fig3.png")
plt.show()


# obrazy różnią się

# zadanie 5


def ramki(w, h, grub, kolor):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    ile = 0
    m = min(w, h)
    dokad = int(m / (2 * grub))
    for i in range(0, dokad):
        tab[ile * grub: h - (ile * grub), ile * grub: w - (ile * grub)] = kolor % 256
        ile += 1
        kolor += 25
    return tab


w, h = im1.size
tab = ramki(w, h, 5, 0)
im4 = Image.fromarray(tab)

# a

r1, g1, b1 = im1.split()
im1_1 = Image.merge("RGB", (im4, g1, b1))
im1_2 = Image.merge("RGB", (r1, im4, b1))
im1_3 = Image.merge("RGB", (r1, g1, im4))

# b

plt.figure(figsize=(32, 16))
plt.subplot(1, 3, 1)
plt.imshow(im1_1)
plt.axis("off")
plt.subplot(1, 3, 2)
plt.imshow(im1_2)
plt.axis("off")
plt.subplot(1, 3, 3)
plt.imshow(im1_3)
plt.axis("off")
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig("fig4.png")
plt.show()

# zadanie 6

# a

r2 = Image.open("serduszko.bmp").convert("L")
g2 = Image.open("kwadrat.bmp").convert("L")
b2 = Image.open("koło.bmp").convert("L")

# b

rgb1 = Image.merge("RGB", (r2, g2, b2))
rgb2 = Image.merge("RGB", (g2, r2, b2))
rgb3 = Image.merge("RGB", (b2, g2, r2))
rgb4 = Image.merge("RGB", (r2, b2, g2))
rgb5 = Image.merge("RGB", (g2, b2, r2))
rgb6 = Image.merge("RGB", (b2, r2, g2))

plt.figure(figsize=(32, 16))
plt.subplot(2, 3, 1)
plt.imshow(rgb1)
plt.axis("off")
plt.subplot(2, 3, 2)
plt.imshow(rgb2)
plt.axis("off")
plt.subplot(2, 3, 3)
plt.imshow(rgb3)
plt.axis("off")
plt.subplot(2, 3, 4)
plt.imshow(rgb4)
plt.axis("off")
plt.subplot(2, 3, 5)
plt.imshow(rgb5)
plt.axis("off")
plt.subplot(2, 3, 6)
plt.imshow(rgb6)
plt.axis("off")
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig("fig5.png")
plt.show()


# zadanie 7

# Funkcja porownaj_obraz sprawdza, czy podane 2 obrazy są identyczne.
# Jeśli tak, to zwraca True. Jeśli nie, to zwraca False.
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


print("Obrazy im1 i im2 są identyczne: ", porownaj_obraz(im1, im2))
print("Obrazy im3_jpg i im3_png są identyczne: ", porownaj_obraz(im3_jpg, im3_png))
