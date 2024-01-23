
class Punkt:
    x: int = 0
    y: int = 0

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def distance(self):
        return (self.x**2 + self.y**2)**0.5


class NamedPunkt:
    x: int = 0
    y: int = 0
    nazwa: str = ""

    def __init__(self, x: int, y: int, nazwa: str) -> None:
        self.x = x
        self.y = y
        self.nazwa = nazwa

    def distance(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

