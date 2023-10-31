package Zad3;

import java.util.Iterator;

public class It {
    public static <E> void print(Iterable<E> x){
        Iterator<E> iter = x.iterator();
        while(iter.hasNext()){
            System.out.print(iter.next());
            if(iter.hasNext()){
                System.out.print(", ");
            }
        }
        System.out.println();
    }
}
