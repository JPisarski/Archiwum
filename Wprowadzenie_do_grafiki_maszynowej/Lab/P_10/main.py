from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageFilter
from PIL import ImageChops
from PIL import ImageOps
from PIL import ImageStat as stat


# zadanie 1

obraz = Image.open("pat.png")
w, h = obraz.size
s_w = 0.15
s_h = 0.27
resample_method = ['NEAREST', 'LANCZOS', 'BILINEAR', 'BICUBIC', 'BOX', 'HAMMING']
im_N = obraz.resize((int(w*s_w), int(h*s_h)), 0)
# plt.figure(figsize=(20, 16))
# i = 1
# for t in range(6):
#     file_name = "resample_" + str(resample_method[t])
#     im_r = obraz.resize((int(w*s_w), int(h*s_h)), t)
#     plt.subplot(6, 2, i)
#     plt.title(str(file_name))
#     plt.imshow(im_r)
#     plt.axis('off')
#     i += 1
#     diff = ImageChops.difference(im_N, im_r)
#     s = stat.Stat(diff)
#     plt.subplot(6, 2, i)
#     plt.title('srednia' + str(np.round(s.mean, 2)))
#     plt.imshow(diff)
#     plt.axis('off')
#     i += 1
#
# plt.subplots_adjust(wspace=0.5, hspace=0.7)
# plt.savefig("fig1.png")
# plt.show()

# zadanie 2

balwan = Image.open("balwan.png")

w, h = balwan.size
s_w = 1.5
s_h = 1.5
rekawica_lewa = balwan.resize((int((82-9) * s_w), int((325-245) * s_h)), box=(9, 245, 82, 325))
rekawica_prawa = balwan.resize((int((418-330) * s_w), int((260-188) * s_h)), box=(330, 188, 418, 260))
balwan1 = balwan.copy()
balwan1.paste(rekawica_lewa, (9, 245))
balwan1.paste(rekawica_prawa, (307, 183))
balwan1.save("balwan1.png")
# balwan1.show()

# zadanie 3

# a

a = obraz.rotate(60, expand=1, fillcolor=(255, 0, 0))

# b

b = obraz.rotate(60, fillcolor=(255, 0, 0))

# c

c = obraz.rotate(300, expand=1, fillcolor=(0, 255, 0))

# d

d = obraz.rotate(300, fillcolor=(0, 255, 0))

# e

plt.figure(figsize=(32, 16))
plt.subplot(2, 2, 1)
plt.imshow(a)
plt.axis('off')
plt.subplot(2, 2, 2)
plt.imshow(b)
plt.axis('off')
plt.subplot(2, 2, 3)
plt.imshow(c)
plt.axis('off')
plt.subplot(2, 2, 4)
plt.imshow(d)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig("fig4.png")
# plt.show()

# zadanie 4

w, h = obraz.size
obraz_nowy = Image.new('RGB', (2 * w, 2 * h), (255, 0, 0))
obraz_nowy.paste(obraz, (w, h))
obraz_nowy.rotate(30, expand=1, fillcolor=(0, 255, 0)).save("obraz_nowy.png")

# zadanie 5

obraz_1 = obraz.transpose(Image.TRANSPOSE)
obraz_2 = obraz.transpose(Image.FLIP_LEFT_RIGHT)
obraz_2 = obraz_2.rotate(90, expand=1)
obraz_3 = obraz.transpose(Image.TRANSVERSE)
obraz_4 = obraz.transpose(Image.FLIP_LEFT_RIGHT)
obraz_4 = obraz_4.rotate(270, expand=1)


plt.figure(figsize=(32, 16))
plt.subplot(2, 2, 1)
plt.imshow(obraz_1)
plt.axis('off')
plt.subplot(2, 2, 2)
plt.imshow(obraz_2)
plt.axis('off')
plt.subplot(2, 2, 3)
plt.imshow(obraz_3)
plt.axis('off')
plt.subplot(2, 2, 4)
plt.imshow(obraz_4)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig("fig5.png")
plt.show()
