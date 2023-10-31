
def n_wyraz(wyraz_1, q, n):
    return wyraz_1*q**(n-1)


def suma_n_wyrazow_poczatkowych(wyraz_1, q, n):
    if q == 1:
        return wyraz_1 * n
    else:
        return wyraz_1*(1-q**n)/(1-q)

