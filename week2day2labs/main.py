
# ============================================================
# 🧪 LAB 1 — Variable Names & Case Sensitivity
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 1 — VARIABLE NAMES & CASE SENSITIVITY")
print("=" * 60)

Student_name = "Sara"
student_name = "Abdullah"

print("\n📌 Output:")
print("-" * 30)
print(f"Student_name  → {Student_name}")
print(f"student_name  → {student_name}")


# ============================================================
# 🧪 LAB 2 — Variables & Strings
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 2 — VARIABLES & STRINGS")
print("=" * 60)

student_name = "Mada"
student_age = 30

course = "Python Programming"

print(f"\n👋 Welcome {student_name}!")
print(f"📚 Course: {course}")
print(f"🎂 Age: {student_age}")


# ============================================================
# 🧪 LAB 3 — Data Types
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 3 — DATA TYPES")
print("=" * 60)

student_name, student_age, student_is_registered = "Mada", 30, True

print("\n📌 Data Types:")
print("-" * 30)

print(type(student_age))
print(type(student_is_registered))
print(type(student_name))

print("\n🔎 Type Checking:")
print("-" * 30)

print(isinstance(student_name, str))
print(isinstance(student_age, int))


# ============================================================
# 🧪 LAB 4 — User Input & Conditional Statements
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 4 — USER INPUT & CONDITIONALS")
print("=" * 60)

age = input("\n👉 Enter your age: ")

if (isinstance(int(age), int)):
    print("✅ You are eligible to register for the course."  )
else:
    print("❌ You are not eligible to register for the course.")


# ============================================================
# 🧪 LAB 5 — String Indexing
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 5 — STRING INDEXING")
print("=" * 60)

teacher_name = "Faisal"

index = int(input("\n👉 Enter the index of the character you want to access in the teacher's name: "))

if index < 0 or index >= len(teacher_name):
    print("❌ Invalid index. Please enter a valid index.")
else:       
    print(f"✅ Character at index {index}: {teacher_name[index]}")


# ============================================================
# 🧪 LAB 6 — Challenge: Swapping Variables
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 6 — CHALLENGE: SWAPPING VARIABLES")
print("=" * 60)

x = 1
y = 0

x , y = y , x

print("\n🔄 Values after swapping:")
print("-" * 30)
print(f"x = {x}")
print(f"y = {y}")


# ============================================================
# 🎉 END OF LABS
# ============================================================

print("\n" + "=" * 60)
print("🎉 ALL LABS COMPLETED!")
print("=" * 60)

