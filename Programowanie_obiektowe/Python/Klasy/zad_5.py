
class Student:
    nazwa_ucznia: str
    klasa_ucznia: str
    student_id: int

    def __init__(self, nazwa_ucznia, klasa_ucznia, student_id) -> None:
        self.nazwa_ucznia = nazwa_ucznia
        self.klasa_ucznia = klasa_ucznia
        self.student_id = student_id


A = Student("Jan Kowalski", "5A", "90210")

print(A.nazwa_ucznia)
print(A.klasa_ucznia)
print(A.student_id)
