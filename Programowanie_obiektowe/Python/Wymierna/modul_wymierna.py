from __future__ import annotations


class Wymierna:
    licznik: float
    mianownik: float

        
    def __init__(self, p: float = 0.0, q: float = 1.0) -> None:
        self.licznik = p
        self.mianownik = q
        if gcd(self.licznik, self.mianownik) != 1:
            self.licznik //= gcd(p, q)
            self.mianownik //= gcd(p, q)

        if self.mianownik < 0:
            self.licznik *= -1
            self.mianownik *= -1
            
    def __init__(self, licznik: float = 0.0, mianownik: float = 1.0) -> None:
        self.licznik = licznik
        self.mianownik = mianownik

    def get_licznik(self) -> float:
        return self.licznik

    def get_mianownik(self) -> float:
        return self.mianownik

    def __repr__(self) -> str:
        return str(self.licznik/self.mianownik)

    def __float__(self) -> float:
        return self.licznik / self.mianownik

    def __add__(self, other: Wymierna) -> Wymierna:
        return Wymierna((self.licznik/self.mianownik)+(other.licznik/other.mianownik))

    def __sub__(self, other: Wymierna) -> Wymierna:
        return Wymierna((self.licznik/self.mianownik)-(other.licznik/other.mianownik))

    def __eq__(self, other: Wymierna) -> bool:
        if self.licznik/self.mianownik < other.licznik/other.mianownik or \
                self.licznik/self.mianownik > other.licznik/other.mianownik:
            return False
        else:
            return True

    def __ne__(self, other: Wymierna) -> bool:
        if self.licznik/self.mianownik != other.licznik/other.mianownik:
            return True
        else:
            return False

    def __lt__(self, other: Wymierna) -> bool:
        if self.licznik/self.mianownik < other.licznik/other.mianownik:
            return True
        else:
            return False

    def __le__(self, other: Wymierna) -> bool:
        if self.licznik/self.mianownik <= other.licznik/other.mianownik:
            return True
        else:
            return False

    def __gt__(self, other: Wymierna) -> bool:
        if self.licznik/self.mianownik > other.licznik/other.mianownik:
            return True
        else:
            return False

    def __ge__(self, other: Wymierna) -> bool:
        if self.licznik/self.mianownik >= other.licznik/other.mianownik:
            return True
        else:
            return False

    def __mul__(self, other: Wymierna) -> Wymierna:
        return Wymierna((self.licznik * other.licznik), (self.mianownik * other.mianownik))

    def __truediv__(self, other: Wymierna) -> Wymierna:
        return Wymierna((self.licznik * other.mianownik), (self.mianownik * other.licznik))





