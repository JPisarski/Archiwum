package pl.uwm.wmii.lab9;

import java.util.Scanner;

public class Main_3_b {
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        int ile = scan.nextInt();
        int wynik = 0;
        for(int i=0; i<ile; i++)
        {
            int liczba = scan.nextInt();
            if(liczba % 3 == 0 && liczba % 5 !=0)
            {
                wynik++;
            }
        }
        System.out.println(wynik);
    }
}
