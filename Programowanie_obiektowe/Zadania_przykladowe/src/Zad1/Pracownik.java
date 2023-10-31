package Zad1;

import java.util.Date;
import java.util.GregorianCalendar;


class Pracownik implements Comparable, Cloneable
{
    public Pracownik(String nazwisko, double pobory)
    {
        this.nazwisko = nazwisko;
        this.pobory = pobory;
    }

    @Override
    public int compareTo(Object other) {
        if (this.pobory < ((Pracownik) other).pobory) {
            return -1;
        }
        if (this.pobory > ((Pracownik) other).pobory) {
            return 1;
        }
        return 0;
    }

    @Override
    public Pracownik clone() throws CloneNotSupportedException
    {
        Pracownik cloned = (Pracownik) super.clone();
        cloned.dataZatrudnienia = (Date)dataZatrudnienia.clone();
        return cloned;
    }

    public void setDataZatrudnienia(int year, int month, int day)
    {
        dataZatrudnienia = new GregorianCalendar(year, month - 1, day).getTime();
    }

    public void zwiekszPobory(double procent)
    {
        double podwyzka = pobory * procent / 100;
        pobory += podwyzka;
    }

    @Override
    public String toString()
    {
        return "Pracownik[nazwisko = " + nazwisko
                + ", pobory = " + pobory
                + ", dataZatrudnienia = " + dataZatrudnienia
                + "]";
    }

    private String nazwisko;
    private double pobory;
    private Date dataZatrudnienia = null;
}
