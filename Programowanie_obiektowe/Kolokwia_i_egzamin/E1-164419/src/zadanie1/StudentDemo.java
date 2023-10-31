package zadanie1;

import java.util.ArrayList;
import java.util.Comparator;

public class StudentDemo {
    public static void main(String[] args) throws CloneNotSupportedException {
        Person p = new Student("Fred", 1729);
        System.out.println(p.getName());
        Student s = (Student) p;
        System.out.println(s.getName());
//
        Named n = s;
        System.out.println(n.getName());

        Student d = s.clone();
        System.out.println(d.getName());
        System.out.println(d);

        ArrayList<Student> studenci = new ArrayList<>();
        studenci.add(new Student("Zenon", 1729));
        studenci.add(new Student("Andrzej", 1729));
        studenci.add(new Student("Kamil", 1729));

        studenci.sort(new NamesComparator());

        System.out.println();
        for (Student e : studenci) {
            System.out.println("nazwisko = " + e.getName() + ", id = " + e.getId());
        }
        System.out.println();



    }
}

class NamesComparator implements Comparator<Student> {
    public int compare(Student s1, Student s2){
        return s1.getName().compareTo(s2.getName());
    }

}
