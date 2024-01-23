from PIL import Image
import numpy as np

# zadanie 2

obraz = Image.open("inicjaly.bmp")

print("Tryb:", obraz.mode)
print("Format:", obraz.format)
print("Rozmiar:", obraz.size)

# zadanie 3

obraz = Image.open("inicjaly.bmp")
t_obraz = np.asarray(obraz)
t_obraz1 = np.asarray(obraz) * 1

inicjaly_txt = open("inicjaly.txt", "w")

for x in t_obraz1:
    for y in x:
        inicjaly_txt.write(str(y) + ' ')
    inicjaly_txt.write('\n')

inicjaly_txt.close()

# zadanie 4

# a

obraz = Image.open("inicjaly.bmp")
t1 = np.asarray(obraz)
print("Typ danych tablicy t1:", t1.dtype)
print("Rozmiar tablicy t1:", t1.shape)
print("Rozmiar tablicy t1:", t1.size)
print("Wymiar tablicy t1:", t1.ndim)
print("Rozmiar wyrazu tablicy t1:", t1.itemsize)

# b

obraz = Image.open("inicjaly.bmp")
t1 = np.asarray(obraz)
print("Piksel (0,0):", t1[0][0])
print("Piksel (50,30) :", t1[30][50])
print("Piksel (90,40) :", t1[40][90])
print("Piksel (99,0) :", t1[0][99])

# zadanie 5

t2 = np.loadtxt("inicjaly.txt", dtype=np.bool_)

obraz = Image.open("inicjaly.bmp")
t_obraz = np.asarray(obraz)

print("Typ danych tablicy t2:", t2.dtype)
print("Rozmiar tablicy t2:", t2.shape)
print("Rozmiar tablicy t2:", t2.size)
print("Wymiar tablicy t2:", t2.ndim)
print("Rozmiar wyrazu tablicy t2:", t2.itemsize)
print("Typ danych tablicy t_obraz:", t_obraz.dtype)
print("Rozmiar tablicy t_obraz:", t_obraz.shape)
print("Rozmiar tablicy t_obraz:", t_obraz.size)
print("Wymiar tablicy t_obraz:", t_obraz.ndim)
print("Rozmiar wyrazu tablicy t_obraz:", t_obraz.itemsize)

# zadanie 6

t3 = np.loadtxt("inicjaly.txt", dtype=np.uint8)
obraz = Image.open("inicjaly.bmp")
t_obraz = np.asarray(obraz)

print("Typ danych tablicy t3:", t3.dtype)
print("Rozmiar tablicy t3:", t3.shape)
print("Rozmiar tablicy t3:", t3.size)
print("Wymiar tablicy t3:", t3.ndim)
print("Rozmiar wyrazu tablicy t3:", t3.itemsize)
print("Typ danych tablicy t_obraz:", t_obraz.dtype)
print("Rozmiar tablicy t_obraz:", t_obraz.shape)
print("Rozmiar tablicy t_obraz:", t_obraz.size)
print("Wymiar tablicy t_obraz:", t_obraz.ndim)
print("Rozmiar wyrazu tablicy t_obraz:", t_obraz.itemsize)

#a

obraz_1 = Image.fromarray(t3)
obraz_1.show()

obraz_2 = Image.fromarray(t3 * 255)
obraz_2.show()

