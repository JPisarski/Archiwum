package Zad1;

public class TestPracownik {
    public static void main(String[] args)
    {
        try {
            Pracownik original = new Pracownik("John Q. Public", 50000);
            original.setDataZatrudnienia(2000, 1, 1);
            Pracownik copy = original.clone();
            copy.zwiekszPobory(10);
            copy.setDataZatrudnienia(2002, 12, 31);
            System.out.println();
            System.out.println("oryginał: " + original);
            System.out.println("kopia:    " + copy);
            System.out.println();
        } catch (CloneNotSupportedException e) {
            e.printStackTrace();
        }
        Pracownik p1 = new Pracownik("Jan Nowak", 50000);
        Pracownik p2 = new Pracownik("Adam Kowalski", 100000);
        System.out.println(p2.compareTo(p1));
    }
}

