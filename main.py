import config
import models
import database
import validators
import student_service
import grade_service
import statistics
import search_service
import ui
import report

def main():
    ui.show_header(config.APP_NAME)

    students = database.load_students()
    students = student_service.add_sample_students(students)

    print("\n=== รายชื่อนักศึกษา ===")
    student_service.show_students(students)

    print("\n=== คำนวณเกรด ===")
    for student in students:
        student.grade = grade_service.calculate_grade(student.score)

    student_service.show_students(students)

    print("\n=== ตรวจสอบข้อมูล ===")
    for student in students:
        print(f"{student.name}: {'ผ่าน' if validators.validate_student(student) else 'ไม่ผ่าน'}")

    print("\n=== ค้นหานักศึกษา ===")
    result = search_service.search_by_name(students, "สมชาย")
    student_service.show_students(result)

    print("\n=== สถิติ ===")
    stats = statistics.calculate_statistics(students)
    statistics.show_statistics(stats)

    print("\n=== รายงาน ===")
    report.print_report(students, stats)

    database.save_students(students)
    ui.show_footer()

if __name__ == "__main__":
    main()
