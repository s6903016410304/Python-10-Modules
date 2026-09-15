def add_sample_students(students):
    # ในโปรแกรมจริงสามารถเปลี่ยนเป็นรับข้อมูลจากผู้ใช้ได้
    return students

def show_students(students):
    if not students:
        print("ไม่พบข้อมูล")
        return

    print("ID   | ชื่อ | คะแนน | เกรด")
    print("-" * 35)
    for student in students:
        print(student)
