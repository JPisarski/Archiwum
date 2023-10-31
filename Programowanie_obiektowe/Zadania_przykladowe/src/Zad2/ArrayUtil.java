package Zad2;

public class ArrayUtil {
    public static <T extends  Comparable<T>> boolean isSorted(T[] tab){
        for(int i=0; i<tab.length-1; i++){
            if(tab[i+1].compareTo(tab[i])<0){
                return false;
            }
        }
        return true;
    }
}
