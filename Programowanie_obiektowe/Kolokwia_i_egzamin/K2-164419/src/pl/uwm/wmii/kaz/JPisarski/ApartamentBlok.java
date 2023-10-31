package pl.uwm.wmii.kaz.JPisarski;

import java.time.LocalDate;
import java.util.Objects;

public class ApartamentBlok extends House {

    public ApartamentBlok(String address, int floors, LocalDate year, String ownerName, String type, boolean garage) {
        super(address, floors, year, ownerName);
        if(type.equals("")){
            this.type = "wieżowiec";
        }
        else{
            this.type = type;
        }
        this.garage = garage;
    }

    public String getType() {
        return this.type;
    }

    public boolean isGarage() {
        return this.garage;
    }

    public void setType(String type) {
        if(type.equals("")){
            this.type = "wieżowiec";
        }
        else{
            this.type = type;
        }
    }

    public void setGarage(boolean garage) {
        this.garage = garage;
    }

    @Override
    public String toString() {
        return this.getClass().getSimpleName()+ "\n" +
                "address= '" + this.getAddress() + "',\n" +
                "floors= " + this.getFloors() + ",\n" +
                "year= " + this.getYear().toString() + ",\n" +
                "ownerName= '" + this.getOwnerName() + "',\n" +
                "type= '" + this.type + "',\n" +
                "garage= " + String.valueOf(this.garage) + "\n";
    }

    @Override
    public void renovate(int x){
        super.renovate(x);
        if(this.getFloors() > 10){
            this.garage = true;
        }
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        ApartamentBlok that = (ApartamentBlok) o;
        return this.getOwnerName().equals(that.getOwnerName()) && this.getFloors() == that.getFloors()
                && this.garage == true && that.garage == true;
    }

    private String type;
    private boolean garage;
}
