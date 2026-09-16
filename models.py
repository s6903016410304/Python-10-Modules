class Student:
    def __init__(self, student_id, name, score, grade=""):
        self.student_id = student_id
        self.name = name
        self.score = score
        self.grade = grade

    def __str__(self):
        return f"{self.student_id:<6} | {self.name:<15} | {self.score:>6.1f} | {self.grade:<4}"
