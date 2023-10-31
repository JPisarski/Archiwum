import numpy as np
import pandas as pd
import openpyxl as px
import seaborn as sn
import matplotlib.pyplot as plt

# numpy 1

# a = np.arange(4, 4*20+1, 4)
# print(a)

# a = [2.5, 6.0, 5.4, 5.5, 3.6]
# b = np.array(a, dtype="int32")
# print(b)
# print(b.dtype)


# def fun(n):
#     a = [2**x for x in range(1, n*n+1)]
#     b = np.array(a)
#     return b.reshape(n, n)
#
# print(fun(3))


# def fun(podstawa, ilosc):
#     return np.logspace(1, ilosc, base=podstawa, num=ilosc)
#
#
# print(fun(2, 4))

# def fun(n):
#     a = np.arange(n, 0, -1)
#     b = np.diag(a, 2)
#     return b
#
#
# print(fun(5))

# a = np.array(list("Maria"))
# b = np.array(list("Krzyś"))
# c = np.array(list("Środa"))
# d = np.flip(b)
#
# w = np.diag(c)
# w[:, 4] = a
# w[:, 0] = d
# print(w)

# def fun(n):
#     d = [2 for x in range(0, n)]
#     a = np.diag(d)
#     for x in range(1, n):
#         r = 2+x*2
#         t = np.diag([r for h in range(x, n)], x)
#         y = np.diag([r for h in range(x, n)], -x)
#         a = a+t+y
#     return a
#
#
# print(fun(3))

# def fun(tablica, kierunek):
#     if kierunek == "pion":
#         if (len(tablica.shape) == 2 and tablica.shape[1] % 2 == 1) or \
#                 (len(tablica.shape) == 1 and tablica.shape[0] % 2 == 1):
#             print("Ilość kolumn nie pozwala na operację")
#         else:
#             if len(tablica.shape) == 2:
#                 x = tablica.shape[1]/2
#                 y = tablica[:, :int(x)]
#                 z = tablica[:, int(x):]
#                 print(y)
#                 print(z)
#             else:
#                 x = tablica.shape[0]/2
#                 y = tablica[:, :int(x)]
#                 z = tablica[:, int(x):]
#                 print(y)
#                 print(z)
#     elif kierunek == "poziom":
#         if (len(tablica.shape) == 2 and tablica.shape[0] % 2 == 1) or len(tablica.shape) == 1:
#             print("Ilość wierszy nie pozwala na operację")
#         else:
#             x = tablica.shape[0]/2
#             y = tablica[:int(x)]
#             z = tablica[int(x):]
#             print(y)
#             print(z)
#
#
# a = np.array([[4,4], [5,5]])
# fun(a, "poziom")

# a = [(5+5*n) for n in range(0, 25)]
# b = np.array(a).reshape(5, 5)
# print(b)


# numpy 2

# a = np.array([1,2,3])
# b = np.array([4,5,6])
# print(a*b)

# a = np.arange(0, 9).reshape(3, 3)
# b = np.arange(0, 16).reshape(4, 4)
# print(a.min(axis=0))
# print(a.min(axis=1))
# print(b.min(axis=0))
# print(b.min(axis=1))

# a = np.array([1,2,3])
# b = np.array([4,5,6])
# print(np.dot(a, b))

# a = np.array([1.0,2.0,3.0])
# b = np.array([4,5,6])
# print(a*b)

# a = np.array(([0, 1, 2], [3, 4, 5]))
# b = np.cos(a)
# c = np.sin(a)
# print(c)
# print(b)
# print(c + b)

# a = np.arange(0, 9).reshape(3, 3)
# for x in a:
#     print(x)
# for x in a.flat:
#     print(x)


# b = np.arange(0, 9).reshape(3, 3)
# print(b)
# print(b.reshape(9, 1))
# print(b.ravel())


# pandas 1

# df = pd.read_excel("imiona.xlsx")

# print(df[df["Liczba"] > 1000])

# print(df[df["Imie"] == "JAKUB"])

# print(df["Liczba"].sum())

# a = df[df["Rok"] <= 2005]
# print(a["Liczba"].sum())

# a = df[df["Plec"] == "M"]
# b = df[df["Plec"] == "K"]
# print(a["Liczba"].sum())
# print(b["Liczba"].sum())

# a = df[df["Plec"] == "M"].groupby(["Imie"]).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'), ascending=False)
# b = df[df["Plec"] == "K"].groupby(["Imie"]).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'), ascending=False)
# print(a.iloc[0])
# print(b.iloc[0])

# a = df[df["Plec"] == "M"]
# b = df[df["Plec"] == "K"]
#
#
# for x in range(2000, 2018):
#     z = a[a["Rok"] == x]
#     print("Najpopularniejsze imię męskie w roku:")
#     print(x)
#     z = z[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
#     print(z.idxmax().iloc[0])
#
# for x in range(2000, 2018):
#     z = b[b["Rok"] == x]
#     print("Najpopularniejsze imię żeńskie w roku:")
#     print(x)
#     z = z[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
#     print(z.idxmax().iloc[0])


# df = pd.read_csv("zamowienia.csv", header=0, sep=";", decimal=".")

# print(df["Sprzedawca"].unique())

# print(df["Utarg"].sort_values(ascending=False).head(5))

