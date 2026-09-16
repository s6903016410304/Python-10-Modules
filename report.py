def print_report(students, stats):
    if not students:
        print("ไม่มีข้อมูลสำหรับสร้างรายงาน")
        return
    print("รายงานผลการเรียน")
    print("-" * 60)
    for student in students:
        status = "ผ่าน" if student.score >= 50 else "ไม่ผ่าน"
        print(f"{student.student_id} | {student.name} | {student.score:.1f} | เกรด {student.grade} | {status}")
    print("-" * 60)
    print(f"นักศึกษาทั้งหมด : {len(students)} คน")
    print(f"คะแนนเฉลี่ย      : {stats['average']:.2f}")
    print(f"ผ่าน             : {stats['passed']} คน")
    print(f"ไม่ผ่าน           : {stats['failed']} คน")
