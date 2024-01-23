
class Car:
    wyd: float
    stan: float = 0.0
    pojemnosc: float

    def __init__(self, wyd: float, pojemnosc: float) -> None:
        self.wyd = wyd
        self.pojemnosc = pojemnosc

    def drive(self, x: float) -> None:
        self.stan -= 0.001*x/self.wyd

    def get_fuel_level(self) -> float:
        return self.stan

    def add_fuel(self, x: float) -> None:
        if x + self.stan > self.pojemnosc:
            print("Za mała pojemność")
        else:
            self.stan += x

