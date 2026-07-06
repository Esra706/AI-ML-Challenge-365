

def grade_checker(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

# Testing the grade checker with different marks
test_scores = [95, 82, 71, 65, 40]

for score in test_scores:
    grade = grade_checker(score)
    print(f"Marks: {score} -> Grade: {grade}")


# Grade checker with pass/fail logic
marks = 55
if marks >= 40:
    print(f"\nMarks {marks}: PASS")
    if marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    elif marks >= 60:
        print("Grade: C")
    else:
        print("Grade: D")
else:
    print(f"\nMarks {marks}: FAIL")