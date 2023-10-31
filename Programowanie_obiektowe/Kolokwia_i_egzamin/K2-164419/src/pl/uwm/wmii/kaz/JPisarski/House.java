package pl.uwm.wmii.kaz.JPisarski;

import java.time.LocalDate;
import java.util.Objects;

public class House {

    public House(String address, int floors, LocalDate year, String ownerName){
        if(address.equals("")){
            this.address = "ul. Słoneczna 54, 10-710 Olsztyn";
        }
        else {
            this.address = address;
        }
        if(ownerName.equals("")){
            this.ownerName = "Domek Wydziałowy";
        }
        else{
            this.ownerName = ownerName;
        }
        if(floors <= 0){
            this.floors = 2;
        }
        else{
            this.floors = floors;
        }
        if(year.compareTo(LocalDate.now())>0){
            this.year = LocalDate.now();
        }
        else{
            this.year = year;
        }
    }

    public String getAddress() {
        return this.address;
    }

    public int getFloors() {
        return this.floors;
    }

    public LocalDate getYear() {
        return this.year;
    }

    public String getOwnerName() {
        return this.ownerName;
    }

    public void setAddress(String address) {
        if(address.equals("")){
            this.address = "ul. Słoneczna 54, 10-710 Olsztyn";
        }
        else {
            this.address = address;
        }
    }

    public void setFloors(int floors) {
        if(floors <= 0){
            this.floors = 2;
        }
        else{
            this.floors = floors;
        }
    }

    public void setYear(LocalDate year) {
        if(year.compareTo(LocalDate.now())>0){
            this.year = LocalDate.now();
        }
        else{
            this.year = year;
        }
    }

    public void setOwnerName(String ownerName) {
        if(ownerName.equals("")){
            this.ownerName = "Domek Wydziałowy";
        }
        else {
            this.ownerName = ownerName;
        }
    }

    @Override
    public String toString() {
        return "address= '" + this.address + "',\n" +
                "floors= " + this.floors + ",\n" +
                "year= " + this.year.toString() + ",\n" +
                "ownerName= '" + this.ownerName + "',\n" +
                this.getClass().getSimpleName() + "\n" ;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        House house = (House) o;
        return this.address.equals(house.address);
    }

    public void renovate(int x){
        this.floors += x;
        if(this.floors > 30){
            this.floors = 30;
        }
    }

    // w tej metodzie, nie wiem czy uwzględnić przypadek, że liczba pięter > 30 ?????
    public static void jakiLimit(House y){
        int roznica = 30 - y.floors;
        System.out.println("Ilość pięter: " + y.floors +", pozostało do pełnego limitu: " + roznica);
    }

    private String address;
    private int floors;
    private LocalDate year;
    private String ownerName;
}
