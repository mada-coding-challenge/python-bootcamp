
# ============================================================
# 🐍 WEEK 3 — DAY 1
# Python Functions
# ============================================================


# ============================================================
# 🏆 PRACTICE — Calculate Grade
# ============================================================

print("\n" + "=" * 60)
print("🏆 PRACTICE — CALCULATE GRADE")
print("=" * 60)


def calculate_grade(score):
    grade = ""

    if score >= 90:
        grade = "🏆 Grade: A"
    elif score >= 80:
        grade = "🥇 Grade: B"
    elif score >= 70:
        grade = "🥈 Grade: C"
    elif score >= 60:
        grade = "🥉 Grade: D"
    else:
        grade = "Grade F"

    return grade


print(f"""
📊 Grade Results

60 → {calculate_grade(60)}
50 → {calculate_grade(50)}
80 → {calculate_grade(80)}
""")


# ============================================================
# 🧪 LAB 1 — Creating & Calling a Function
# ============================================================

print("=" * 60)
print("🧪 LAB 1 — CREATING & CALLING A FUNCTION")
print("=" * 60)


def great():
    print("👋 Welcome to Python")


great()


# ============================================================
# 🧪 LAB 2 — Displaying a Menu
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 2 — DISPLAYING A MENU")
print("=" * 60)


def show_menu():
    print("☕ 1 - Coffee")
    print("🍵 2 - Tea")
    print("🫚 3 - Ginger")


show_menu()

print("\n📍 Outside the function call:")

show_menu()


# ============================================================
# 🧪 LAB 3 — Nested Functions & Scope
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 3 — NESTED FUNCTIONS & SCOPE")
print("=" * 60)


def unknownScope():
    print("📌 Line One")

    def gotFunc():
        print("➡️ From within the GoTO")

    print("📌 Where is line 2?")

    gotFunc()

    print("📌 I'm up here")


unknownScope()


# ============================================================
# 🧪 LAB 4 — Function Parameters
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 4 — FUNCTION PARAMETERS")
print("=" * 60)


def great_student(name):
    print(f"👋 Welcome {name}")


great_student("Sara and Taif")


# ============================================================
# 🧪 LAB 5 — Multiple Parameters
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 5 — MULTIPLE PARAMETERS")
print("=" * 60)


def show_booking(destination, nights):
    print(
        f"✈️ You're traveling to {destination}, "
        f"and will stay for {nights} nights"
    )


show_booking("Jeddah", 2)
show_booking("Doha", 5)


# ============================================================
# 🧪 LAB 6 — Default Parameters, Return Values & Docstrings
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 6 — DEFAULT PARAMETERS & DOCSTRINGS")
print("=" * 60)


def getVAT(total, rate=0.15):
    """This function will get the total with VAT added to it,
    and return the sum"""
    subTotal = total + (total * rate)
    return subTotal


print(f"💰 Total with 15% VAT: {getVAT(154):.2f}")
print(f"💰 Total with 5% VAT:  {getVAT(154, 0.05):.2f}")

print("\n📖 Function Documentation:")
print(getVAT.__doc__)


# ============================================================
# 🎉 END OF WEEK 3 — DAY 1
# ============================================================

print("\n" + "=" * 60)
print("🎉 WEEK 3 — DAY 1 COMPLETED!")
print("=" * 60)

