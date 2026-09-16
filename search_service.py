def search_by_name(students, keyword):
    keyword = keyword.casefold()
    return [student for student in students if keyword in student.name.casefold()]


def search_by_id(students, student_id):
    return [student for student in students if student.student_id == student_id]
