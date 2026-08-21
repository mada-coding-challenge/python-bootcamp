import json

from pathlib import Path


# ============================================================
#              PYTHON JSON - GUIDED PRACTICE
# ============================================================
#
# Topic:
# JSON Data Management
#
# Concepts:
# - json.dump()
# - json.load()
# - pathlib.Path
# - Creating directories
# - Reading JSON files
# - Writing JSON files
# - Exception handling
# - Custom exceptions
# - Data validation
# ============================================================


# ============================================================
# >>>>>>>>>>>>>>>>>>>>> EXERCISE 1 <<<<<<<<<<<<<<<<<<<<<<<<<<<
# ============================================================
#
# CREATE STUDENT DATA
#
# Create a list containing student dictionaries.
#
# Each student should have:
# - name
# - score
#
# Students:
# Sara -> 92
# Ali  -> 85
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 1: CREATE STUDENT DATA")
print("=" * 60)

students = [
    {
        "name": "Sara",
        "score": 92
    },
    {
        "name": "Ali",
        "score": 85
    }
]

print("Student data:")
print(students)


# ============================================================
# >>>>>>>>>>>>>>>>>>>>> EXERCISE 2 <<<<<<<<<<<<<<<<<<<<<<<<<<<
# ============================================================
#
# CREATE A DATA DIRECTORY
#
# Create a directory called "data".
#
# Then create a path for:
#
# data/students.json
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 2: CREATE DATA DIRECTORY")
print("=" * 60)

data_dir = Path("data")

data_dir.mkdir(exist_ok=True)

data_file = data_dir / "students.json"

print("Directory:", data_dir)
print("JSON file:", data_file)


# ============================================================
# >>>>>>>>>>>>>>>>>>>>> EXERCISE 3 <<<<<<<<<<<<<<<<<<<<<<<<<<<
# ============================================================
#
# WRITE DATA TO JSON
#
# Save the students list into students.json.
#
# Use:
# - json.dump()
# - indent=2
# - UTF-8 encoding
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 3: WRITE JSON FILE")
print("=" * 60)

with data_file.open("w", encoding="utf-8") as file:
    json.dump(students, file, indent=2)

print("Student data saved successfully.")
print("File:", data_file)


# ============================================================
# >>>>>>>>>>>>>>>>>>>>> EXERCISE 4 <<<<<<<<<<<<<<<<<<<<<<<<<<<
# ============================================================
#
# READ DATA FROM JSON
#
# Read students.json using json.load().
#
# Store the result in a variable called "loaded".
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 4: READ JSON FILE")
print("=" * 60)

try:
    with data_file.open("r", encoding="utf-8") as file:
        loaded = json.load(file)

    print("Student data loaded successfully.")
    print(loaded)

except FileNotFoundError:
    print("Student file not found.")

except PermissionError:
    print("Student file cannot be read.")

except json.JSONDecodeError:
    print("The JSON file is invalid.")


# ============================================================
# >>>>>>>>>>>>>>>>>>>>> EXERCISE 5 <<<<<<<<<<<<<<<<<<<<<<<<<<<
# ============================================================
#
# CREATE A CUSTOM EXCEPTION
#
# Create a custom exception called:
#
# InvalidStudentError
#
# This exception will be used when student data is invalid.
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 5: CUSTOM EXCEPTION")
print("=" * 60)


class InvalidStudentError(Exception):
    pass


print("InvalidStudentError created successfully.")


# ============================================================
# >>>>>>>>>>>>>>>>>>>>> EXERCISE 6 <<<<<<<<<<<<<<<<<<<<<<<<<<<
# ============================================================
#
# VALIDATE STUDENT DATA
#
# Create a function called validate_student().
#
# A student is invalid when:
#
# - name is empty
# - score is less than 0
#
# Valid students should be printed.
#
# Invalid students should raise InvalidStudentError.
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 6: VALIDATE STUDENTS")
print("=" * 60)


def validate_student(students):
    for student in students:

        if student["name"] == "":
            raise InvalidStudentError("Student name is missing.")

        if student["score"] < 0:
            raise InvalidStudentError(
                f"Invalid score for {student['name']}."
            )

        print(student)


# ============================================================
# >>>>>>>>>>>>>>>>>>>>> EXERCISE 7 <<<<<<<<<<<<<<<<<<<<<<<<<<<
# ============================================================
#
# RUN VALIDATION
#
# Call validate_student().
#
# Catch InvalidStudentError and display the error message.
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 7: RUN VALIDATION")
print("=" * 60)

try:
    validate_student(loaded)

except InvalidStudentError as error:
    print("Missing student:", error)


# ============================================================
# >>>>>>>>>>>>>>>>>>>>> EXERCISE 8 <<<<<<<<<<<<<<<<<<<<<<<<<<<
# ======================= FINAL PRACTICE ======================
# ============================================================
#
# Add another student and validate the complete list.
#
# Student:
# Lina -> 95
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 8: FINAL JSON PRACTICE")
print("=" * 60)

loaded.append(
    {
        "name": "Lina",
        "score": 95
    }
)

print("Updated students:")

try:
    validate_student(loaded)

except InvalidStudentError as error:
    print("Invalid student:", error)


# ============================================================
#                         COMPLETE
# ============================================================

print("\n" + "=" * 60)
print("ALL JSON GUIDED PRACTICE COMPLETED")
print("=" * 60)