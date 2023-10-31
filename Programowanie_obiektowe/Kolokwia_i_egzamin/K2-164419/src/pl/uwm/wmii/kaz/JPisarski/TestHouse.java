package pl.uwm.wmii.kaz.JPisarski;

import java.time.LocalDate;

public class TestHouse {
    public static void main(String[] args){
        House h1 = new House("", -10 , LocalDate.of(2050,5,5), "");
        House h2 = new House("ul. 3 Maja 10, 90-210 Łódź", 25 , LocalDate.now(), "Pisarski");
        System.out.println(h1);
        System.out.println(h2);
        System.out.println(h2.getAddress());
        System.out.println(h2.getFloors());
        System.out.println(h2.getYear());
        System.out.println(h2.getOwnerName());
        h2.setAddress("");
        h2.setFloors(-100);
        h2.setYear(LocalDate.of(2100, 4, 4));
        h2.setOwnerName("");
        System.out.println(h2.getAddress());
        System.out.println(h2.getFloors());
        System.out.println(h2.getYear());
        System.out.println(h2.getOwnerName());
        h1.setAddress("ul. Krakowska 15, 12-134 Kraków");
        h1.setFloors(100);
        h1.setYear(LocalDate.now());
        h1.setOwnerName("Pisarski Jakub");
        System.out.println(h1.getAddress());
        System.out.println(h1.getFloors());
        System.out.println(h1.getYear());
        System.out.println(h1.getOwnerName());
        System.out.println(h1);
        System.out.println(h2);
        System.out.println(h1.equals(h2));
        h2.setAddress(h1.getAddress());
        System.out.println(h1.equals(h2));
        System.out.println(h1.getFloors());
        h1.renovate(10);
        System.out.println(h1.getFloors());
        House.jakiLimit(h1);
        ApartamentBlok a1 = new ApartamentBlok("", -10 , LocalDate.of(2050,5,5),
                "", "", true);
        System.out.println(a1);
        ApartamentBlok a2 = new ApartamentBlok("ul. 3 Maja 10, 90-210 Łódź", 25 , LocalDate.now(),
                "Pisarski", "wielorodzinny", false);
        System.out.println(a1.getType());
        System.out.println(a1.isGarage());
        a1.setGarage(false);
        a1.setType("hotel");
        System.out.println(a1.getType());
        System.out.println(a1.isGarage());
        a1.renovate(10);
        System.out.println(a1);
        System.out.println(a2);
        System.out.println(a1.equals(a2));
        ApartamentBlok a3 = new ApartamentBlok("ul. Biała 9, 12-112 Bielsko Biała", 12, LocalDate.now(),
                "Domek Wydziałowy", "wieżowiec", true);
        System.out.println(a1.equals(a3));
    }
}