# print(df.groupby(['Sprzedawca']).size())

# print(df.groupby(["Kraj"]).size())

# print(df[(df["Kraj"] == "Polska") & (df["Data zamowienia"] >= "2005-01-01") & (df["Data zamowienia"] <= "2005-12-31")].
#       agg({"Utarg": ["sum"]}))

# print(df[df["Data zamowienia"].str[:4] == "2004"].agg({"Utarg": ["mean"]}))

# rok_2004 = df[((df["Data zamowienia"] >= "2004-01-01") & (df["Data zamowienia"] <= "2004-12-31"))]
# rok_2004.to_csv("zamowienia_2004.csv", index=False)



# pandas 2

df = pd.read_excel("imiona.xlsx")

# a = df["Rok"].unique()
#
# b = df.groupby(["Rok"]).agg({"Liczba":["sum"]})
# b.plot(ylabel="Liczba urodzonych dzieci", xticks=a, rot=40, legend=True, title="Liczba urodzonych dzieci dla każdego roku")
# plt.subplots_adjust(left=0.15, right=0.9, bottom=0.15, top=0.9)
# plt.show()


# a = df.groupby(["Plec"]).agg({"Liczba": ["sum"]})
# a.plot(kind="bar", ylabel="Liczba urodzeń", legend=True, rot=0, title="Liczba urodzonych chłopców i dziewczynek")
# plt.show()

# a = df[df['Rok'] > 2012].groupby(['Plec']).agg({'Liczba':['sum']})
# a.plot(kind="pie", subplots=True, autopct='%.2f %%', fontsize=15, legend=True)
# plt.show()

# df = pd.read_csv("zamowienia.csv", delimiter=";")
# a = df["Sprzedawca"].unique()
# b = df.groupby('Sprzedawca').size()
# b.plot(kind="bar", ylabel="liczba zamówień", rot=40, title='Ilość zamówień sprzedawców')
# plt.subplots_adjust(left=0.1, right=0.9, bottom=0.2, top=0.9)
# plt.show()


# matplotlib

# x = np.arange(1, 21)
# y = 1/x
# plt.plot(x, y, label="f(x)=1/x")
# plt.xlabel("x")
# plt.ylabel("f(x)")
# plt.title("Wykres funkcji f(x) = 1/x dla x[1,20]")
# plt.legend()
# plt.axis([0, 20, 0, 1])
# plt.show()

# x = np.arange(1, 21)
# y = 1/x
# plt.plot(x, y,"g>:", label="f(x)=1/x")
# plt.xlabel("x")
# plt.ylabel("f(x)")
# plt.title("Wykres funkcji f(x) = 1/x dla x[1,20]")
# plt.legend()
# plt.axis([0, 20, 0, 1])
# plt.show()

# x = np.arange(0, 30, .1)
# plt.plot(x, np.sin(x), 'b', label='sin(x)')
# plt.plot(x, np.cos(x), 'r', label='cos(x)')
# plt.xlabel('x')
# plt.ylabel('sin(x) cos(x)')
# plt.legend(loc='upper right')
# plt.title('Wykres sin(x), cos(x)')
# plt.axis([0, 30, -1, 1])
# plt.show()

#
# df = pd.read_csv('iris.data', header=None, sep=',', decimal='.')
# print(df)
# colors = np.random.randint(0, 50, len(df.index))
# scale = np.abs(df[0] - df[1])
# plt.scatter(df[0], df[1], c=colors, s=scale)
# plt.xlabel('sepal length')
# plt.ylabel('sepal width')
# plt.show()


# df = pd.read_excel("imiona.xlsx", header=0)
# print(df)
# plt.subplot(1, 3, 1)
#
# grouped = df.groupby('Plec')
# etykiety = list(grouped.groups.keys())
# wartosci = list(grouped.agg('Liczba').sum())
# plt.bar(x=etykiety, height=wartosci, color=['green', 'red'])
# plt.xlabel('Płeć')
# plt.ylabel('Liczba narodzonych dzieci')
# # wykres 2
# plt.subplot(1, 3, 2)
# x = df['Rok'].unique()
# kobiety = df[(df.Plec == 'K')].groupby('Rok').agg({'Liczba':['sum']}).values
# mezczyzni = df[(df.Plec == 'M')].groupby('Rok').agg({'Liczba':['sum']}).values
# plt.plot(x, kobiety, label="Kobiety")
# plt.plot(x, mezczyzni, label="Mężczyźni")
# plt.xlabel('Rok')
# #
# # # wykres 3
# plt.subplot(1, 3, 3)
# x = df['Rok'].unique()
# y = df.groupby('Rok').agg('Liczba').sum()
# plt.bar(x, y)
# plt.xlabel('Rok')
# # wyświetlamy cały wykres
# plt.subplots_adjust(wspace=0.85)
# plt.show()


# df = pd.read_csv('zamowienia.csv', sep=';')
# x = df.groupby('Sprzedawca')['Utarg'].sum()
# print(x)

# explode = [0.0 for n in range(len(x.index))]
# explode[1] = 0.2
# plt.pie(x=x, labels=x.index, autopct=lambda pct: "{:.2f}%".format(pct), explode=explode, shadow=True)
# plt.title("Procentowy udział kwot zamówień sprzedawców")
# plt.show()