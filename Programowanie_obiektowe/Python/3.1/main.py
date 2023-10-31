

class Dane:
    imie: str = ""
    nazwisko: str = ""

    def __init__(self, imie: str, nazwisko: str) -> None:
        self.imie = imie
        self.nazwisko = nazwisko


osoba_1: Dane = Dane("Jakub", "Pisarski")
osoba_2: Dane = Dane("Jan", "Kowalski")

print(osoba_1.nazwisko)
print(osoba_2.nazwisko)
