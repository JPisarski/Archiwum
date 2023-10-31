import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl as pl

#do zadań 1, 2, 3

a = pd.read_excel("imiona.xlsx", header=0)

#zadanie 1

# x = a["Rok"].unique()
# print(x)
# y = a.groupby(["Rok"]).agg({"Liczba":["sum"]})
# print(y)
# y.plot(title=" Wykres liczby narodzin w latach 2000-2017", xticks=x, legend=False, rot=90)
# plt.show()

#zadanie 2

# z = a.groupby(["Plec"]).agg({"Liczba":["sum"]})
# print(z)
#
# z.plot(kind="bar", title="Liczba narodzin dziewczynek i chłopców w latach 2000-2017", legend=False, rot=0)
# plt.show()

#zadanie 3

# w = a[a["Rok"]>=2014]
# print(w)
# m = w.groupby(["Plec"]).agg({"Liczba":["sum"]})
# print(m)
# m.plot(kind="pie", subplots=True, title= "Podział procentowy narodzin chłopców i dziewcząt w latach 2014-2017", autopct='%1.1f%%', legend=False)
# plt.show()

# #do zadania 4

b = pd.read_csv("zamowienia.csv", header=0, sep=";", decimal=",")

# #zadanie 4


# t = b.groupby(["Sprzedawca"]).agg({"idZamowienia":["count"]})
# print(t)
#
# t.plot(kind="bar", legend=False, title="Ilość zamowień każdego sprzedawcy")
# plt.show()
