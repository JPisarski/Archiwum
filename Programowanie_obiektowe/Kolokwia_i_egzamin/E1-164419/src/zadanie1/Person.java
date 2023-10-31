package zadanie1;

public abstract class Person implements Named{
    private String name;

    public Person(String name) { this.name = name; }
    public final String getName() { return name; }

    public abstract int getId();
}

