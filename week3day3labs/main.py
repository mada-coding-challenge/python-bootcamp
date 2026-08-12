
# ============================================================
# 🐍 WEEK 3 — DAY 3
# Python Collections
# Lists • Tuples • Sets • Dictionaries
# ============================================================

import math


# ============================================================
# 🧪 IN-CLASS EXERCISE 1 — Lists
# ============================================================

print("\n" + "=" * 60)
print("🧪 IN-CLASS EXERCISE 1 — LISTS")
print("=" * 60)

students = ["Sara", "Omar", "Lina"]

print("👩‍🎓 Students:", students)
print("🥇 First student:", students[0])
print("📦 Type:", type(students))


# ============================================================
# 🧪 IN-CLASS EXERCISE 2 — List Indexing
# ============================================================

print("\n" + "=" * 60)
print("🧪 IN-CLASS EXERCISE 2 — LIST INDEXING")
print("=" * 60)

colors = ["Red", "Blue", "Pink"]

print("🔴 First color:", colors[0])
print("🔵 Second color:", colors[1])
print("🩷 Last color:", colors[-1])


# ============================================================
# 🧪 IN-CLASS EXERCISE 3 — List Slicing
# ============================================================

print("\n" + "=" * 60)
print("🧪 IN-CLASS EXERCISE 3 — LIST SLICING")
print("=" * 60)

numbers = [10, 20, 30, 40, 50]

print("✂️ numbers[1:4]:", numbers[1:4])
print("✂️ numbers[:3]:", numbers[:3])
print("✂️ numbers[::2]:", numbers[::2])
print("🔄 numbers[::-1]:", numbers[::-1])


# ============================================================
# 🧪 IN-CLASS EXERCISE 4 — Modifying Lists
# ============================================================

print("\n" + "=" * 60)
print("🧪 IN-CLASS EXERCISE 4 — MODIFYING LISTS")
print("=" * 60)

tasks = ["Plan", "code"]

tasks[0] = "design"
tasks.append("test")
tasks.insert(1, "review")

print("📋 Updated tasks:", tasks)


# ============================================================
# 🧪 IN-CLASS EXERCISE 5 — Removing & Sorting
# ============================================================

print("\n" + "=" * 60)
print("🧪 IN-CLASS EXERCISE 5 — REMOVING & SORTING")
print("=" * 60)

scores = [88, 72, 95, 81]

scores.remove(72)

last = scores.pop()
scores.sort()

print("📊 Sorted scores:", scores)
print("🗑️ Removed last score:", last)


# ============================================================
# 🧪 IN-CLASS EXERCISE 6 — Iterating Through Lists
# ============================================================

print("\n" + "=" * 60)
print("🧪 IN-CLASS EXERCISE 6 — ITERATING THROUGH LISTS")
print("=" * 60)

for student in students:
    print("👩‍🎓", student)

print("\n🔢 Using enumerate():")

for index, student in enumerate(students):
    print(index, student)

print("\n📦 enumerate() objects:")

for student in enumerate(students):
    print(student)


# ============================================================
# 🧪 IN-CLASS EXERCISE 7 — Nested Lists
# ============================================================

print("\n" + "=" * 60)
print("🧪 IN-CLASS EXERCISE 7 — NESTED LISTS")
print("=" * 60)

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print("🔢 First row:", matrix[0])
print("🎯 matrix[1][2]:", matrix[1][2])


# ============================================================
# 🧪 IN-CLASS EXERCISE 8 — Tuples
# ============================================================

print("\n" + "=" * 60)
print("🧪 IN-CLASS EXERCISE 8 — TUPLES")
print("=" * 60)

location = (24.7135, 46.6753)

print("📍 Latitude:", location[0])
print("📍 Longitude:", location[-1])


# ============================================================
# 🧪 IN-CLASS EXERCISE 9 — Tuple Unpacking
# ============================================================

print("\n" + "=" * 60)
print("🧪 IN-CLASS EXERCISE 9 — TUPLE UNPACKING")
print("=" * 60)

student = ("Sara", 22, "Python", "ksu", "java")

name, age, course, *others = student

print("👤 Name:", name)
print("🎂 Age:", age)
print("📚 Course:", course)
print("📦 Other information:", others)


# ============================================================
# 🧪 IN-CLASS EXERCISE 10 — Sets
# ============================================================

print("\n" + "=" * 60)
print("🧪 IN-CLASS EXERCISE 10 — SETS")
print("=" * 60)

skills = {"Python", "Git", "Python"}

skills.add("Django")

print("🛠️ Skills:", skills)
print("🔎 'Git' in skills:", "Git" in skills)
print("📊 Number of skills:", len(skills))


# ============================================================
# 🧪 IN-CLASS EXERCISE 11 — Set Operations
# ============================================================

print("\n" + "=" * 60)
print("🧪 IN-CLASS EXERCISE 11 — SET OPERATIONS")
print("=" * 60)

backend = {"Python", "Django", "SQL"}
frontend = {"HTML", "css", "Javascript", "SQL"}

print("🔗 Union:", backend | frontend)
print("🤝 Intersection:", backend & frontend)
print("➖ Difference:", backend - frontend)


# ============================================================
# 🧪 IN-CLASS EXERCISE 12 — Dictionaries
# ============================================================

print("\n" + "=" * 60)
print("🧪 IN-CLASS EXERCISE 12 — DICTIONARIES")
print("=" * 60)

student = {
    "name": "Sara",
    "age": 22,
    "course": "python",
    "score": 90,
    "grade": "A"
}

print("👤 Name:", student["name"])

student["score"] = 95
student["grade"] = "A"

