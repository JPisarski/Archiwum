from modul_student import Student


def main() -> None:
    student_1 = Student("Jan", "Janowski")
    print(student_1.get_name())
    student_1.add_quiz(5)
    student_1.add_quiz(5)
    print(student_1.get_total_score())
    print(student_1.get_average_score())


if __name__ == "__main__":
    main()
