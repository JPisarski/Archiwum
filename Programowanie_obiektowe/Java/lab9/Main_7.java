package pl.uwm.wmii.lab9;

import java.util.Scanner;

public class Main_7 {
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        int ile = scan.nextInt();
        double[] tab = new double[ile];
        for(int i=0; i<ile; i++)
        {
            int liczba = scan.nextInt();
            tab[i] = liczba;
        }
        int wynik = 0;
        for(int j=0; j<ile-1; j++)
        {
            if(tab[j]>0 && tab[j+1] >0)
            {
                wynik++;
            }
        }
        System.out.println(wynik);
    }
}
