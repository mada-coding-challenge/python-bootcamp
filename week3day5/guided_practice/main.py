# Guided Practice — Student Score Report
from copy import deepcopy


# 1. Create a list of student dictionaries
students = [
    {"name": "Sara", "scores": [40, 50, 80]},
    {"name": "Omar", "scores": [90, 70, 60]}
]


# 2. Calculate each student's average using a list comprehension
students_average = [
    {
        "name": student["name"],
        "scores": student["scores"],
        "average": round(
            sum(student["scores"]) / len(student["scores"]),
            2
        )
    }
    for student in students
]


# 3. Keep only students whose average is at least 60
averaged_students = [
    student
    for student in students_average
    if student["average"] >= 60
]


# 4. Build a dictionary index using the student's name as the key
reported_students = {
    student["name"]: student
    for student in averaged_students
}


print("Report:")
print(reported_students)


# 5. Create an independent backup using deepcopy
backup = deepcopy(reported_students)


# Change a nested value in the original
reported_students["Omar"]["scores"][0] = 100


# Show that the original and backup are separate
print("\nAfter changing the original:")
print("Original:", reported_students)
print("Backup:", backup)