package Zad2;

import java.time.LocalDate;

public class TestArrrayUtil {
    public static void main(String[] args){
        Integer a1 = Integer.valueOf(1);
        Integer a2 = Integer.valueOf(2);
        Integer a3 = Integer.valueOf(3);
        Integer[] tab1 = {a1, a2, a3};
        Integer[] tab2 = {a3, a2, a1};
        Integer[] tab3 = {a3, a3, a3};
        System.out.println(ArrayUtil.isSorted(tab1));
        System.out.println(ArrayUtil.isSorted(tab2));
        System.out.println(ArrayUtil.isSorted(tab3));
        LocalDate b1 = LocalDate.of(2007, 7, 17);
        LocalDate b2 = LocalDate.of(2008, 7, 17);
        LocalDate b3 = LocalDate.of(2008, 7, 18);
        LocalDate[] tab4 = {b1, b2, b3};
        LocalDate[] tab5 = {b3, b2, b1};
        LocalDate[] tab6 = {b3, b3, b3};
        System.out.println(ArrayUtil.isSorted(tab4));
        System.out.println(ArrayUtil.isSorted(tab5));
        System.out.println(ArrayUtil.isSorted(tab6));
    }
}
