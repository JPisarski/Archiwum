from modul_Car import Car


def main() -> None:
    my_car = Car(20, 40)
    my_car.add_fuel(30)
    my_car.drive(100)
    print(my_car.get_fuel_level())


if __name__ == "__main__":
    main()
