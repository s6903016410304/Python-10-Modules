def validate_score(score):
    return isinstance(score, (int, float)) and 0 <= score <= 100

def validate_student(student):
    return (
        bool(student.student_id)
        and bool(student.name)
        and validate_score(student.score)
    )
