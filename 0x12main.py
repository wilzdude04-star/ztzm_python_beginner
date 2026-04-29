# Student Grading System with Report Generator

print("=== Student Grading System ===")

# Store student data
students = []

# Loop to collect student data
while True:
    name = input("\nEnter student name (or type 'done' to finish): ")

    if name.lower() == "done":
        break

    # Input validation for score
    try:
        score = int(input(f"Enter {name}'s score: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    # Determine grade using conditionals
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    # Store data in dictionary
    student = {
        "name": name,
        "score": score,
        "grade": grade
    }

    students.append(student)

# Generate final report
print("\n--- Final Report ---")

if len(students) == 0:
    print("No student data available.")
else:
    for student in students:
        print(f"{student['name']}: {student['score']} - Grade {student['grade']}")
