import numpy as np

# #zadanie 1
#
# x = np.array([1, 2, 3])
# y = np.array([4, 5, 6])
# z = x*y
# print(z)
#
# #zadanie 2
#
# x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# y = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
# print(x.min(0))
# print(x.min(1))
# print(y.min(0))
# print(y.min(1))
#
# #zadanie 3
# 
# x = np.array([1, 2, 3])
# y = np.array([4, 5, 6])
# z = np.dot(x, y)
# print(z)
#
# #zadanie 4
#
# x = np.array([1, 2, 3])
# y = np.array([4.5, 5.5, 6.5])
# z = x*y
# print(z)
#
# #zadanie 5
#
# x = np.array([[1, 2, 3], [4, 5, 6]])
# a = np.sin(x)
# print(a)
#
# # zadanie 6
#
# x = np.array([[5, 6, 7], [8, 9, 10]])
# b = np.cos(x)
# print(b)
#
# #zadanie 7
#
# x = np.array([[1, 2, 3], [4, 5, 6]])
# a = np.sin(x)
# y = np.array([[5, 6, 7], [8, 9, 10]])
# b = np.cos(y)
# c = a + b
# print(c)
#
# # zadanie 8
#
# x = np.array([[3, 3, 3], [4, 4, 4], [5, 5, 5]])
# for z in x:
#     print(z)
#
# #zadanie 9
#
# x = np.array([[3, 3, 3], [4, 4, 4], [5, 5, 5]])
# for z in x.flat:
#     print(z)
#
# #zadanie 10
# 
# x = np.arange(81).reshape(9, 9)
# print(x)
# a = x.reshape(81, 1)
# print(a)
# b = x.reshape(1, 81)
# print(b)
# c = x.reshape(3, 27)
# print(c)
# d = x.reshape(27, 3)
# print(d)
#
# #zadanie 11
#
# x = np.arange(12)
# print(x)
# a = x.reshape(3, 4)
# print(a)
# b = a.reshape(4,3)
# print(b)
# c = x.reshape(2, 6)
# print(c)
# print(x.flatten())
# print(a.flatten())
# print(b.flatten())
# print(c.flatten())