email = student.get("email", "Not set")
grade = student.pop("grade")

print("📧 Email:", email)
print("🎓 Removed grade:", grade)
print("📋 Updated student:", student)


# ============================================================
# 🧪 IN-CLASS EXERCISE 13 — Dictionary Iteration
# ============================================================

print("\n" + "=" * 60)
print("🧪 IN-CLASS EXERCISE 13 — DICTIONARY ITERATION")
print("=" * 60)

print("🔑 Keys:")

for key in student:
    print(key)

print("\n🔑 Values:")

for key, value in student.items():
    print(f"{key}: {value}")


# ============================================================
# 🧪 IN-CLASS EXERCISE 14 — Membership & Length
# ============================================================

print("\n" + "=" * 60)
print("🧪 IN-CLASS EXERCISE 14 — MEMBERSHIP & LENGTH")
print("=" * 60)

names = ["Sara", "Omar"]
skills = ["Python", "Set"]
student = {"name": "Sara", "score": 95}

print("📊 Number of names:", len(names))
print("🐍 'Python' in skills:", "Python" in skills)
print("👤 'name' in student:", "name" in student)


# ============================================================
# 🧪 IN-CLASS EXERCISE 15 — List of Dictionaries
# ============================================================

print("\n" + "=" * 60)
print("🧪 IN-CLASS EXERCISE 15 — LIST OF DICTIONARIES")
print("=" * 60)

students = [
    {"name": "Sara", "score": 95},
    {"name": "Omar", "score": 88}
]

for student in students:
    print(f"👩‍🎓 {student['name']} — Score: {student['score']}")


# ============================================================
# 🎯 GUIDED PRACTICE — Nested Collections
# ============================================================

print("\n" + "=" * 60)
print("🎯 GUIDED PRACTICE — NESTED COLLECTIONS")
print("=" * 60)

students = [
    {
        "name": "mada",
        "scores": (90, 80, 70),
        "skills": {"python", "java"}
    },
    {
        "name": "Sara",
        "scores": (60, 100, 30),
        "skills": {"python", "dart"}
    },
    {
        "name": "Taif",
        "scores": (100, 50, 40),
        "skills": {"sql", "java"}
    }
]

students[0]["skills"].add("javascript")

for student in students:
    print(
        f"{student['name']} scores average is "
        f"{sum(student['scores']) / len(student['scores'])} "
        f"skills: {student['skills']}"
    )


# ============================================================
# 🧪 LAB 1 — Iterables & enumerate()
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 1 — ITERABLES & ENUMERATE")
print("=" * 60)

students = ["Sara", "Mashael", "Dalal", "Taif"]

for student in students:
    print("👩‍🎓", student)

iterable = enumerate(students)

print("\n🔎 First item from enumerate:")
print(next(iterable))


# ============================================================
# 🧪 LAB 2 — Collection Types
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 2 — COLLECTION TYPES")
print("=" * 60)

set_col = ["Abdullah", "Nasser", "Dalal", "Sara"]
tuple_col = (11, 12, 33, 44, 55, 66)
dict_col = {"name": "Abdullah", "age": 22}
list_col = ["abc", 333, (33, 33)]

print("📋 List:", set_col)
print("📦 Type:", type(set_col))

print("🔢 Tuple:", tuple_col)
print("📦 Type:", type(tuple_col))

print("📖 Dictionary:", dict_col)
print("📦 Type:", type(dict_col))

print("📚 Mixed List:", list_col)
print("📦 Type:", type(list_col))

print("\n🔎 Dictionary Values Types:")

for c in dict_col.values():
    print(type(c))


# ============================================================
# 🧪 LAB 3 — List Indexing & Reversing
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 3 — LIST INDEXING & REVERSING")
print("=" * 60)

cars = ["GMC", " BMW", "Geely", "Porsche", "Merc", "Chevy"]

print("🚗 Fourth car:", cars[3])
print("🚗 Last car:", cars[-1])
print("🔄 Reversed:", cars[-1::-1])


# ============================================================
# 🧪 LAB 4 — List Modification
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 4 — LIST MODIFICATION")
print("=" * 60)

tasks = ["Read email", "Open ticket"]

tasks[0] = "Login"
tasks.append("Get Coffee")
tasks.insert(0, "Get breakfast")
tasks.pop(3)

print("📋 Final tasks:", tasks)


# ============================================================
# 🧪 LAB 5 — Built-in Functions & math Module
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 5 — BUILT-IN FUNCTIONS & MATH")
print("=" * 60)

nums = [11, 22, 33, 44, 55, 66]

print("➕ Sum:", sum(nums))
print("📊 Length:", len(nums))
print("⬆️ Maximum:", max(nums))
print("⬇️ Minimum:", min(nums))
print("√ Square root of maximum:", math.sqrt(max(nums)))
print("📖 math.__doc__:", math.__doc__)

print("\n📋 Original numbers:", nums)
print("🗑️ Removed item:", nums.pop(2))
print("🔽 Sorted descending:", sorted(nums, reverse=True))


# ============================================================
# 🧪 LAB 6 — Set Modification
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 6 — SET MODIFICATION")
print("=" * 60)

skills = {"Python", "Django", "Flask", "FastAPI", "Java"}

skills.add("CSS")
skills.add("HTML")

# skills.remove("Java")
skills.discard("Java")

print("🛠️ Final skills:", skills)


# ============================================================
# 🎉 END OF WEEK 3 — DAY 3
# ============================================================

print("\n" + "=" * 60)
print("🎉 WEEK 3 — DAY 3 COMPLETED!")
print("=" * 60)

