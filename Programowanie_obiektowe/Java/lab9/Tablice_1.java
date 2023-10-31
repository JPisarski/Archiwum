package pl.uwm.wmii.lab9;

import java.util.Random;
import java.util.Scanner;

import static java.lang.Math.pow;

public class Tablice_1 {
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        int ile = scan.nextInt();
        int[] tab = new int[ile];
        Random r = new Random();
        for(int i=0; i<ile; i++)
        {
            tab[i] = r.nextInt(1999)-999;
        }
        int p = 0;
        int np = 0;
        for(int el: tab)
        {
            if(el % 2 == 0)
            {
                p++;
            }
            else
            {
                np++;
            }
        }
        int u = 0;
        int zero = 0;
        int d = 0;
        int sumu = 0;
        int sumd = 0;
        for(int el: tab)
        {
            if(el < 0)
            {
                u++;
                sumu += el;
            } else if (el > 0)
            {
                d++;
                sumd += el;
            }
            else
            {
                zero++;
            }
        }
        int max = tab[0];
        for(int el: tab)
        {
            if(el > max)
            {
                max = el;
            }
        }
        int ilemax = 0;
        for(int el: tab)
        {
            if(el == max)
            {
                ilemax++;
            }
        }
        int[] dld = new int[ile];
        int dl = 0;
        int index = 0;
        for(int k=0; k<ile; k++)
        {
            if (tab[k] > 0)
            {
                dl ++;
                if (k==ile-1)
                {
                    dld[index] = dl;
                }
            }
            else
            {
                dld[index] = dl;
                dl = 0;
                index += 1;
            }
        }
        int maxd = dld[0];
        for(int el: dld)
        {
            if(el > maxd)
            {
                maxd = el;
            }
        }


        System.out.printf("Parzyste: %d, Nieparzyste: %d %n", p, np);
        System.out.printf("Ujemne: %d, Dodatnie: %d, Zera: %d %n", u, d, zero);
        System.out.printf("Max: %d, Ilemax %d %n", max, ilemax);
        System.out.printf("Suma ujemnych: %d, Suma dodatnich %d %n", sumu, sumd);
        System.out.printf("Długość najdłuższego fragmentu tablicy, w którym wszystkie elementy są dodatnie: %d %n", maxd);
    }
}

