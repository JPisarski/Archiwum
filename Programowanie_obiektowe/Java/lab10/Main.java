package pl.uwm.wmii.lab10;

public class Main {
    public static void main(String[] args)
    {
        String carName = "Mój samochód";
        System.out.println(carName);
        CarA car1 = new CarA();
        car1.setMarka("Fiat");
        car1.setRok(2020);
        System.out.printf("%S, %d %n", car1.get_marka(), car1.get_rok());
        /*CarA car2 = new CarA();
        car2.setMarka("Opel");
        car2.setRok(2021);
        System.out.printf("%S, %d %n", car2.get_marka(), car2.get_rok());
        car1 = car2;
        System.out.printf("%S, %d %n", car1.get_marka(), car1.get_rok());
        System.out.printf("%S, %d %n", car2.get_marka(), car2.get_rok()); */
        CarB car_3 = new CarB();
        CarB car_4 = new CarB(25.5, "Fiat");
        CarB car_5 = CarB.Create();
    }
}
