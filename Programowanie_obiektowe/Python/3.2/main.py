import random


class Coin:
    side: str = ""

    def throw(self) -> None:
        self.side = random.choice(["Orzeł", "Reszka"])

    def show_side(self) -> str:
        return self.side


pieniadz_1: Coin = Coin()
pieniadz_1.throw()
print(pieniadz_1.show_side())
pieniadz_2: Coin = Coin()
pieniadz_2.throw()
print(pieniadz_2.show_side())
