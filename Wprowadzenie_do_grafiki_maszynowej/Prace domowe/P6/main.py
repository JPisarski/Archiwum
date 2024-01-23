from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# zadanie 1

obraz = Image.open("obraz.jpg")
inicjaly = Image.open("inicjaly.bmp")


# zadanie 2

# a

def wstaw_inicjaly(obraz, inicjaly, m, n, kolor):
    obraz1 = obraz.copy()
    w, h = obraz1.size
    w0, h0 = inicjaly.size
    for i in range(w0):
        for j in range(h0):
            if m + i < w and n + j < h:
                if inicjaly.getpixel((i, j)) == 0:
                    obraz1.putpixel((m + i, n + j), kolor)
    return obraz1


obraz1 = wstaw_inicjaly(obraz, inicjaly, obraz.size[0] - inicjaly.size[0],
                        obraz.size[1] - inicjaly.size[1],(255, 0, 0))
obraz1.save("obraz1.png")
obraz1.show()


# b

def wstaw_inicjaly_maska(obraz, inicjaly, m, n, x, y, z):
    obraz1 = obraz.copy()
    w, h = obraz1.size
    w0, h0 = inicjaly.size
    for i in range(w0):
        for j in range(h0):
            if m + i < w and n + j < h:
                if inicjaly.getpixel((i, j)) == 0:
                    p = obraz1.getpixel((m + i, n + j))
                    obraz1.putpixel((m + i, n + j), (p[0] + x, p[1] + y, p[2] + z))
    return obraz1


obraz2 = wstaw_inicjaly_maska(obraz, inicjaly, int((obraz.size[0] - inicjaly.size[0])/2),
                              int((obraz.size[1] - inicjaly.size[1])/2), 100, 75, 150)
obraz2.save("obraz2.png")
obraz2.show()


# zadanie 3

# a

def wstaw_inicjaly_load(obraz, inicjaly, m, n, kolor):
    obraz1 = obraz.copy()
    pixel = obraz1.load()
    w, h = obraz1.size
    pixini = inicjaly.load()
    w0, h0 = inicjaly.size
    for i in range(w0):
        for j in range(h0):
            if m + i < w and n + j < h:
                if pixini[i, j] == 0:
                    pixel[m + i, n + j] = kolor
    return obraz1


obraz3 = wstaw_inicjaly_load(obraz, inicjaly, obraz.size[0] - inicjaly.size[0],
                             obraz.size[1] - inicjaly.size[1],(255, 0, 255))
obraz3.show()

# b

# musiałem zmienić nazwę funkcji


def wstaw_inicjaly_maska_2(obraz, inicjaly, m, n, x, y, z):
    obraz1 = obraz.copy()
    pixel = obraz1.load()
    w, h = obraz1.size
    pixini = inicjaly.load()
    w0, h0 = inicjaly.size
    for i in range(w0):
        for j in range(h0):
            if m + i < w and n + j < h:
                if pixini[i, j] == 0:
                    p = pixel[m + i, n + j]
                    pixel[m + i, n + j] = (p[0] + x, p[1] + y, p[2] + z)
    return obraz1


obraz4 = wstaw_inicjaly_maska_2(obraz, inicjaly, int((obraz.size[0] - inicjaly.size[0])/2),
                              int((obraz.size[1] - inicjaly.size[1])/2), 50, 75, 250)
obraz4.show()


# zadanie 4

# a

def kontrast(obraz, wsp_kontrastu):
    mn = ((255 + wsp_kontrastu)/255) ** 2
    return obraz.point(lambda i: 128 + (i - 128) * mn)


obraz5 = kontrast(obraz, 25)
obraz6 = kontrast(obraz, 50)
obraz7 = kontrast(obraz, 100)
plt.figure(figsize=(32, 16))
plt.subplot(1, 4, 1)
plt.imshow(obraz)
plt.axis('off')
plt.subplot(1, 4, 2)
plt.imshow(obraz7)
plt.axis('off')
plt.subplot(1, 4, 3)
plt.imshow(obraz6)
plt.axis('off')
plt.subplot(1, 4, 4)
plt.imshow(obraz5)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig1.png')
plt.show()

# b


def transformacja_logarytmiczna(obraz):
    return obraz.point(lambda i: 255 * np.log(1 + i / 255))


def filtr_liniowy(obraz, a, b):
    return obraz.point(lambda i: i * a + b)


obraz8 = transformacja_logarytmiczna(obraz)
obraz9 = filtr_liniowy(obraz, 2, 100)
plt.figure(figsize=(32, 16))
plt.subplot(1, 3, 1)
plt.imshow(obraz)
plt.axis('off')
plt.subplot(1, 3, 2)
plt.imshow(obraz8)
plt.axis('off')
plt.subplot(1, 3, 3)
plt.imshow(obraz9)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig2.png')
plt.show()

# c

# gamma więsza od 0, ułamek, liczba rzeczywista do 100


def transformacja_gamma(obraz, gamma):
    return obraz.point(lambda i: (i / 255) ** (1 / gamma) * 255)


obraz10 = transformacja_gamma(obraz, 0.1)
obraz11 = transformacja_gamma(obraz, 0.5)
obraz12 = transformacja_gamma(obraz, 5)
plt.figure(figsize=(32, 16))
plt.subplot(1, 4, 1)
plt.imshow(obraz)
plt.axis('off')
plt.subplot(1, 4, 2)
plt.imshow(obraz10)
plt.axis('off')
plt.subplot(1, 4, 3)
plt.imshow(obraz11)
plt.axis('off')
plt.subplot(1, 4, 4)
plt.imshow(obraz12)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig3.png')
plt.show()


# zadanie 5

# w 1 przypadku, gdy wartość piksela przekroczy 255, jest zastosowana operacja: wartość piksela = wartość piksela % 256
# w 2 przypadku, gdy wartość piksela przekroczy 255, wartość piksela ustanawiana jest na 255.
# Więcej wyjaśnień w raporcie.

# zadanie 6


def obraz_plus_sto(obraz):
    T = np.array(obraz, dtype='uint8')
    w, h, k = T.shape
    for x in range(w):
        for y in range(h):
            for z in range(k):
                if T[x, y, z] + 100 <= 255:
                    T[x, y, z] = T[x, y, z] + 100
                else:
                    T[x, y, z] = 255
    return Image.fromarray(T)


obraz13 = obraz.copy()
obraz13 = obraz13.point(lambda i: i + 100)
obraz13.show()
obraz14 = obraz_plus_sto(obraz)
obraz14.show()



