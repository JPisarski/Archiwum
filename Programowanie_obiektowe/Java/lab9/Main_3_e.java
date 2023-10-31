package pl.uwm.wmii.lab9;

import java.util.Scanner;
import static java.lang.Math.pow;

public class Main_3_e {
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
        for(int i=0; i<ile; i++)
        {
            int factorial = 1;
            for(int j=1; j<=i+1; j++)
            {
                factorial *= j;
            }

            if(pow(2, i+1) < tab[i] && tab [i] < factorial)
            {
                wynik++;
            }
        }
        System.out.println(wynik);
    }
}