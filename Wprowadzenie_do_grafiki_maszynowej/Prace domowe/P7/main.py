from PIL import Image
import math


# zadanie 1
# 1.1

def rysuj_kwadrat_max(obraz, m, n, k):
    obraz1 = obraz.copy()
    pix = obraz.load()
    pix1 = obraz1.load()
    d = int(k / 2)
    kolor = [0, 0, 0]
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pixel = pix[x, y]
            for c in range(3):
                if pixel[c] > kolor[c]:
                    kolor[c] = pixel[c]
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pix1[x, y] = (kolor[0], kolor[1], kolor[2])
    return obraz1


obraz = Image.open("obraz.jpg")
obraz1 = rysuj_kwadrat_max(obraz, 220, 220, 51)
obraz1 = rysuj_kwadrat_max(obraz1, 500, 400, 55)
obraz1 = rysuj_kwadrat_max(obraz1, 720, 460, 31)
obraz1.save("obraz1.png")


# 1.2


def rysuj_kwadrat_min(obraz, m, n, k):
    obraz1 = obraz.copy()
    pix = obraz.load()
    pix1 = obraz1.load()
    d = int(k / 2)
    kolor = [255, 255, 255]
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pixel = pix[x, y]
            for c in range(3):
                if pixel[c] < kolor[c]:
                    kolor[c] = pixel[c]
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pix1[x, y] = (kolor[0], kolor[1], kolor[2])
    return obraz1


obraz2 = rysuj_kwadrat_min(obraz, 220, 220, 51)
obraz2 = rysuj_kwadrat_min(obraz2, 500, 400, 55)
obraz2 = rysuj_kwadrat_min(obraz2, 720, 460, 31)
obraz2.save("obraz2.png")


# zadanie 2


def rysuj_kolo_kopia(obraz, m_s, n_s, r, nx, ny):  # nx, ny - miejsce, gdzie wstawiamy środek skopiowanego koła
    obraz1 = obraz.copy()
    w, h = obraz.size
    for i in range(w):
        for j in range(h):
            if (i - m_s) ** 2 + (j - n_s) ** 2 < r ** 2:
                if 0 <= i + nx - m_s < w and 0 <= j + ny - n_s < h:
                    obraz1.putpixel((i + (nx - m_s), j + (ny - n_s)), obraz.getpixel((i, j)))
    return obraz1


obraz3 = rysuj_kolo_kopia(obraz, 490, 365, 50, 492, 88)
obraz3.save("obraz3.png")

# 2.1


obraz4 = rysuj_kolo_kopia(obraz, 490, 365, 50, 150, 10)
obraz4 = rysuj_kolo_kopia(obraz4, 490, 365, 50, 20, 20)
obraz4 = rysuj_kolo_kopia(obraz4, 490, 365, 50, 0, 150)
obraz4 = rysuj_kolo_kopia(obraz4, 490, 365, 50, 0, 300)
obraz4 = rysuj_kolo_kopia(obraz4, 490, 365, 50, 220, 370)
obraz4 = rysuj_kolo_kopia(obraz4, 490, 365, 50, 359, 370)
obraz4 = rysuj_kolo_kopia(obraz4, 490, 365, 50, 615, 370)
obraz4 = rysuj_kolo_kopia(obraz4, 490, 365, 50, 750, 400)
obraz4 = rysuj_kolo_kopia(obraz4, 490, 365, 50, 880, 550)
obraz4 = rysuj_kolo_kopia(obraz4, 490, 365, 50, 830, 660)

obraz4.save("obraz4.png")


# zadanie 3


def odbij_w_pionie(im):
    img = im.copy()
    w, h = im.size
    px = img.load()
    for i in range(w):
        for j in range(h):
            px[i, j] = px[w - 1 - i, j]
    return img


obraz5 = odbij_w_pionie(obraz)
obraz5.show()

# Zmieniona funkcja odbija prawą stronę na lewo. Dzieje się to dlatego, że wartości pixeli pobierane są z tablicy
# obrazu, w której jednocześnie zmieniamy wartości pikseli. Gdy pętla przekroczy połowę pikseli (połowę obrazu),
# funkcja zacznie ustalać nowe wartości drugiej połowy pikseli (połowy obrazu) na podstawie zmienionych już wartość
# pikseli pierwszej połowy obrazu. Dlatego druga połowa wygląda jak odbicie lustrzane pierwszej.


# dodatkowe

# def odbij_gora_dol(obraz):
#     px0 = obraz.load()
#     img = obraz.copy()
#     w, h = obraz.size
#     px = img.load()
#     for i in range(w):
#         for j in range(h):
#             px[i, j] = px0[i, h - j - 1]
#     return img
#
#
# odbij_gora_dol(obraz).show()


# def odbij_dol_na_gore(obraz):
#     img = obraz.copy()
#     w, h = obraz.size
#     h1 = int(h / 2)
#     px = img.load()
#     for i in range(w):
#         for j in range(h1):
#             px[i, j] = px[i, h - j - 1]
#     return img
#
#
#
# odbij_dol_na_gore(obraz).show()


# def odbij_gore_na_dol(obraz):
#     img = obraz.copy()
#     w, h = obraz.size
#     h1 = int(h / 2)
#     px = img.load()
#     for i in range(w):
#         for j in range(h1, h):
#             px[i, j] = px[i, h - j - 1]
#     return img
#
#
#
# odbij_gore_na_dol(obraz).show()
