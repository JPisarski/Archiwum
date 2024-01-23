import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

obraz = Image.open("obraz11.jpg")


histogram = obraz.histogram()
plt.title("Histogram")
plt.bar(range(256), histogram[2 * 256:], color='b', alpha=0.3)
plt.savefig("hist.png")
plt.show()

print(histogram[2*256 + 50])