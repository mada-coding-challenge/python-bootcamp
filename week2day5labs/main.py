# ============================================================
# 🐍 WEEK 2 — DAY 5
# Python Loops & Repetition
# ============================================================


# ============================================================
# 🧪 LAB 1 — Even & Odd Numbers
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 1 — EVEN & ODD NUMBERS")
print("=" * 60)

rangeNums = int(input("\n🔢 Enter number: "))

evenCount = 0

for number in range(1, rangeNums + 1):
    if number % 2 == 0:
        print(f"🟢 {number} is even")
        evenCount += 1
    else:
        print(f"🔵 {number} is odd")

print(f"\n📊 Total even numbers: {evenCount}")
print(f"🔢 Total numbers: {rangeNums}")


# ============================================================
# 🧪 LAB 2 — Loop Attempts
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 2 — LOOP ATTEMPTS")
print("=" * 60)

for number in range(3):
    print(f"🔄 Attempt: {number + 1}")


# ============================================================
# 🧪 LAB 3 — Even Numbers Using range()
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 3 — EVEN NUMBERS")
print("=" * 60)

for num in range(2, 11, 2):
    print(f"🔢 {num}")


# ============================================================
# 🧪 LAB 4 — Countdown
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 4 — COUNTDOWN")
print("=" * 60)

for secnndsToLaunch in range(10, 0, -1):
    print(f"🚀 T-{secnndsToLaunch}")


# ============================================================
# 🧪 LAB 5 — Looping Through a String
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 5 — LOOPING THROUGH A STRING")
print("=" * 60)

course = "Python"

for letter in course:
    print(f"🔤 {letter}")


# ============================================================
# 🧪 LAB 6 — Looping Through a List
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 6 — LOOPING THROUGH A LIST")
print("=" * 60)

students = ["sara", "Shahad", "Khadija"]

for student in students:
    print(f"👩‍🎓 Progressing student is: {student}")


# ============================================================
# 🧪 LAB 7 — Finding Even Numbers
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 7 — FINDING EVEN NUMBERS")
print("=" * 60)

for number in range(1, 11):
    if number % 2 == 0:
        print(f"🟢 {number} is even")
    print("-------")


# ============================================================
# 🧪 LAB 8 — Counting Even Numbers
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 8 — COUNTING EVEN NUMBERS")
print("=" * 60)

numbers = [4, 7, 10, 13, 16, 21]
even_counter = 0

for num in numbers:
    if num % 2 == 0:
        even_counter += 1

print(f"\n📊 Total even numbers is: {even_counter}")


# ============================================================
# 🧪 LAB 9 — Calculating Total & VAT
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 9 — TOTAL & VAT CALCULATION")
print("=" * 60)

prices = [25, 30, 55, 60]
total = 0

for price in prices:
    total += price

print(f"\n💰 Your total is: {total}")
print(f"🧾 VAT (15%): {total * (15 / 100):.2f}")


# ============================================================
# 🧪 LAB 10 — While Loop
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 10 — WHILE LOOP")
print("=" * 60)

count = 1

while count < 5:
    count += 1
    print(f"🔄 Count . . . {count}")

print("✅ Loop completed")


# ============================================================
# 🧪 LAB 11 — Input Validation with while
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 11 — INPUT VALIDATION")
print("=" * 60)

message = "Please enter your age: "
age_text = input(message).strip()

while not age_text.isdigit():
    age_text = input(message).strip()

age = int(age_text)

print(f"🎂 You are: {age}")


# ============================================================
# 🧪 LAB 12 — Password Loop
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 12 — PASSWORD LOOP")
print("=" * 60)

password = "python123"

print("🔐 Enter Your Password")

while password != "":
    password = input("🔑 Enter Your Password: ")


# ============================================================
# 🧪 LAB 13 — Password Validation
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 13 — PASSWORD VALIDATION")
print("=" * 60)

password = ""

password = input("🔐 Please enter password: ")

while password != "python123":
    password = input("❌ Incorrect password, try again: ")

print("✅ Access granted")


# ============================================================
# 🧪 LAB 14 — pass Statement
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 14 — PASS STATEMENT")
print("=" * 60)

for score in [80, 55, 4, 90]:
    if score < 50:
        pass

    print(f"📊 Score processed: {score}")


# ============================================================
# 🧪 LAB 15 — continue Statement
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 15 — CONTINUE STATEMENT")
print("=" * 60)

for record in [80, 55, 45, 90]:
    if record < 50:
        print(f"⏭️ Skipping: {record}")
        continue

    print(f"✅ Processing: {record}")


# ============================================================
# 🧪 LAB 16 — break Statement
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 16 — BREAK STATEMENT")
print("=" * 60)

for badscore in [80, 55, 45, 90]:
    if badscore < 50:
        print(f"🛑 Stopping at: {badscore}")
        break

    print(f"👀 We saw: {badscore}")


# ============================================================
# 🧪 LAB 17 — Nested Loops
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 17 — NESTED LOOPS")
print("=" * 60)

for row in range(1, 4):
    for column in range(1, 4):
        print(f"📐 Row: {row} x {column} = {row * column}")


# ============================================================
# 🎉 END OF WEEK 2 — DAY 5
# ============================================================

print("\n" + "=" * 60)
print("🎉 WEEK 2 — DAY 5 COMPLETED!")
print("=" * 60)

