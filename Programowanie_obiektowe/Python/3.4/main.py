from typing import List


class Stat:

    x: List[float] = []

    def __init__(self, x: List[float]) -> None:
        self.x = x

    def suma(self) -> float:
        return sum(self.x)

    def minimun(self) -> float:
        return min(self.x)

    def maximum(self) -> float:
        return max(self.x)


przyklad: Stat = Stat([5, 25, 50, 100])
print(przyklad.suma())
print(przyklad.minimun())
print(przyklad.maximum())

