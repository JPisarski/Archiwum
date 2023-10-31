import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import openpyxl as op

# zadanie 1

# x = np.arange(1, 20, 1)
# y = 1/x
# plt.plot(x, y)
# plt.legend(labels=["1/x"])
# plt.xlabel("x")
# plt.ylabel("f(x)")
# plt.axis([0, 20, 0, 1])
# plt.show()

# zadanie 2

# x = np.arange(1, 20, 1)
# y = 1/x
# plt.plot(x, y, "g>")
# plt.legend(labels=["f(x)=1/x"])
# plt.xlabel("x")
# plt.ylabel("f(x)")
# plt.axis([0, 20, 0, 1])
# plt.title("Wykres funkcji f(x) dla x [1, 19]")
# plt.plot(x, y, "g:")
# plt.show()

# zadanie 3

# x = np.arange(0, 31, 0.1)
# y = np.sin(x)
# z = np.cos(x)
# plt.plot(x, y, "r")
# plt.plot(x, z, "g")
# plt.xlabel("sin(x) i cos(x)")
# plt.ylabel("Wartości")
# plt.legend(labels=["sin(x)", "cos(x)"], loc="upper right")
# plt.axis([0, 30, -1, 1])
# plt.show()

# zadanie 4

# dane = pd.read_csv("iris.data", header=None, sep=",", decimal=".")
# print(dane)
# x = dane[0]
# y = dane[1]
# z = np.abs(x-y)
# kolor =np.random.randint(0, 150, 150)
# plt.scatter(x, y, c=kolor, s=z)
# plt.xlabel("Sepal Lenght")
# plt.ylabel("Sepal Width")
# plt.show()

# zadanie 5

# a = pd.read_excel("imiona.xlsx", header=0)
# print(a)
#
# x = a.groupby(["Plec"]).agg({"Liczba": ["sum"]})
# print(x)
# y = pd.DataFrame({"Plec": ["K", "M"], "Liczba": [3521321, 3714961]})
# print(y)
# plt.subplot(1, 3, 1,)
# plt.bar(data=y,x="Plec", height="Liczba", color=['red', 'green'])
# plt.xlabel("Płeć")
# plt.ylabel("Liczba narodzin w danych latach")
# plt.title("Wykres słupkowy narodzin w danych latach")
#
#
#
# w = a[a["Plec"]=="K"]
# m = a[a["Plec"]=="M"]
# k = w.groupby(["Rok"]).agg({"Liczba": ["sum"]})
# c = m.groupby(["Rok"]).agg({"Liczba": ["sum"]})
# print(k)
# plt.subplot(1, 3, 2,)
# plt.plot(np.arange(2000, 2018, 1), [187142, 181975, 175590, 173995, 176779, 183112, 190437, 201448, 216632, 219811,
#                                         216566, 204174, 203908, 194290, 197456, 196672, 199724, 201610])
# print(c)
# plt.plot(np.arange(2000, 2018, 1), [197263, 191947, 185415, 183215, 186903, 192820, 200796, 211946, 227408, 230881,
#                                     229289, 216221,216021,204890,208585,207746,210699,212916])
# plt.legend(labels=["Kobiety", "Mężczyźni"])
# plt.xlabel("Rok")
# plt.ylabel("Liczba")
# plt.axis([2000, 2017, 150000, 250000])
# plt.xticks(np.arange(2000,2018,1), rotation=90)
# plt.title("Wykres słupkowy narodzin w danych latach")
#
#
#
# z = a.groupby(["Rok"]).agg({"Liczba": ["sum"]})
# print(z)
# q = pd.DataFrame({"Rok": np.arange(2000, 2018, 1), "Liczba": [384405, 373922, 361005, 357210, 363682, 375932, 391233,
#                                                                 413394, 444040, 450692, 445855, 420395, 419929, 399180,
#                                                                 406041, 404418, 410423, 414526]})
# plt.subplot(1, 3, 3,)
# plt.bar(data=q, x="Rok", height="Liczba", color=["blue"])
# plt.xlabel("Lata")
# plt.ylabel("Liczba narodzin w danych latach")
# plt.title("Wykres słupkowy narodzin w danych latach")
# plt.xticks(np.arange(2000, 2018, 1), rotation=90)
# plt.subplots_adjust(wspace=1.5)
# plt.show()

# zadanie 6

# a = pd.read_csv("zamowienia.csv", header=0, sep=";", decimal=".")
# x = a["Sprzedawca"].unique()
# y = a.groupby(["Sprzedawca"]).agg({"Utarg":["sum"]})
# print(x)
# print(y)
# z = [68792.25, 72527.63, 225763.68, 201196.27, 75048.04, 182500.09, 123032.67, 162503.78, 116962.99]
# myexplode = [0.2, 0, 0, 0, 0.5, 0.6, 0.7, 0.5, 0.9]
# plt.pie(z, labels=x, autopct=lambda pct: "{:.1f}%".format(pct), explode=myexplode, shadow=True)
# plt.show()

