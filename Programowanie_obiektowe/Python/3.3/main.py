from typing import List


class Prostokat:
    a: float = 0
    b: float = 0

    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def pole(self) -> float:
        return self.a * self.b


prostokat_1: Prostokat = Prostokat(10, 10)
prostokat_2: Prostokat = Prostokat(20, 5)
x: List[Prostokat] = [prostokat_1, prostokat_2]
for p in x:
    print(p.pole())


def fun(a: Prostokat) -> None:
    print(f"Bok 1: {a.a}")
    print(f"Bok 2: {a.b}")
    print(f"Pole: {a.pole()}")


fun(prostokat_1)
fun(prostokat_2)
