from PIL import Image
import numpy as np


# zadanie 1

def rysuj_ramke_w_obrazie(obraz, grub):
    obraz_wstawiany = np.asarray(obraz) * 1
    h, w = obraz_wstawiany.shape
    for i in range(h):
        for j in range(grub):
            obraz_wstawiany[i][j] = 0
        for j in range(w - grub, w):
            obraz_wstawiany[i][j] = 0
    for i in range(w):
        for j in range(grub):
            obraz_wstawiany[j][i] = 0
        for j in range(h - grub, h):
            obraz_wstawiany[j][i] = 0
    tab = obraz_wstawiany.astype(bool)
    return Image.fromarray(tab)


# zadanie 2

inicjaly = Image.open("inicjaly.bmp")

inicjaly_10 = rysuj_ramke_w_obrazie(inicjaly, 10)
inicjaly_10.save("ramka10.bmp")

inicjaly_5 = rysuj_ramke_w_obrazie(inicjaly, 5)
inicjaly_5.save("ramka5.bmp")


# zadanie 3

# 1

def fun1(w, h, grub):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    ile = 1
    m = min(w, h)
    dokad = int(m / (2 * grub))
    for i in range(0, dokad):
        tab[ile * grub: h - (ile * grub), ile * grub: w - (ile * grub)] = ile % 2
        ile += 1
    tab1 = tab.astype(bool)
    return Image.fromarray(tab1)


# 2

def fun2(w, h, grub):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(w / grub)
    for k in range(ile):
        for g in range(grub):
            i = k * grub + g
            for j in range(h):
                tab[j, i] = k % 2
    tab1 = tab.astype(bool)
    return Image.fromarray(tab1)


# 3

def fun3(w, h, m, n):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    tab[0:n, 0:m] = 0
    tab[n:h, m:w] = 0
    tab1 = tab.astype(bool)
    return Image.fromarray(tab1)


# 4 fun4(w,h) zaznacza na obrazie poziomą i pionową linię dzielącą obraz na pół (w przypadku, gdyby:
# - w lub h miało wartość parzystą, linia jest 2 razy grubsza niż w przypadku, gdyby miało wartość nieparzystą)
def fun4(w, h):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    for i in range(h):
        if (w/2) % 2 == 0:
            tab[i][int(w/2)-1] = 0
            tab[i][int(w/2)] = 0
        else:
            tab[i][int(w/2)] = 0
    for i in range(w):
        if (h/2) % 2 == 0:
            tab[int(h/2)-1][i] = 0
            tab[int(h/2)][i] = 0
        else:
            tab[int(h/2)][i] = 0
    tab1 = tab.astype(bool)
    return Image.fromarray(tab1)

# zadanie 4

# w=480, h=320, grub=10, m=100, n=50

o1 = fun1(480, 320, 10)
o1.save("o1.bmp")
o2 = fun2(480, 320, 10)
o2.save("o2.bmp")
o3 = fun3(480, 320, 100, 50)
o3.save("o3.bmp")
o4 = fun4(480, 320)
o4.save("o4.bmp")

# zadanie 5

# 1.1


def wstaw_obraz_w_obraz(obraz_bazowy, obraz_wstawiany, m, n):  # m<=w,  n<=h
    tab_obraz_w = np.asarray(obraz_wstawiany) * 1
    h0, w0 = tab_obraz_w.shape
    tab_obraz_b = np.asarray(obraz_bazowy) * 1
    hb, wb = tab_obraz_b.shape
    n_k = min(hb, n + h0)
    m_k = min(wb, m + w0)
    n_p = max(0, n)
    m_p = max(0, m)
    print(n_k, m_k)
    print(n_p, m_p)
    for i in range(n_p, n_k):
        for j in range(m_p, m_k):
            tab_obraz_b[i][j] = tab_obraz_w[i - n][j - m]
    tab = tab_obraz_b.astype(bool)  # zapisanie tablicy w typie bool (obrazy czarnobiałe)
    return Image.fromarray(tab)

# 1.2

o1 = Image.open("o1.bmp")
inicjaly = Image.open("inicjaly.bmp")
r1 = wstaw_obraz_w_obraz(o1, inicjaly, 300, 90)
r1.save("wstaw1.bmp")
r2 = wstaw_obraz_w_obraz(o1, inicjaly, 10, 290)
r2.save("wstaw2.bmp")


