import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from PIL import ImageStat as stat

obraz = Image.open("obraz9.jpg")
x = stat.Stat(obraz)
print(x.mean)
