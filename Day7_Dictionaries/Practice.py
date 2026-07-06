

# Store student names and grades
grades = {
    "Isra": 95,
    "Ali": 82,
    "Sara": 78,
    "Bilal": 90
}

# Access a single student's grade
print("Isra's grade:", grades["Isra"])

# Loop through all students and print grades
print("\n--- All Grades ---")
for name, grade in grades.items():
    print(f"{name}: {grade}")

# Update a grade
grades["Sara"] = 85
print("\nUpdated Sara's grade:", grades["Sara"])

# Add a new student
grades["Ahmed"] = 88
print("After adding Ahmed:", grades)

# Safe check for a student that may not exist
print("\nChecking Zara:", grades.get("Zara", "Not found"))

# Find the highest scoring student
top_student = max(grades, key=grades.get)
print(f"\nTop student: {top_student} with {grades[top_student]} marks")

# Calculate average grade
average = sum(grades.values()) / len(grades)
print(f"Average grade: {average:.2f}")