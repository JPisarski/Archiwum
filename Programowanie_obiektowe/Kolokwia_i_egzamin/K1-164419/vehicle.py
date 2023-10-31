from __future__ import annotations


class Vehicle:
    __reg: str
    __model: int
    __prod_year: int

    def __init__(self, reg: str = None, model: int = 0,
                 prod_year: int = 2022) -> None:
        self.__reg = reg
        self.__model = model
        if model < 0:
            self.__model = 0
        self.__prod_year = prod_year
        if prod_year < 1900 or prod_year > 2022:
            self.__prod_year = 2022

    # nie wiem, czy dobrze zrozumiałem zadanie,
    # bo można też zrobić, gdy PRZYNAJMNIEJ 1 argument nie spełnia warunku:
    #     if model < 0 or prod_year < 1900 or prod_year > 2022:
    #         self.__model = 0
    #         self.__prod_year = 2022

    @property
    def reg(self) -> str:
        return self.__reg

    @reg.setter
    def reg(self, value: str) -> None:
        if type(value) != str:
            raise ValueError("To nie jest napis!")
        else:
            self.__reg = value

    @property
    def model(self) -> int:
        return self.__model

    @model.setter
    def model(self, value: int) -> None:
        if type(value) != int:
            raise ValueError("To nie jest liczba całkowita!")
        elif value < 0:
            raise ValueError("To nie może być liczba ujemna!")
        else:
            self.__model = value

    @property
    def prod_year(self) -> int:
        return self.__prod_year

    @prod_year.setter
    def prod_year(self, value: int) -> None:
        if type(value) != int:
            raise ValueError("To nie jest liczba całkowita")
        elif value < 1900 or value > 2022:
            raise ValueError("Nieprawidłowy rok!")
        else:
            self.__prod_year = value

    def brake(self) -> str:
        return "Zatrzymuję się"

    def drive(self) -> str:
        return f"Jadę świetnym pojazdem z roku {self.__prod_year}!"

    def __str__(self) -> str:
        if self.reg is None:
            return f"Pojazd wyprodukowany w roku: {self.__prod_year}.\n" \
               f"Model: {self.__model}."
        else:
            return f"Pojazd wyprodukowany w roku: {self.__prod_year}.\n" \
                   f"Model: {self.__model}.\n" \
                   f"Rejestracja: {self.__reg}."

    def __eq__(self, other: Vehicle) -> bool:
        if isinstance(other, Vehicle):
            return self.__model == other.__model \
                   and self.__prod_year == other.__prod_year
        else:
            return NotImplemented

    def __ne__(self, other: Vehicle) -> bool:
        if isinstance(other, Vehicle):
            return self.__model != other.__model \
                   or self.__prod_year != other.__prod_year
        else:
            return NotImplemented
