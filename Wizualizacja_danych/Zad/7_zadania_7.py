import numpy as np

# #zadanie 1
#
# x = np.arange(4, 84, 4)
# print(x)
#
# #zadanie 2
# 
# x = np.array([5.0, 6.6, 7.5, 9.25])
# y = x.astype("int32")
# print(y)
#
# #zadanie 3
#
#
# def fun(n):
#     x = np.array([2**i for i in range(1, n*n+1)])
#     return x.reshape(n, n)
#
#
# print(fun(4))
#
# #zadanie 4
#
#
# def fun(x, y):
#     return np.logspace(1, y, num=y, base=x)
#
#
# print(fun(2, 4))
#
# #zadanie 5
#
# import random
#
# def fun(n):
#     y = []
#     for x in range(n):
#         y.append(random.randint(0, 100))
#     y.reverse()
#     x = np.diag(y, 2)
#     return x
#
#
# print(fun(3))
#
# #zadanie 6
#
# x = np.array([list("akslop"), list("irlwki"), list("łóbwał"), list("fwruak"),list("aksfzd"),list("yafgsy")])
# print(x)
#
# #zadanie 7
#
#
# def fun(n):
#     a = np.diag([2 for x in range(1, n + 1)])
#     p = 4
#     for i in range(1, n):
#         y = np. diag([p for x in range(1, n+1-i)], i)
#         z = np.diag([p for x in range(1, n + 1 - i)], -i)
#         a += z + y
#         p += 2
#     print(a)
#
#
# fun(3)
#
# #zadanie 8
#
#
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
#                 return y, z
#             else:
#                 x = tablica.shape[0]/2
#                 y = tablica[:, :int(x)]
#                 z = tablica[:, int(x):]
#                 return y, z
#     elif kierunek == "poziom":
#         if (len(tablica.shape) == 2 and tablica.shape[0] % 2 == 1) or len(tablica.shape) == 1:
#             print("Ilość wierszy nie pozwala na operację")
#         else:
#             x = tablica.shape[0]/2
#             y = tablica[:int(x)]
#             z = tablica[int(x):]
#             return y, z
#
#
# a = np.array([[4,4], [5,5]])
# print(fun(a, "pion"))

# #zadanie 9
#
# wyraz_1 = 10
# r = 10
# x = np.arange(wyraz_1, wyraz_1 + 24 * r + 1, r)
# y = x.reshape(5, 5)
# print(y)
#
