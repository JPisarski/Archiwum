from vehicle import Vehicle
from car import Car


def main() -> None:
    v_1: Vehicle = Vehicle()
    print(v_1)
    v_2: Vehicle = Vehicle("123456", 10, 2020)
    print(v_2)
    print(v_1 == v_2)
    print(v_1.model)
    v_1.prod_year = 1990
    print(v_1)

    c_1: Car = Car()
    print(c_1)
    c_2: Car = Car("XYZ12345", 3, 2019, 20000., "czerwony", 3)
    print(c_2)
    print(c_1 == c_2)


if __name__ == "__main__":
    main()
