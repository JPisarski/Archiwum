package Zad3;

import java.util.*;

import static Zad3.It.print;

public class TestIt {
    public static void main(String[] args){
        ArrayList<String> a1 = new ArrayList<>();
        a1.add("Jeden");
        a1.add("Dwa");
        a1.add("Trzy");
        print(a1);
        LinkedList<Integer> a2 = new LinkedList<>();
        Integer b1 = Integer.valueOf(1);
        Integer b2 = Integer.valueOf(2);
        Integer b3 = Integer.valueOf(3);
        a2.add(b1);
        a2.add(b2);
        a2.add(b3);
        print(a2);
        HashSet<String> a3 = new HashSet<>();
        a3.add("11");
        a3.add("22");
        a3.add("33");
        print(a3);
        List<Integer> list = Arrays.asList(1, 2, 3, 4, 5);
        ArrayList<String> arrayList = new ArrayList<>(Arrays.asList("one", "two", "three"));
        LinkedList<Double> linkedList = new LinkedList<>(Arrays.asList(1.1, 2.2, 3.3));

        print(list); // 1, 2, 3, 4, 5,
        System.out.println();
        print(arrayList); // one, two, three,
        System.out.println();
        print(linkedList); // 1.1, 2.2, 3.3,
    }
}
