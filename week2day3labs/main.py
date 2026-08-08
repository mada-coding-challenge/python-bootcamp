
# ============================================================
# 🐍 WEEK 2 — DAY 3
# Python Operators, Strings & Membership
# ============================================================


# ============================================================
# 🧪 LAB 1 — Arithmetic Operators
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 1 — ARITHMETIC OPERATORS")
print("=" * 60)

results = 10 + 5 * 2 - 4 / 2

print("\n📌 Result:")
print(f"results: {results}")


# ============================================================
# 🧪 LAB 2 — Floor Division & Modulo
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 2 — FLOOR DIVISION & MODULO")
print("=" * 60)

total_items = 17
box_capacity = 5

full_boxes = total_items // box_capacity
remaining_items = total_items % box_capacity

print("\n📦 Box Calculation:")
print(f"Total items      : {total_items}")
print(f"Box capacity     : {box_capacity}")
print(f"Full boxes       : {full_boxes}")
print(f"Remaining items  : {remaining_items}")


# ============================================================
# 🧪 LAB 3 — Operator Precedence
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 3 — OPERATOR PRECEDENCE")
print("=" * 60)

base_calc = 2 + 3 * 2 ** 2
gcalc = (2 + 3) * (2 ** 2)

print("\n📐 Calculations:")
print(f"base_calc: {base_calc}")
print(f"gcalc:     {gcalc}")


# ============================================================
# 🧪 LAB 4 — Logical Operators
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 4 — LOGICAL OPERATORS")
print("=" * 60)

user_age = 25
has_prermission = True

is_eligible = (user_age >= 18 and has_prermission)

print("\n🔐 Eligibility Check:")
print(f"User age          : {user_age}")
print(f"Has permission    : {has_prermission}")
print(f"Is eligible       : {is_eligible}")


# ============================================================
# 🧪 LAB 5 — Assignment Operators
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 5 — ASSIGNMENT OPERATORS")
print("=" * 60)

score = 10

score += 5
score *= 5

print("\n🏆 Score:")
print(f"Final score: {score}")


# ============================================================
# 🧪 LAB 6 — Membership Operators
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 6 — MEMBERSHIP OPERATORS")
print("=" * 60)

memberships = ["Admin", "Moderator", "Member"]

current_membership = "Admin"

if current_membership in memberships:
    print("\n✅ You have access to the system.")
else:
    print("\n❌ Go Home.")


# ============================================================
# 🧪 LAB 7 — String Search & Membership
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 7 — STRING SEARCH")
print("=" * 60)

sentence = "Python web development."

new_sentence = sentence.find("Python")

print("\n🔎 Search Results:")
print(f"Sentence: {sentence}")
print(f"Start index of 'Python': {new_sentence}")
print(f"'Python' exists in sentence: {'Python' in sentence}")


# ============================================================
# 🧪 LAB 8 — String Indexing & Slicing
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 8 — STRING INDEXING & SLICING")
print("=" * 60)

message = "Python programming"

first_char = message[0]
last_char = message[-1]

print("\n🔤 Characters:")
print(f"First character: {first_char}")
print(f"Last character : {last_char}")

slicing = message[0:6]

print(f"Sliced text    : {slicing}")


# ============================================================
# 🧪 LAB 9 — String Cleaning & Formatting
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 9 — STRING CLEANING & FORMATTING")
print("=" * 60)

my_email = "    mada@g.com   "

clean_email = my_email.strip().lower()

print("\n📧 Email:")
print(f"Original email : '{my_email}'")
print(f"Clean email    : '{clean_email}'")

message = "python is a powerful programming language."

title_case_message = message.title()

print("\n📝 Text Formatting:")
print(f"Original : {message}")
print(f"Title    : {title_case_message}")


# ============================================================
# 🧪 LAB 10 — Split & Join
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 10 — SPLIT & JOIN")
print("=" * 60)

csv_text = "apple,banana,cherry,grape"

fruits_list = csv_text.split(",")

print("\n🍎 Split Result:")
print(f"Original text : {csv_text}")
print(f"Fruits list   : {fruits_list}")

joined_fruits = "-".join(fruits_list)

print("\n🔗 Join Result:")
print(f"Joined fruits : {joined_fruits}")


# ============================================================
# 🧪 LAB 11 — Immutability & Identity
# ============================================================

print("\n" + "=" * 60)
print("🧪 LAB 11 — IMMUTABILITY & IDENTITY")
print("=" * 60)

name = "Khaled"

try:
    name[0] = "A"
except TypeError as e:
    print("\n🔒 String Immutability:")
    print(f"Error: {e}")

x = 5
y = 5

print("\n🧠 Object Identity:")

if x is y:
    print("x and y are the same object in memory.")
else:
    print("x and y are different objects in memory.")

print(f"id(x): {id(x)}")
print(f"id(y): {id(y)}")


# ============================================================
# 🎉 END OF LABS
# ============================================================

print("\n" + "=" * 60)
print("🎉 ALL LABS COMPLETED!")
print("=" * 60)

