from modul_punkt import Punkt, NamedPunkt


def main() -> None:
    a: Punkt = Punkt(0, 0)
    b: NamedPunkt = NamedPunkt(3, 4, "Punkcik")
    print(a.distance())
    print(b.distance())


if __name__ == "__main__":
    main()
