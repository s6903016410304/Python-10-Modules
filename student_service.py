def show_students(students):
    if not students:
        print("ยังไม่มีข้อมูลนักศึกษา")
        return
    print("รหัส   | ชื่อ            | คะแนน | เกรด")
    print("-" * 48)
    for student in students:
        print(student)


def count_students(students):
    return len(students)
