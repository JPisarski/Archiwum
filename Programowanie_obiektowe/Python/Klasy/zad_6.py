
class Student:
    nazwa_ucznia: str
    klasa_ucznia: str
    student_id: int

    def __init__(self, nazwa_ucznia="", klasa_ucznia="", student_id=0) -> None:
        self.nazwa_ucznia = nazwa_ucznia
        self.klasa_ucznia = klasa_ucznia
        self.student_id = student_id

    def student_data(self) -> None:
        print(self.student_id)
        if self.nazwa_ucznia != "":
            print(self.nazwa_ucznia)
        if self.klasa_ucznia != "":
            print(self.klasa_ucznia)


A = Student("Jan Kowalski", "5A", 90210)
A.student_data()
B = Student(student_id=99999)
B.student_data()
