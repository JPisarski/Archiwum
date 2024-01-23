package pl.uwm.wmii.lab10;

public class CarA {
    private String marka;
    private int rok;
    private int model;
    private int iloscDrzwi;
    private double pojemnoscSilnika;
    double srednieSpalanie;

    public String get_marka()
    {
        return this.marka;
    }
    public int get_rok()
    {
        return this.rok;
    }
    public int get_model()
    {
        return this.model;
    }
    public int get_iloscDrzwi()
    {
        return this.iloscDrzwi;
    }
    public double get_pojemnoscSilnika()
    {
        return this.pojemnoscSilnika;
    }
    public void setMarka(String value)
    {
        this.marka = value;
    }
    public void setRok(int value)
    {
        this.rok = value;
    }
    public void setModel(int value)
    {
        this.model = value;
    }
    public void setIloscDrzwi(int value)
    {
        this.iloscDrzwi = value;
    }
    public void setPojemnoscSilnika(double value)
    {
        this.pojemnoscSilnika = value;
    }
    private double ObliczSpalanie(double dlugoscTrasy)
    {
        return this.srednieSpalanie * dlugoscTrasy;
    }
    public double ObliczKosztPrzejazdu(double dlugoscTrasy, double cenaPaliwa)
    {
        return ObliczSpalanie(dlugoscTrasy) * cenaPaliwa;
    }
}
