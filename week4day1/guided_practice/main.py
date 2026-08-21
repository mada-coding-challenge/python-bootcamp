# ============================================================
#              PYTHON OOP - GUIDED PRACTICE
# ============================================================
#
# Topic:
# Student and Course Management
#
# Concepts:
# - Classes and objects
# - Instance attributes
# - Methods
# - Lists of objects
# - isinstance()
# - Adding data to objects
# - Calculating averages
# - Default values
# ============================================================


# ============================================================
#                    GUIDED PRACTICE
# ============================================================
#
# Build a simple course system.
#
# The system should:
#
# 1. Create Student objects.
# 2. Store each student's name and scores.
# 3. Add new scores to a student.
# 4. Calculate the student's average.
# 5. Create a Course object.
# 6. Add students to the course.
# 7. Display all students with their scores and averages.
#
# ============================================================


# ============================================================
# STEP 1: CREATE THE STUDENT CLASS
# ============================================================
#
# Each Student should have:
# - name
# - scores
#
# The scores should default to an empty list.
# ============================================================


class Student:
    def __init__(self, name, scores=None):
        self.name = name
        self.scores = scores if scores is not None else []

    # --------------------------------------------------------
    # STEP 2: ADD A SCORE
    # --------------------------------------------------------
    #
    # Only scores between 0 and 100 should be accepted.
    # --------------------------------------------------------

    def add_score(self, score):
        if 0 <= score <= 100:
            self.scores.append(score)

    # --------------------------------------------------------
    # STEP 3: CALCULATE THE AVERAGE
    # --------------------------------------------------------
    #
    # If the student has no scores, return 0.
    # Otherwise, calculate the average.
    # --------------------------------------------------------

    def average(self):
        if len(self.scores) == 0:
            return 0

        return sum(self.scores) / len(self.scores)


# ============================================================
# STEP 4: CREATE THE COURSE CLASS
# ============================================================
#
# A Course should contain a list of students.
# ============================================================


class Course:
    def __init__(self, students=[]):
        self.students = students

    # --------------------------------------------------------
    # STEP 5: DISPLAY STUDENTS
    # --------------------------------------------------------
    #
    # Display:
    # - student name
    # - scores
    # - average
    # --------------------------------------------------------

    def display(self):
        for student in self.students:
            print(
                f"Name: {student.name} | "
                f"Scores: {student.scores} | "
                f"Average: {student.average():.2f}"
            )

    # --------------------------------------------------------
    # STEP 6: ADD A STUDENT
    # --------------------------------------------------------
    #
    # Only Student objects should be added to the course.
    # --------------------------------------------------------

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)


# ============================================================
# STEP 7: CREATE THE COURSE
# ============================================================

course = Course()


# ============================================================
# STEP 8: CREATE AND ADD STUDENTS
# ============================================================

course.add_student(Student("Sara", [30, 40, 80]))
course.add_student(Student("Omar", [40, 89, 40]))
course.add_student(Student("Lina", [90, 100, 70]))


# ============================================================
# STEP 9: DISPLAY THE COURSE
# ============================================================

print("=" * 65)
print("                    COURSE STUDENTS")
print("=" * 65)

course.display()

print("=" * 65)