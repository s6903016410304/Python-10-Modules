import os
import config
from models import Student

def load_students():
    # ตัวอย่างข้อมูลเริ่มต้น
    return [
        Student("001", "สมชาย", 85),
        Student("002", "สมหญิง", 72),
        Student("003", "วิชัย", 48),
        Student("004", "มานะ", 91),
        Student("005", "สุดา", 63),
    ]

def save_students(students):
    with open(config.DATA_FILE, "w", encoding="utf-8") as file:
        for student in students:
            file.write(f"{student.student_id},{student.name},{student.score},{student.grade}\n")
    print(f"บันทึกข้อมูลลง {config.DATA_FILE} แล้ว")
