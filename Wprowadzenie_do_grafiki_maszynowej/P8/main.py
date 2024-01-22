import numpy as np
from PIL import Image
from PIL import ImageFilter
from PIL import ImageChops
import matplotlib.pyplot as plt

#

obraz = Image.open("obraz.jpg")

# zadanie 1


def filtruj(obraz, kernel, scale):
    tab = np.array(obraz)
    tab1 = np.copy(tab)
    w, h, z = tab.shape
    k = kernel.shape[0]
    d = int(k / 2)
    for m in range(d, w-d):
        for n in range(d, h-d):
            for o in range(3):
                p = 0
                for a in range(k):
                    for b in range(k):
                        p += (tab[m - d + a, n - d + b, o] * kernel[a, b])
                p /= scale
                tab1[m, n, o] = p
    return Image.fromarray(tab1)


# zadanie 2

# a

obraz1 = obraz.filter(ImageFilter.BLUR)

# b

dane = ImageFilter.BLUR.filterargs
print(dane)
kernel = np.array(dane[3]).reshape(dane[0])
scale = dane[1]
obraz2 = filtruj(obraz, kernel, scale)

# c

plt.figure(figsize=(32, 16))
plt.subplot(1, 4, 1)
plt.imshow(obraz)
plt.axis('off')
plt.subplot(1, 4, 2)
plt.imshow(obraz1)
plt.axis('off')
plt.subplot(1, 4, 3)
plt.imshow(obraz2)
plt.axis('off')
plt.subplot(1, 4, 4)
plt.imshow(ImageChops.difference(obraz1, obraz2))
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig("fig1.png")

# zadanie 3

obrazsz = obraz.convert("L")

# a

obrazsz1 = obrazsz.filter(ImageFilter.EMBOSS)

# b

dane1 = ImageFilter.EMBOSS.filterargs
print(dane1)
ImageFilter.EMBOSS.filterargs = ((3, 3), 1, 128, (-1, 0, 1, -2, 0, 2, -1, 0, 1))
obrazsobel1 = obrazsz.filter(ImageFilter.EMBOSS)
ImageFilter.EMBOSS.filterargs = ((3, 3), 1, 128, (-1, -2, -1, 0, 0, 0, 1, 2, 1))
obrazsobel2 = obrazsz.filter(ImageFilter.EMBOSS)


# c

plt.figure(figsize=(32, 16))
plt.subplot(1, 4, 1)
plt.imshow(obrazsz, "gray")
plt.axis('off')
plt.subplot(1, 4, 2)
plt.imshow(obrazsz1, "gray")
plt.axis('off')
plt.subplot(1, 4, 3)
plt.imshow(obrazsobel1, "gray")
plt.axis('off')
plt.subplot(1, 4, 4)
plt.imshow(obrazsobel2, "gray")
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig("fig2.png")

# zadanie 4


obraz2f = obraz.filter(ImageFilter.DETAIL)
obraz4f = obraz.filter(ImageFilter.EDGE_ENHANCE_MORE)
obraz6f = obraz.filter(ImageFilter.SHARPEN)
obraz8f = obraz.filter(ImageFilter.SMOOTH_MORE)

plt.figure(figsize=(32, 16))
plt.subplot(4, 2, 1)
plt.title("DETAIL")
plt.imshow(obraz2f)
plt.axis('off')
plt.subplot(4, 2, 2)
plt.title("porówanienie z obrazem oryginalnym")
plt.imshow(ImageChops.difference(obraz, obraz2f))
plt.axis('off')
plt.subplot(4, 2, 3)
plt.title("EDGE_ENHANCE_MORE")
plt.imshow(obraz4f)
plt.axis('off')
plt.subplot(4, 2, 4)
plt.title("porówanienie z obrazem oryginalnym")
plt.imshow(ImageChops.difference(obraz, obraz4f))
plt.axis('off')
plt.subplot(4, 2, 5)
plt.title("SHARPEN")
plt.imshow(obraz6f)
plt.axis('off')
plt.subplot(4, 2, 6)
plt.title("porówanienie z obrazem oryginalnym")
plt.imshow(ImageChops.difference(obraz, obraz6f))
plt.axis('off')
plt.subplot(4, 2, 7)
plt.title("SMOOTH_MORE")
plt.imshow(obraz8f)
plt.axis('off')
plt.subplot(4, 2, 8)
plt.title("porówanienie z obrazem oryginalnym")
plt.imshow(ImageChops.difference(obraz, obraz8f))
plt.axis('off')
plt.subplots_adjust(wspace=0.025, hspace=0.25)
plt.savefig("fig3.png")

# zadanie 5

obraz12f = obraz.filter(ImageFilter.GaussianBlur(radius=5))
obraz13f = obraz.filter(ImageFilter.UnsharpMask(radius=5, percent=200, threshold=5))
obraz16f = obraz.filter(ImageFilter.MedianFilter(size=3))
obraz17f = obraz.filter(ImageFilter.MinFilter(size=3))
obraz18f = obraz.filter(ImageFilter.MaxFilter(size=3))

plt.figure(figsize=(32, 16))
plt.subplot(5, 2, 1)
plt.title("GaussianBlur - radius=5")
plt.imshow(obraz12f)
plt.axis('off')
plt.subplot(5, 2, 2)
plt.title("porówanienie z obrazem oryginalnym")
plt.imshow(ImageChops.difference(obraz, obraz12f))
plt.axis('off')
plt.subplot(5, 2, 3)
plt.title("UnsharpMask - radius=5, percent=200, threshold=5")
plt.imshow(obraz13f)
plt.axis('off')
plt.subplot(5, 2, 4)
plt.title("porówanienie z obrazem oryginalnym")
plt.imshow(ImageChops.difference(obraz, obraz13f))
plt.axis('off')
plt.subplot(5, 2, 5)
plt.title("MedianFilter - size=3")
plt.imshow(obraz16f)
plt.axis('off')
plt.subplot(5, 2, 6)
plt.title("porówanienie z obrazem oryginalnym")
plt.imshow(ImageChops.difference(obraz, obraz16f))
plt.axis('off')
plt.subplot(5, 2, 7)
plt.title("MinFilter - size=3")
plt.imshow(obraz17f)
plt.axis('off')
plt.subplot(5, 2, 8)
plt.title("porówanienie z obrazem oryginalnym")
plt.imshow(ImageChops.difference(obraz, obraz17f))
plt.axis('off')
plt.subplot(5, 2, 9)
plt.title("MaxFilter - size=3")
plt.imshow(obraz18f)
plt.axis('off')
plt.subplot(5, 2, 10)
plt.title("porówanienie z obrazem oryginalnym")
plt.imshow(ImageChops.difference(obraz, obraz18f))
plt.axis('off')
plt.subplots_adjust(wspace=0.025, hspace=0.25)
plt.savefig("fig4.png")

