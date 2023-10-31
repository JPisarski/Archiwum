package pl.uwm.wmii.lab9;

import java.util.Scanner;

public class Main_2 {
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        int ile = scan.nextInt();
        double[] tab = new double[ile];
        for(int i=0; i<ile; i++)
        {
            double liczba = scan.nextDouble();
            tab[i] = liczba;
        }
        for(int j=1; j<ile; j++)
        {
            System.out.println(tab[j]);
        }
        System.out.println(tab[0]);
    }
}
