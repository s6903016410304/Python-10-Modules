def print_report(students, stats):
    print("สรุปรายงานนักศึกษา")
    print("-" * 35)

    for student in students:
        status = "ผ่าน" if student.score >= 50 else "ไม่ผ่าน"
        print(f"{student.name}: {student.score:.1f} คะแนน, เกรด {student.grade}, {status}")

    print("-" * 35)
    print(f"ค่าเฉลี่ยรวม: {stats['average']:.2f}")
