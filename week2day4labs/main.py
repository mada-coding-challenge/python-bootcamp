
# ============================================================
# 🐍 WEEK 2 — DAY 4
# Python Conditionals, Validation & Pattern Matching
# ============================================================


# ============================================================
# 🧪 LAB 1 — Name & Score Validation
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 1 — NAME & SCORE VALIDATION")
print("=" * 60)

name = input("\n👤 Enter your name: ")

if(name):
    print("✅ Name: ", name)
else:
    print("❌ Name is required.")

score = input("📊 Enter your score: ")

if(score.isdigit() and 0 <= int(score) <= 100):
    print("✅ Score: ", score)

    score = int(score)

    # ========================================================
    # 🧪 LAB 3 — Grade Classification
    # ========================================================

    print("\n📚 Grade Classification:")

    if score >= 90:
       print("🏆 Grade: A")
    elif score >= 80:
       print("🥇 Grade: B")
    elif score >= 70:
       print("🥈 Grade: C")
    elif score >= 60:
       print("🥉 Grade: D")
    else:
       print("📖 Grade: F")

else:
    print("❌ Score must be a number between 0 and 100.")


# ============================================================
# 🧪 LAB 2 — Course Selection
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 2 — COURSE SELECTION")
print("=" * 60)

choice = input(
    "\n🎓 Choose Your course (Python, Java, or C++): "
).upper()

match choice:
    case "PYTHON":
        print("✅ Course: ", choice)
    case "JAVA":
        print("✅ Course: ", choice)
    case "C++":
        print("✅ Course: ", choice)
    case _:
        print("❌ Invalid course selection. Please choose Python, Java, or C++.")


# ============================================================
# 🧪 LAB 4 — Logical Conditions
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 4 — LOGICAL CONDITIONS")
print("=" * 60)

age = 20

if 18 <= age <= 50:
    print("✅ Age is between 18 and 50.")

print("✔️ Code completed")

is_active = True
is_verified = True
role = "admin"
is_blocked = False

if is_active and is_verified:
    print("✅ Account is ready to use")

if role == "admin" or role == "moderator":
    print("✏️ You can edit content.")

if not is_blocked:
    print("🔓 You can access the account.")
else:
    print("🔒 Account is blocked. Please contact support.")


# ============================================================
# 🧪 LAB 5 — Nested Conditions
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 5 — NESTED CONDITIONS")
print("=" * 60)

account_active = True
has_permission = False

if account_active:
    if has_permission:
        print("✅ Access granted")
    else:
        print("❌ Access denied")
else:
    print("🔒 Account is inactive")


# ============================================================
# 🧪 LAB 6 — Truthy & Falsy Values
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 6 — TRUTHY & FALSY VALUES")
print("=" * 60)

name

cart = []
balance = 0

if name:
    print("✅ Name has a value")

if not cart:
    print("🛒 Cart is empty")

print("💰 Balance:", bool(balance))


# ============================================================
# 🧪 LAB 7 — Name Validation
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 7 — NAME VALIDATION")
print("=" * 60)

name = input("\n👤 Enter your name: ").strip()

if not name:
    print("❌ Name is required.")
elif not name.replace(" ", "").isalpha():
    print("❌ Name must contain only letters and spaces.")
else:
    print("✅ Name is valid.")


# ============================================================
# 🧪 LAB 8 — Age Validation
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 8 — AGE VALIDATION")
print("=" * 60)

age_text = input("\n🎂 Enter your age: ").strip()

if age_text.isdigit():
    age = int(age_text)
    print(f"📅 You will be {age + 5} years old in 5 years.")
else:
    print("❌ Invalid age. Please enter a valid number.")


# ============================================================
# 🧪 LAB 9 — Score Validation
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 9 — SCORE VALIDATION")
print("=" * 60)

score_text = input("\n📊 Enter a number between 0 and 100: ")

if score_text.isdigit():
    score_x = int(score_text)

    if 0 <= score_x and score_x <= 100:
        print("✅ Valid score.")
    else:
        print("❌ Score must be between 0 and 100.")


# ============================================================
# 🧪 LAB 10 — Membership Validation
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 10 — MEMBERSHIP VALIDATION")
print("=" * 60)

membership = ["Admin", "Viewer", "Editor"]

current_membership = input(
    "\n👤 Enter your membership: "
).strip().lower()

print("📋 Membership:", current_membership.title())

if current_membership.title() in membership:
    print("✅ You are allowed to view the content.")
    print("👤 Membership:", current_membership.title())
else:
    print("❌ Please contact the admin team.")


# ============================================================
# 🧪 LAB 11 — Command Matching
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 11 — COMMAND MATCHING")
print("=" * 60)

command = input(
    "\n⌨️ Please enter a command (start, stop, status): "
).strip().lower()

match command:
    case "start":
        print("🟢 System is starting...")
    case "stop":
        print("🔴 System is stopping...")
    case "status":
        print("📊 System status: Running")
    case _:
        print("❌ Please enter proper command")


# ============================================================
# 🎉 END OF WEEK 2 — DAY 4
# ============================================================

print("\n" + "=" * 60)
print("🎉 WEEK 2 — DAY 4 COMPLETED!")
print("=" * 60)
