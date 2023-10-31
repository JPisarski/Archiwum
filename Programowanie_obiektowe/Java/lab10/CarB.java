package pl.uwm.wmii.lab10;

public class CarB {
    private String marka;
    private double pojemnoscSilnika;
    public CarB()
    {

    }
    public CarB(double pojemonoscSilnika, String marka)
    {
        this.pojemnoscSilnika = pojemonoscSilnika;
        this.marka = marka;
    }
    public static CarB Create()
    {
        return new CarB();
    }

    static int iloscKol;
}
