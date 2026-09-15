# Python 10 Modules Project

โปรแกรมตัวอย่างภาษา Python ที่มี **10 modules** และถูกเรียกใช้จาก `main.py`

## Modules

1. `config.py` - เก็บค่าตั้งค่าของโปรแกรม
2. `models.py` - สร้างคลาส Student
3. `database.py` - จัดการข้อมูลนักศึกษา
4. `validators.py` - ตรวจสอบข้อมูล
5. `student_service.py` - จัดการข้อมูลนักศึกษา
6. `grade_service.py` - คำนวณเกรด
7. `statistics.py` - คำนวณสถิติ
8. `search_service.py` - ค้นหานักศึกษา
9. `ui.py` - แสดงส่วนติดต่อผู้ใช้
10. `report.py` - สร้างรายงาน

## การทำงาน

`main.py` จะ import และเรียกใช้ทั้ง 10 modules

```text
main.py
 ├── config.py
 ├── models.py
 ├── database.py
 ├── validators.py
 ├── student_service.py
 ├── grade_service.py
 ├── statistics.py
 ├── search_service.py
 ├── ui.py
 └── report.py
```

## วิธีรัน

ต้องติดตั้ง Python 3 ก่อน จากนั้นเปิด Terminal ในโฟลเดอร์โปรเจกต์แล้วใช้

```bash
python main.py
```

โปรแกรมจะแสดงรายชื่อนักศึกษา คำนวณเกรด ค้นหาข้อมูล แสดงสถิติ และสร้างไฟล์ `students.txt`

## อัปโหลด GitHub

สร้าง Repository ใหม่บน GitHub แล้วเปิด Terminal ในโฟลเดอร์นี้:

```bash
git init
git add .
git commit -m "Create Python project with 10 modules"
git branch -M main
git remote add origin https://github.com/USERNAME/python-10-modules.git
git push -u origin main
```

เปลี่ยน `USERNAME` และชื่อ repository ให้ตรงกับ GitHub ของตัวเอง
