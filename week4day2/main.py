from pathlib import Path


# ============================================================
#                  PYTHON FILE HANDLING
# ============================================================


# ============================================================
# >>>>>>>>>>>>>>>>>>>>> EXERCISE 1 <<<<<<<<<<<<<<<<<<<<<<<<<<<
# ============================================================
# Read a text file using pathlib.
#
# Goal:
# - Create a Path object
# - Open a file
# - Read its contents
# - Check whether the file is closed
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 1: READ A FILE")
print("=" * 60)

path = Path("notes.txt")

# Create the file so the exercise can run independently
path.write_text(
    "Python is easy to learn.\n"
    "Practice makes progress.\n",
    encoding="utf-8"
)

with path.open("r", encoding="utf-8") as file:
    content = file.read()

print("File content:")
print(content)

print("File closed:", file.closed)


# ============================================================
# >>>>>>>>>>>>>>>>>>>>> EXERCISE 2 <<<<<<<<<<<<<<<<<<<<<<<<<<<
# ============================================================
# Create a directory and work with file paths.
#
# Goal:
# - Create a directory
# - Check if it is a directory
# - Create a Path for a file
# - Check if the file exists
# - Get file information
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 2: WORKING WITH PATHS")
print("=" * 60)

data_dir = Path("data")

data_dir.mkdir(exist_ok=True)

data_file = data_dir / "students.txt"

print("Is directory:", data_dir.is_dir())
print("Does students.txt exist:", data_file.exists())

print("Full path:", data_file)
print("File name:", data_file.name)
print("File suffix:", data_file.suffix)


# ============================================================
# >>>>>>>>>>>>>>>>>>>>> EXERCISE 3 <<<<<<<<<<<<<<<<<<<<<<<<<<<
# ============================================================
# Append new content to an existing file.
#
# File modes:
#
# "r" -> read
# "w" -> write and replace
# "a" -> append
# "x" -> create only if file does not exist
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 3: APPEND TO A FILE")
print("=" * 60)

path = Path("notes.txt")

with path.open("a", encoding="utf-8") as file:
    file.write("New note\n")

print("New note added.")

print("\nUpdated file:")

with path.open("r", encoding="utf-8") as file:
    print(file.read())


# ============================================================
# >>>>>>>>>>>>>>>>>>>>> EXERCISE 4 <<<<<<<<<<<<<<<<<<<<<<<<<<<
# ============================================================
# Read a file line by line.
#
# Goal:
# - Loop through a file
# - Remove whitespace with strip()
# - Ignore empty lines
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 4: READ FILE LINE BY LINE")
print("=" * 60)

path = Path("students.txt")

path.write_text(
    "Sara\n"
    "Ali\n"
    "\n"
    "Omar\n"
    "Lina\n",
    encoding="utf-8"
)

print("Students:")

with path.open("r", encoding="utf-8") as file:
    for line in file:
        name = line.strip()

        if name:
            print(name)


# ============================================================
# >>>>>>>>>>>>>>>>>>>>> EXERCISE 5 <<<<<<<<<<<<<<<<<<<<<<<<<<<
# ============================================================
# Write content to a file.
#
# Goal:
# - Use "w" mode
# - Write multiple lines
# - Get the number of characters written
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 5: WRITE TO A FILE")
print("=" * 60)

path = Path("students.txt")

with path.open("w", encoding="utf-8") as file:
    count = file.write("Sara\nAli\n")

print("Characters written:", count)

print("\nFile content:")

print(path.read_text(encoding="utf-8"))


# ============================================================
# >>>>>>>>>>>>>>>>>>>>> EXERCISE 6 <<<<<<<<<<<<<<<<<<<<<<<<<<<
# ============================================================
# Append information to a log file.
#
# Goal:
# - Open a file using append mode
# - Add a new activity
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 6: ACTIVITY LOG")
print("=" * 60)

path = Path("activity.log")

with path.open("a", encoding="utf-8") as file:
    file.write("Student enrolled: Sara\n")

print("Activity saved.")

print("\nActivity log:")

print(path.read_text(encoding="utf-8"))


# ============================================================
# >>>>>>>>>>>>>>>>>>>>> EXERCISE 7 <<<<<<<<<<<<<<<<<<<<<<<<<<<
# ============================================================
# Write a list of names to a file.
#
# Goal:
# - Create a list
# - Join the values using "\n"
# - Write the result to a file
# - Support Unicode text
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 7: WRITE A LIST TO A FILE")
print("=" * 60)

names = [
    "Sara",
    "نورة",
    "Ali"
]

text = "\n".join(names) + "\n"

Path("students.txt").write_text(
    text,
    encoding="utf-8"
)

print("Names saved successfully.")

print("\nFile content:")

print(Path("students.txt").read_text(encoding="utf-8"))


# ============================================================
# >>>>>>>>>>>>>>>>>>>>> EXERCISE 8 <<<<<<<<<<<<<<<<<<<<<<<<<<<
# ============================================================
# FINAL PRACTICE
#
# Combine the concepts from the previous exercises.
#
# Create a students file and then:
# - Read the file
# - Display each student
# - Count the students
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 8: FINAL FILE PRACTICE")
print("=" * 60)

students = [
    "Sara",
    "نورة",
    "Ali",
    "Omar"
]

path = Path("students.txt")

path.write_text(
    "\n".join(students) + "\n",
    encoding="utf-8"
)

count = 0

print("Students:")

with path.open("r", encoding="utf-8") as file:
    for line in file:
        name = line.strip()

        if name:
            print("-", name)
            count += 1

print("\nTotal students:", count)


# ============================================================
#                        COMPLETE
# ============================================================

print("\n" + "=" * 60)
print("ALL FILE HANDLING EXERCISES COMPLETED")
print("=" * 60)