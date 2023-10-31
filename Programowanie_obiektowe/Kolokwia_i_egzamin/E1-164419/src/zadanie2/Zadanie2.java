package zadanie2;

import java.time.LocalDate;

public class Zadanie2 {
    public static  <T> void print(T[] tab){
        for(int i=0; i< tab.length; i++){
            if(i<tab.length-1){
                System.out.print(tab[i] + ", ");
            }
            if(i == tab.length-1){
                System.out.print(tab[i] +"\n");
            }
        }
    }

    public static void main(String[] args){
        String[] tab1 = {"AAA", "BBB", "CCC"};
        Integer[] tab2 = {1, 2, 3};
        Double[] tab3 =  {5.5 , 6.6, 7.7};
        print(tab1);
        print(tab2);
        print(tab3);
    }
}
