package pl.uwm.wmii.lab9;

import java.util.Scanner;

import static java.lang.Math.abs;
import static java.lang.Math.sqrt;

public class Main_1_c {
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        int ile = scan.nextInt();
        int wynik = 0;
        for(int i=0; i<ile; i++)
        {
            int liczba = scan.nextInt();
            wynik += sqrt(abs(liczba));
        }
        System.out.println(wynik);
    }

}
