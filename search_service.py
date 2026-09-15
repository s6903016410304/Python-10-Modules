def search_by_name(students, keyword):
    keyword = keyword.lower()
    return [
        student for student in students
        if keyword in student.name.lower()
    ]

def search_by_id(students, student_id):
    return [
        student for student in students
        if student.student_id == student_id
    ]
