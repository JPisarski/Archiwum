package pl.uwm.wmii.lab9;

import java.util.Scanner;

public class Main_3_c {
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        int ile = scan.nextInt();
        int wynik = 0;
        for(int i=0; i<ile; i++)
        {
            int liczba = scan.nextInt();
            if(liczba % 2 != 0)
            {
                continue;
            }
            for(int j=0; j<=liczba/2; j++)
            {
                if(j*j == liczba)
                {
                    wynik += 1;
                    break;
                }
            }
        }
        System.out.println(wynik);
    }
}
