from PIL import Image
import numpy as np

# zadanie dodatkowe


def wytnij_fragment_obrazu(obraz, m_p, n_p, m_k, n_k):
    tab = np.asarray(obraz) * 1
    tab_nowa = tab[n_p: n_k, m_p: m_k]
    tab_nowa = tab_nowa.astype(bool)
    return Image.fromarray(tab_nowa)


inicjaly = Image.open("inicjaly.bmp")
inicjaly_j = wytnij_fragment_obrazu(inicjaly, 20, 5, 46, 48)
inicjaly_j.show()
inicjaly_j.save("inicjal_j.bmp")
inicjaly_p = wytnij_fragment_obrazu(inicjaly, 47, 5, 70, 40)
inicjaly_p.show()
inicjaly_p.save("inicjal_p.bmp")

