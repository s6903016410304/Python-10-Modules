def calculate_statistics(students):
    scores = [student.score for student in students]

    if not scores:
        return {
            "average": 0,
            "highest": 0,
            "lowest": 0,
            "passed": 0,
            "failed": 0,
        }

    return {
        "average": sum(scores) / len(scores),
        "highest": max(scores),
        "lowest": min(scores),
        "passed": sum(score >= 50 for score in scores),
        "failed": sum(score < 50 for score in scores),
    }

def show_statistics(stats):
    print(f"คะแนนเฉลี่ย : {stats['average']:.2f}")
    print(f"คะแนนสูงสุด : {stats['highest']}")
    print(f"คะแนนต่ำสุด : {stats['lowest']}")
    print(f"จำนวนคนผ่าน : {stats['passed']}")
    print(f"จำนวนคนไม่ผ่าน : {stats['failed']}")
