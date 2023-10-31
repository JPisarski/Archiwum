package pl.uwm.wmii.lab9;

import java.util.Scanner;

public class Main_6 {
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
        double max = tab[0];
        double min = tab[0];
        for(double el: tab)
        {
            if(el < min)
            {
                min = el;
            } else if (el > max)
            {
                max = el;
            }
        }
        System.out.printf("Min %f,  Max %f", min, max);
    }
}
