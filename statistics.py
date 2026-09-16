def calculate_statistics(students):
    if not students:
        return {"average": 0, "highest": 0, "lowest": 0, "passed": 0, "failed": 0}
    scores = [student.score for student in students]
    return {
        "average": sum(scores) / len(scores),
        "highest": max(scores),
        "lowest": min(scores),
        "passed": sum(score >= 50 for score in scores),
        "failed": sum(score < 50 for score in scores),
    }


def show_statistics(stats):
    print(f"คะแนนเฉลี่ย : {stats['average']:.2f}")
    print(f"คะแนนสูงสุด : {stats['highest']:.2f}")
    print(f"คะแนนต่ำสุด : {stats['lowest']:.2f}")
    print(f"จำนวนคนผ่าน : {stats['passed']}")
    print(f"จำนวนคนไม่ผ่าน : {stats['failed']}")
