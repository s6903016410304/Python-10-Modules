import os
import config
from models import Student


def load_students():
    if not os.path.exists(config.DATA_FILE):
        return [
            Student("001", "สมชาย", 85, "A"),
            Student("002", "สมหญิง", 72, "B"),
            Student("003", "วิชัย", 48, "F"),
            Student("004", "มานะ", 91, "A"),
            Student("005", "สุดา", 63, "C"),
        ]

    students = []
    try:
        with open(config.DATA_FILE, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    student_id, name, score, grade = parts
                    students.append(Student(student_id, name, float(score), grade))
    except (ValueError, OSError):
        print("ไม่สามารถอ่านไฟล์ข้อมูลได้ จะใช้ข้อมูลตัวอย่างแทน")
        return [Student("001", "สมชาย", 85, "A"), Student("002", "สมหญิง", 72, "B"), Student("003", "วิชัย", 48, "F")]
    return students


def save_students(students):
    try:
        with open(config.DATA_FILE, "w", encoding="utf-8") as file:
            for student in students:
                file.write(f"{student.student_id},{student.name},{student.score},{student.grade}\n")
        print(f"บันทึกข้อมูลลง {config.DATA_FILE} สำเร็จ")
    except OSError:
        print("ไม่สามารถบันทึกข้อมูลได้")
