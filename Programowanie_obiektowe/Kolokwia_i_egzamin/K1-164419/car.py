from __future__ import annotations
from vehicle import Vehicle


class Car(Vehicle):
    __price: float
    __colour: str
    __extra_seats: int

    def __init__(self, reg: str = None, model: int = 0,
                 prod_year: int = 2022, price: float = 0.0, colour: str = None,
                 extra_seats: int = 0) -> None:
        super().__init__(reg, model, prod_year)
        self.__price = price
        if price < 0:
            self.__price = 0.0
        self.__colour = colour
        self.__extra_seats = extra_seats
        if extra_seats < 0:
            self.__extra_seats = 0

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if type(value) != float:
            raise ValueError("To nie jest liczba zmiennoprzecinkowa!")
        elif value < 0:
            raise ValueError("To nie może być liczba ujemna!")
        else:
            self.__price = value

    @property
    def colour(self) -> str:
        return self.__colour

    @colour.setter
    def colour(self, value: str) -> None:
        if type(value) != str:
            raise ValueError("To nie jest napis!")
        else:
            self.__colour = value

    @property
    def extra_seats(self) -> int:
        return self.__extra_seats

    @extra_seats.setter
    def extra_seats(self, value: int) -> None:
        if type(value) != int:
            raise ValueError("To nie jest liczba całkowita!")
        elif value < 0:
            raise ValueError("To nie może być liczba ujemna!")
        else:
            self.__extra_seats = value

    def drive(self) -> str:
        return super().drive() + f" Ma kolor {self.__colour}."

    def __eq__(self, other: Car) -> bool:
        if isinstance(other, Car):
            return self.model == other.model and self.__price == other.price
        else:
            return NotImplemented

    def __ne__(self, other: Car) -> bool:
        if isinstance(other, Car):
            return self.model != other.model or self.price != other.price
        else:
            return NotImplemented

    def __str__(self) -> str:
        if self.reg is None:
            return f"Pojazd wyprodukowany w roku: {self.prod_year}.\n" \
               f"Model: {self.model}.\n" \
                   f"Cena: {self.__price}.\n" \
                   f"Kolor: {self.__colour}.\n" \
                   f"Dodatkowe siedzenia: {self.__extra_seats}."
        else:
            return f"Pojazd wyprodukowany w roku: {self.prod_year}.\n" \
                   f"Model: {self.model}.\n" \
                   f"Rejestracja: {self.reg}.\n" \
                   f"Cena: {self.__price}.\n" \
                   f"Kolor: {self.__colour}.\n" \
                   f"Dodatkowe siedzenia: {self.__extra_seats}."
