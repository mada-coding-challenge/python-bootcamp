# ============================================================
#              PYTHON DATA HANDLING EXERCISES
# ============================================================


# ============================================================
# >>>>>>>>>>>>>>>>>>>>> EXERCISE 1 <<<<<<<<<<<<<<<<<<<<<<<<<<<
# ============================================================
# Write data to a CSV file.
#
# Concepts:
# - csv module
# - csv.writer()
# - writerow()
# - Writing rows to a file
# ============================================================

import csv

print("\n" + "=" * 60)
print("EXERCISE 1: WRITE CSV FILE")
print("=" * 60)

with open("students.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "course"])
    writer.writerow(["Sara", "Python"])
    writer.writerow(["Ali", "Django"])

print("students.csv created successfully.")

with open("students.csv", "r", encoding="utf-8") as file:
    print("\nCSV content:")
    print(file.read())


# ============================================================
# >>>>>>>>>>>>>>>>>>>>> EXERCISE 2 <<<<<<<<<<<<<<<<<<<<<<<<<<<
# ============================================================
# Write and read JSON data.
#
# Concepts:
# - json.dump()
# - json.load()
# - JSON lists
# - JSON dictionaries
# ============================================================

import json

print("\n" + "=" * 60)
print("EXERCISE 2: WRITE AND READ JSON")
print("=" * 60)

students = [
    {"name": "Sara", "score": 92},
    {"name": "Ali", "score": 85}
]

with open("students.json", "w", encoding="utf-8") as file:
    json.dump(students, file, indent=2)

print("students.json created successfully.")

with open("students.json", "r", encoding="utf-8") as file:
    loaded = json.load(file)

print("First student:", loaded[0]["name"])


# ============================================================
# >>>>>>>>>>>>>>>>>>>>> EXERCISE 3 <<<<<<<<<<<<<<<<<<<<<<<<<<<
# ============================================================
# Handle invalid user input.
#
# Try converting user input into an integer.
#
# If the user enters something that is not a whole number,
# catch ValueError.
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 3: HANDLE INVALID INPUT")
print("=" * 60)

# Example without requiring user input:
score_input = "abc"

try:
    score = int(score_input)
    print("Score:", score)

except ValueError:
    print("Enter a whole number")
    print("Program continues")


# ============================================================
# >>>>>>>>>>>>>>>>>>>>> EXERCISE 4 <<<<<<<<<<<<<<<<<<<<<<<<<<<
# ============================================================
# Handle a missing file.
#
# Try to read students.txt.
#
# Catch:
# - FileNotFoundError
# - PermissionError
# ============================================================

from pathlib import Path

print("\n" + "=" * 60)
print("EXERCISE 4: HANDLE MISSING FILE")
print("=" * 60)

try:
    text = Path("students.txt").read_text(
        encoding="utf-8"
    )

    print(text)

except FileNotFoundError:
    print("Student file not found")

except PermissionError:
    print("Student file cannot be read")


# ============================================================
# >>>>>>>>>>>>>>>>>>>>> EXERCISE 5 <<<<<<<<<<<<<<<<<<<<<<<<<<<
# ============================================================
# Use try, except, else, and finally.
#
# Concepts:
# - try
# - except
# - else
# - finally
# - OSError
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 5: TRY / EXCEPT / ELSE / FINALLY")
print("=" * 60)

path = Path("students.txt")

# Create the file first so the example can demonstrate
# the successful "else" block.
path.write_text(
    "Sara\nAli\n",
    encoding="utf-8"
)

try:
    text = path.read_text(
        encoding="utf-8"
    )

except OSError as error:
    print("Load failed:", error)

else:
    print("File loaded successfully:")
    print(text)

finally:
    print("Load attempt finished")


# ============================================================
# >>>>>>>>>>>>>>>>>>>>> EXERCISE 6 <<<<<<<<<<<<<<<<<<<<<<<<<<<
# ============================================================
# Validate a score.
#
# A valid score must be between 0 and 100.
#
# If the score is outside this range, raise ValueError.
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 6: VALIDATE SCORE")
print("=" * 60)


def validate_score(score):
    if not 0 <= score <= 100:
        raise ValueError("Score must be 0 to 100")

    return score


try:
    score = validate_score(120)
    print("Valid score:", score)

except ValueError as error:
    print(error)


# ============================================================
# >>>>>>>>>>>>>>>>>>>>> EXERCISE 7 <<<<<<<<<<<<<<<<<<<<<<<<<<<
# ============================================================
# Create and use a custom exception.
#
# Create StudentNotFoundError.
#
# Search for a student by name.
#
# If the student does not exist, raise the custom exception.
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 7: CUSTOM EXCEPTION")
print("=" * 60)


class StudentNotFoundError(Exception):
    pass


def find_student(name, students):
    for student in students:

        if student["name"] == name:
            return student

    raise StudentNotFoundError(name)


students = [
    {"name": "Sara"}
]

try:
    print(find_student("Ali", students))

except StudentNotFoundError as error:
    print("Missing student:", error)


# ============================================================
#                    ALL EXERCISES COMPLETED
# ============================================================

print("\n" + "=" * 60)
print("ALL DATA HANDLING EXERCISES COMPLETED")
print("=" * 60)