from modul_soda import SodaCan


def main() -> None:
    a: SodaCan = SodaCan(1, 1)
    print(a.get_volume())
    print(a.get_surface_area())


if __name__ == "__main__":
    main()

