# ============================================================
# BASIC PYTHON EXAMPLES
# ============================================================

print("\n" + "=" * 60)
print("BASIC PYTHON EXAMPLES")
print("=" * 60)

numbers = range(1_000_000)

total = sum(
    number ** 2
    for number in numbers
)

print(f"\nSum of squares: {total}")


items = ["Python", "Git"]

items.append("Django")

name = "sara"
name = name.title()

print(f"Formatted name: {name}")


# ============================================================
# ALIASING
# ============================================================

print("\n" + "=" * 60)
print("ALIASING")
print("=" * 60)

alias = items

alias.append("Django")

print(f"items : {items}")
print(f"alias : {alias}")
print(f"Same object? {items is alias}")


# ============================================================
# COPY VS ORIGINAL
# ============================================================

print("\n" + "=" * 60)
print("COPY VS ORIGINAL")
print("=" * 60)

original = ["Python", "Git"]

clone = original.copy()

clone.append("Django")

print(f"Original : {original}")
print(f"Clone    : {clone}")
print(f"Same object? {original is clone}")


# ============================================================
# SHALLOW COPY
# ============================================================

print("\n" + "=" * 60)
print("SHALLOW COPY")
print("=" * 60)

original = [["Sara", 90], ["Omar", 85]]

clone = original.copy()

clone[0][1] = 95

print(f"Original : {original}")
print(f"Clone    : {clone}")
print(f"Same inner list? {original[0] is clone[0]}")


# ============================================================
# DEEP COPY
# ============================================================

print("\n" + "=" * 60)
print("DEEP COPY")
print("=" * 60)

from copy import deepcopy

clone = deepcopy(original)

clone[0][1] = 95

print(f"Original : {original}")
print(f"Clone    : {clone}")
print(f"Same inner list? {original[0] is clone[0]}")


# ============================================================
# LIST VS SET
# ============================================================

print("\n" + "=" * 60)
print("LIST VS SET MEMBERSHIP")
print("=" * 60)

names = ["Sara", "Omar", "Lina"]

print(f"Names: {names}")
print(f'"Lina" in list: {"Lina" in names}')

name_set = set(names)

print(f"Names set: {name_set}")
print(f'"Lina" in set: {"Lina" in name_set}')


# ============================================================
# DICTIONARY LOOKUP
# ============================================================

print("\n" + "=" * 60)
print("DICTIONARY LOOKUP")
print("=" * 60)

students = [
    {"id": 101, "name": "Sara"},
    {"id": 102, "name": "Omar"}
]

students_by_id = {
    student["id"]: student
    for student in students
}

print(f"Student with ID 102: {students_by_id[102]['name']}")


# ============================================================
# LAB 1 - SQUARING NUMBERS
# ============================================================

print("\n" + "=" * 60)
print("LAB 1 - SQUARING NUMBERS")
print("=" * 60)

numbers = [1, 2, 3, 4, 5]

squared_numbers = []

for number in numbers:
    squared_numbers.append(number ** 2)

print(f"Using loop          : {squared_numbers}")

comp_numbers = [
    number ** 2
    for number in numbers
]

print(f"Using comprehension : {comp_numbers}")


# ============================================================
# LAB 2 - VAT
# ============================================================

print("\n" + "=" * 60)
print("LAB 2 - CALCULATE VAT")
print("=" * 60)

prices = [10, 25, 40]

prices_with_vat = [
    round(price * 1.15, 2)
    for price in prices
]

print(f"Original prices : {prices}")
print(f"Prices with VAT : {prices_with_vat}")


# ============================================================
# LAB 3 - NAME CASES
# ============================================================

print("\n" + "=" * 60)
print("LAB 3 - NAME CASES")
print("=" * 60)

names = ["Sara", "ArEej", "Mashel", "nasser"]

lower = [
    name.lower()
    for name in names
]

upper = [
    name.upper()
    for name in names
]

titled = [
    name.title()
    for name in names
]

print(f"Lowercase : {lower}")
print(f"Uppercase : {upper}")
print(f"Title Case: {titled}")


# ============================================================
# LAB 4 - CELSIUS TO FAHRENHEIT
# ============================================================

print("\n" + "=" * 60)
print("LAB 4 - CELSIUS TO FAHRENHEIT")
print("=" * 60)

c_temp = [20, 33, 15, 6]

f_temp = [
    temp * 1.8 + 32
    for temp in c_temp
    if temp > 0
]

print(f"Celsius    : {c_temp}")
print(f"Fahrenheit : {f_temp}")


# ============================================================
# LAB 5 - FLATTEN NESTED LIST
# ============================================================

print("\n" + "=" * 60)
print("LAB 5 - FLATTEN NESTED LIST")
print("=" * 60)

nested_list = [[1, 2], [3, 4], [5, 6]]

flattened_list = []

for row in nested_list:
    for column in row:
        flattened_list.append(column)

print(f"Using loop          : {flattened_list}")

comp_flattened_list = [
    column
    for row in nested_list
    for column in row
]

print(f"Using comprehension : {comp_flattened_list}")


# ============================================================
# LAB 6 - PASS OR FAIL
# ============================================================

print("\n" + "=" * 60)
print("LAB 6 - PASS OR FAIL")
print("=" * 60)

scores = [45, 55, 65, 75, 86, 95]

passing_score = [
    "Pass" if score >= 60 else "Failed"
    for score in scores
]

for score, result in zip(scores, passing_score):
    print(f"Score: {score:>3}  →  {result}")


# ============================================================
# LAB 7 - UNIQUE SKILLS
# ============================================================

print("\n" + "=" * 60)
print("LAB 7 - UNIQUE SKILLS")
print("=" * 60)

skills = ["PYTHON", "Git", "python", "javascript", "SQL", "git"]

skills_set = {
    skill.lower()
    for skill in skills
}

print(f"Original skills : {skills}")
print(f"Unique skills   : {skills_set}")


# ============================================================
# LAB 8 - COUNT CHARACTERS
# ============================================================

print("\n" + "=" * 60)
print("LAB 8 - COUNT CHARACTERS")
print("=" * 60)

list_name = ["Sara", "Dalal", "Nora", "Taif"]

counted_Chars = [
    {
        "name": name,
        "count": len(name)
    }
    for name in list_name
]

for person in counted_Chars:
    print(f"{person['name']:<10} → {person['count']} characters")


# ============================================================
# LAB 9 - GENERATOR
# ============================================================

print("\n" + "=" * 60)
print("LAB 9 - GENERATOR EXPRESSION")
print("=" * 60)

new_names = ["Mada", "Khadija", "Yamam", "Meshael"]

upp = (
    name.upper()
    for name in new_names
)

print(f"First value : {next(upp)}")
print(f"Second value: {next(upp)}")

remaining = list(upp)

print(f"Remaining values: {remaining}")

print("\nGenerator after being consumed:")
for x in upp:
    print(x)

print("\n" + "=" * 60)
print("ALL LABS COMPLETED")
print("=" * 60)