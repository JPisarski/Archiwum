
class Student:
    imie: str = ""
    nazwisko: str = ""
    wynik: int = 0
    n: int = 0

    def __init__(self, imie: str, nazwisko: str) -> None:
        self.imie = imie
        self.nazwisko = nazwisko

    def get_name(self) -> str:
        return f"{self.imie} {self.nazwisko}"

    def add_quiz(self, x) -> None:
        self.wynik += x
        self.n += 1

    def get_total_score(self) -> int:
        return self.wynik

    def get_average_score(self) -> float:
        return self.wynik/self.n



