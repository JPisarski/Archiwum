from math import pi


class SodaCan:

    h: float = None
    r: float = None

    def __init__(self, h: float, r: float) -> None:
        self.h = h
        self.r = r

    def get_surface_area(self) -> float:
        return 2 * pi * self.r**2 + 2 * pi * self.r * self.h

    def get_volume(self) -> float:
        return pi * self.r ** 2 * self.h

