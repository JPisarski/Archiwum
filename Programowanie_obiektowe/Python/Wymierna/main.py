from Wymierna.modul_wymierna import Wymierna


def main():
    a = Wymierna(50, 10)
    b = Wymierna(25, 25)
    print(a + b)
    print(a - b)
    print(a == b)
    print(a != b)
    print(a > b)
    print(a >= b)
    print(a < b)
    print(a <= b)
    print(a * b)
    print(a/b)


if __name__ == "__main__":
    main()
