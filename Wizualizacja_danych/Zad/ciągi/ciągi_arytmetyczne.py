
def n_wyraz(wyraz_1, r, n):
    return wyraz_1 + (n - 1) * r


def suma_n_wyrazow_poczatkowych(wyraz_1, r, n):
    return (wyraz_1+ n_wyraz(wyraz_1, r, n))*n/2



