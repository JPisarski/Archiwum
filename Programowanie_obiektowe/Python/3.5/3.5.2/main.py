from module_adres import Adres


def main() -> None:
    a: Adres = Adres(5, "Lipowa", "Kraków", "90-209",  5)
    a.show()
    print(a.comes_before("92-110"))
    b: Adres = Adres(10, "Janowska", "Janowiec", "13-130")
    b.show()


if __name__ == "__main__":
    main()
