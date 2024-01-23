
class Adres:
    nr_domu: int = None
    ulica: str = ""
    nr_mieszkania: int = None
    miasto: str = ""
    kod: str = ""

    def __init__(self, nr_domu, ulica, miasto, kod, nr_mieszkania=None) -> None:
        self.nr_domu = nr_domu
        self.ulica = ulica
        self.nr_mieszkania = nr_mieszkania
        self.miasto = miasto
        self.kod = kod

    def show(self) -> None:
        if self.nr_mieszkania:
            print(f"{self.ulica} {self.nr_domu} {self.nr_mieszkania}")
        else:
            print(f"{self.ulica} {self.nr_domu}")
        print(f"{self.kod} {self.miasto}")

    def comes_before(self, other: str) -> bool:
        if self.kod < other:
            return True
        else:
            return False
