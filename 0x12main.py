# Student Grading System with Report Generator

print("Student Grading System")

students = []

# Collect student data
while True:
    name = input("")

    if name.lower() == "done":
        break

    score = int(input(""))

    # Assign grade
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

    students.append((name, score, grade))

# Match expected spacing
print("")
print("--- Final Report ---")

# Print report (no extra message if empty)
for name, score, grade in students:
    print(f"{name}: {score} - Grade {grade}")
