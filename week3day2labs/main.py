
# ============================================================
# 🐍 WEEK 3 — DAY 2
# Python Modules, Scope & Namespaces
# ============================================================


# ============================================================
# 🧪 PRACTICE — IMPORTING A FUNCTION
# ============================================================

print("\n" + "=" * 60)
print("🧪 PRACTICE — IMPORTING A FUNCTION")
print("=" * 60)

from grades import calculate_grade

print("\n📊 Grade Results")
print("-" * 40)

print(f"50 → {calculate_grade(50)}")
print(f"60 → {calculate_grade(60)}")
print(f"70 → {calculate_grade(70)}")


# ============================================================
# 🧪 LAB 1 — Variables & Function Names
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 1 — VARIABLES & FUNCTION NAMES")
print("=" * 60)

course = "Web Development Bootcamp"
duration = 12


def type(course):
    print("Opss!")


print(f"📚 Course: {course}")
print(f"⏱️ Duration: {duration} weeks")
print(f"🔎 type(course): {type(course)}")


# ============================================================
# 🧪 LAB 2 — globals() & Global Namespace
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 2 — GLOBAL NAMESPACE")
print("=" * 60)

building = "Tuwaiq Academy"
cohort_size = 20

print(f"🏫 Welcome to {building}, class limit is {cohort_size}")
print(f"🔎 'Tuwiaq' in building → {"Tuwiaq" in building}")
print(f"🔎 'cohort_size' in globals() → {"cohort_size" in globals()}")
print(f"🌍 globals()['building'] → {globals()['building']}")


# ============================================================
# 🧪 LAB 3 — Local Scope & Nested Functions
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 3 — LOCAL SCOPE & NESTED FUNCTIONS")
print("=" * 60)

location = "Globl"


def outter():
    location = "Outter"

    print(f"🌍 From {location}")

    def inner():
        location = "Inner"
        print(f"📍 From {location}")

    inner()


outter()


# ============================================================
# 🧪 LAB 4 — Function Call Chain
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 4 — FUNCTION CALL CHAIN")
print("=" * 60)


def printer():
    print("🖨️ Welcome")


def desk():
    printer()


def room():
    desk()


def house():
    room()


def city():
    house()


def country():
    city()


country()


# ============================================================
# 🧪 LAB 5 — Local vs Global Variables
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 5 — LOCAL VS GLOBAL VARIABLES")
print("=" * 60)

language = "Python"


def show_lang(language):
    print(f"📍 Inside function: {language}")


show_lang("Dart")

print(f"🌍 Outside function: {language}")


# ============================================================
# 🧪 LAB 6 — Global Variable Inside a Function
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 6 — GLOBAL VARIABLE ACCESS")
print("=" * 60)

rate = 0.15


def getTotal(amount):
    total = amount * rate + amount
    return total


print(f"💰 Total: {getTotal(199.99):.2f}")
print(f"🔢 Rounded total: {round(getTotal(199.99), 2)}")


# ============================================================
# 🧪 LAB 7 — locals() & Local Namespace
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 7 — LOCAL NAMESPACE")
print("=" * 60)


def inspect_order(item, qty):
    subtotal = 25 * qty

    print("\n📦 Order Information")
    print("-" * 40)
    print(f"📝 Item: {item}")
    print(f"🔢 Quantity: {qty}")
    print(f"💰 Subtotal: {subtotal}")

    print("\n🔍 locals():")
    print(locals())

    print(f"\n🔍 locals()['subtotal']: {locals()['subtotal']}")


inspect_order("Pen", 10)


# ============================================================
# 🎉 END OF WEEK 3 — DAY 2
# ============================================================

print("\n" + "=" * 60)
print("🎉 WEEK 3 — DAY 2 COMPLETED!")
print("=" * 60)

