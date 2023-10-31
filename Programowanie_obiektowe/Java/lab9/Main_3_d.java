package pl.uwm.wmii.lab9;

import java.util.Scanner;

import static java.lang.Math.sqrt;

public class Main_3_d {
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        int ile = scan.nextInt();
        int wynik = 0;
        int[] tab = new int[ile];
        for(int i=0; i<ile; i++)
        {
            int liczba = scan.nextInt();
            tab[i] = liczba;
        }
        if(tab.length >=3)
        {
            for(int i=1; i+1<ile; i++)
            {
                if(tab[i] <(tab[i-1]+tab[i+1])/2)
                {
                    wynik++;
                }
            }
        }
        System.out.println(wynik);
    }
}