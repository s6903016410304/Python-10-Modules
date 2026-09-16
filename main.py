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
    students = database.load_students()

    while True:
        ui.show_header(config.APP_NAME)
        ui.show_menu()
        choice = input("เลือกเมนู 1-10: ").strip()

        if choice == "1":
            ui.show_title("รายชื่อนักศึกษา")
            student_service.show_students(students)

        elif choice == "2":
            ui.show_title("เพิ่มนักศึกษา")
            student_id = input("รหัสนักศึกษา: ").strip()
            name = input("ชื่อนักศึกษา: ").strip()
            try:
                score = float(input("คะแนน (0-100): "))
            except ValueError:
                print("กรุณากรอกคะแนนเป็นตัวเลข")
                ui.pause()
                continue
            new_student = models.Student(student_id, name, score)
            if validators.validate_student(new_student):
                new_student.grade = grade_service.calculate_grade(score)
                students.append(new_student)
                print("เพิ่มนักศึกษาเรียบร้อยแล้ว")
            else:
                print("ข้อมูลไม่ถูกต้อง กรุณาตรวจสอบรหัส ชื่อ และคะแนน")

        elif choice == "3":
            ui.show_title("คำนวณเกรด")
            for student in students:
                student.grade = grade_service.calculate_grade(student.score)
            student_service.show_students(students)

        elif choice == "4":
            ui.show_title("ตรวจสอบข้อมูล")
            for student in students:
                result = validators.validate_student(student)
                print(f"{student.student_id} - {student.name}: {'ข้อมูลถูกต้อง' if result else 'ข้อมูลไม่ถูกต้อง'}")

        elif choice == "5":
            ui.show_title("ค้นหานักศึกษาจากชื่อ")
            keyword = input("พิมพ์ชื่อหรือบางส่วนของชื่อ: ").strip()
            if not keyword:
                print("กรุณาพิมพ์ชื่อที่ต้องการค้นหา")
            else:
                result = search_service.search_by_name(students, keyword)
                if result:
                    student_service.show_students(result)
                else:
                    print(f"ไม่พบชื่อที่มีคำว่า '{keyword}'")

        elif choice == "6":
            ui.show_title("ค้นหานักศึกษาจากรหัส")
            student_id = input("พิมพ์รหัสนักศึกษา: ").strip()
            result = search_service.search_by_id(students, student_id)
            if result:
                student_service.show_students(result)
            else:
                print(f"ไม่พบรหัสนักศึกษา '{student_id}'")

        elif choice == "7":
            ui.show_title("สถิติ")
            stats = statistics.calculate_statistics(students)
            statistics.show_statistics(stats)

        elif choice == "8":
            ui.show_title("รายงาน")
            for student in students:
                student.grade = grade_service.calculate_grade(student.score)
            stats = statistics.calculate_statistics(students)
            report.print_report(students, stats)

        elif choice == "9":
            ui.show_title("บันทึกข้อมูล")
            database.save_students(students)

        elif choice == "10":
            database.save_students(students)
            ui.show_title("ออกจากโปรแกรม")
            print("บันทึกข้อมูลเรียบร้อยแล้ว")
            print("ขอบคุณที่ใช้งาน")
            break

        else:
            print("กรุณาเลือกเมนูตั้งแต่ 1 ถึง 10")

        if choice != "10":
            ui.pause()


if __name__ == "__main__":
    main()
