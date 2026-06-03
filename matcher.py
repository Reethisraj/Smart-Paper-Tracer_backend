from rapidfuzz import fuzz
import re


def compare_answers(answer_text, student_text):

    teacher_answers = re.findall(
        r'Answer:\s*(.*?)(?=Question\s+\d+\s+Baseline:|$)',
        answer_text,
        re.S
    )

    student_answers = re.findall(
        r'Q\d+\s+Answer\s+Extracted:\s*"(.*?)"',
        student_text,
        re.S
    )

    results = []
    total_score = 0

    count = min(
        len(teacher_answers),
        len(student_answers)
    )

    for i in range(count):

        teacher = teacher_answers[i].strip()
        student = student_answers[i].strip()

        score = fuzz.token_sort_ratio(
            teacher.lower(),
            student.lower()
        )

        total_score += score

        results.append({
            "question": f"Q{i+1}",
            "answer": teacher,
            "student": student,
            "score": round(score, 2)
        })

    overall = 0

    if count > 0:
        overall = round(
            total_score / count,
            2
        )

    return {
        "student_name": extract_name(student_text),
        "roll_no": extract_roll(student_text),
        "total_score": overall,
        "results": results
    }


def extract_name(text):
    match = re.search(
        r'Name:\s*([^|]+)',
        text
    )
    return match.group(1).strip() if match else "Unknown"


def extract_roll(text):
    match = re.search(
        r'Roll No:\s*([^|]+)',
        text
    )
    return match.group(1).strip() if match else "Unknown"
