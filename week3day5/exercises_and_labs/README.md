
# 🐍 Python Fundamentals & Practice Labs

A collection of Python exercises covering **lists, sets, dictionaries, comprehensions, generators, copying, aliasing, and basic performance concepts**.

The project is organized into small labs so each concept can be practiced and understood independently.

---

## 📌 Topics Covered

- 🔢 Range and `sum()`
- 📋 Lists and list methods
- 🔗 Aliasing and object identity
- 📑 Shallow copy vs deep copy
- 🔍 List vs Set membership
- 🗂️ Dictionary lookups
- ⚡ List comprehensions
- 🧮 Conditional comprehensions
- 🪆 Nested list comprehensions
- 🔤 String transformations
- 🌡️ Temperature conversion
- 💰 VAT calculation
- 🎯 Pass / Fail conditions
- 🔤 Set comprehensions
- 📊 Dictionary comprehensions
- ⚙️ Generator expressions
- ⏱️ Basic Big-O concepts

---

## 📂 Project Structure

```text
python-practice/
│
├── main.py
└── README.md
````

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Move into the project

```bash
cd python-practice
```

### 3. Run the program

```bash
python main.py
```

---

# 🧪 Labs

## Lab 1 — Squaring Numbers

Converts a list of numbers into their squared values.

### Example

```python
numbers = [1, 2, 3, 4, 5]

comp_numbers = [
    number ** 2
    for number in numbers
]
```

### Output

```text
[1, 4, 9, 16, 25]
```

---

## Lab 2 — Calculate VAT

Calculates a **15% VAT** for each price.

```python
prices = [10, 25, 40]

prices_with_vat = [
    round(price * 1.15, 2)
    for price in prices
]
```

### Output

```text
Original prices : [10, 25, 40]
Prices with VAT : [11.5, 28.75, 46.0]
```

---

## Lab 3 — Name Cases

Demonstrates:

* `.lower()`
* `.upper()`
* `.title()`

```python
names = ["Sara", "ArEej", "Mashel", "nasser"]
```

### Output

```text
Lowercase : ['sara', 'areej', 'mashel', 'nasser']
Uppercase : ['SARA', 'AREEJ', 'MASHEL', 'NASSER']
Title Case: ['Sara', 'Areej', 'Mashel', 'Nasser']
```

---

## Lab 4 — Celsius to Fahrenheit

Converts Celsius temperatures to Fahrenheit.

The formula is:

```text
°F = (°C × 1.8) + 32
```

### Output

```text
Celsius    : [20, 33, 15, 6]
Fahrenheit : [68.0, 91.4, 59.0, 42.8]
```

---

## Lab 5 — Flatten a Nested List

Converts a nested list into a single list.

```python
nested_list = [[1, 2], [3, 4], [5, 6]]
```

### Output

```text
Using loop          : [1, 2, 3, 4, 5, 6]
Using comprehension : [1, 2, 3, 4, 5, 6]
```

---

## Lab 6 — Pass or Fail

Uses a conditional expression inside a list comprehension.

```python
scores = [45, 55, 65, 75, 86, 95]
```

A score of `60` or higher is considered a pass.

### Output

```text
Score:  45  →  Failed
Score:  55  →  Failed
Score:  65  →  Pass
Score:  75  →  Pass
Score:  86  →  Pass
Score:  95  →  Pass
```

---

## Lab 7 — Unique Skills

Uses a **set comprehension** to:

1. Convert skills to lowercase.
2. Remove duplicates.

```python
skills = [
    "PYTHON",
    "Git",
    "python",
    "javascript",
    "SQL",
    "git"
]
```

### Result

```text
Original skills : ['PYTHON', 'Git', 'python', 'javascript', 'SQL', 'git']

Unique skills   : {'python', 'git', 'javascript', 'sql'}
```

> **Note:** Sets are unordered, so the displayed order may be different.

---

## Lab 8 — Count Characters

Creates a list of dictionaries containing each person's name and the number of characters in the name.

```python
list_name = ["Sara", "Dalal", "Nora", "Taif"]
```

### Output

```text
Sara       → 4 characters
Dalal      → 5 characters
Nora       → 4 characters
Taif       → 4 characters
```

---

## Lab 9 — Generator Expression

Demonstrates a generator expression using:

```python
upp = (
    name.upper()
    for name in new_names
)
```

Generators produce values **one at a time** instead of creating the entire result immediately.

### Output

```text
First value : MADA
Second value: KHADIJA
Remaining values: ['YAMAM', 'MESHAEL']
```

Once a generator has been consumed, there are no values left:

```text
Generator after being consumed:
```

---

# 🧠 Python Concepts

## Aliasing

When two variables reference the same object:

```python
items = ["Python", "Git"]

alias = items

alias.append("Django")

print(items is alias)
```

Output:

```text
True
```

Both variables refer to the **same list**.

---

## Shallow Copy

A shallow copy creates a new outer list, but nested objects can still be shared.

```python
original = [["Sara", 90], ["Omar", 85]]

clone = original.copy()

clone[0][1] = 95
```

The change affects the nested list inside `original`.

```text
Original : [['Sara', 95], ['Omar', 85]]
Clone    : [['Sara', 95], ['Omar', 85]]

Same inner list? True
```

---

## Deep Copy

`deepcopy()` creates independent copies of nested objects.

```python
from copy import deepcopy

clone = deepcopy(original)
```

Now changing the clone does not affect the original.

```text
Original : [['Sara', 95], ['Omar', 85]]
Clone    : [['Sara', 95], ['Omar', 85]]

Same inner list? False
```

---

# ⚡ List vs Set Lookup

List membership:

```python
"Lina" in names
```

has an average complexity of:

```text
O(n)
```

A set provides average:

```text
O(1)
```

membership lookup.

```python
name_set = set(names)

"Lina" in name_set
```

This makes sets useful when you frequently need to check whether an item exists.

---

# 🗂️ Dictionary Lookup

The project also demonstrates converting a list of students into a dictionary indexed by ID.

```python
students_by_id = {
    student["id"]: student
    for student in students
}
```

This allows direct lookup:

```python
students_by_id[102]["name"]
```

### Output

```text
Omar
```

---

# 💻 Example CLI Output

When the program runs, the output is organized into sections:

```text
============================================================
BASIC PYTHON EXAMPLES
============================================================

Sum of squares: 333332833333500000

Formatted name: Sara

============================================================
ALIASING
============================================================

items : ['Python', 'Git', 'Django', 'Django']
alias : ['Python', 'Git', 'Django', 'Django']
Same object? True

============================================================
COPY VS ORIGINAL
============================================================

Original : ['Python', 'Git']
Clone    : ['Python', 'Git', 'Django']
Same object? False

============================================================
LAB 1 - SQUARING NUMBERS
============================================================

Using loop          : [1, 4, 9, 16, 25]
Using comprehension : [1, 4, 9, 16, 25]

============================================================
LAB 2 - CALCULATE VAT
============================================================

Original prices : [10, 25, 40]
Prices with VAT : [11.5, 28.75, 46.0]

============================================================
LAB 3 - NAME CASES
============================================================

Lowercase : ['sara', 'areej', 'mashel', 'nasser']
Uppercase : ['SARA', 'AREEJ', 'MASHEL', 'NASSER']
Title Case: ['Sara', 'Areej', 'Mashel', 'Nasser']

============================================================
LAB 4 - CELSIUS TO FAHRENHEIT
============================================================

Celsius    : [20, 33, 15, 6]
Fahrenheit : [68.0, 91.4, 59.0, 42.8]

============================================================
LAB 5 - FLATTEN NESTED LIST
============================================================

Using loop          : [1, 2, 3, 4, 5, 6]
Using comprehension : [1, 2, 3, 4, 5, 6]

============================================================
LAB 6 - PASS OR FAIL
============================================================

Score:  45  →  Failed
Score:  55  →  Failed
Score:  65  →  Pass
Score:  75  →  Pass
Score:  86  →  Pass
Score:  95  →  Pass

============================================================
LAB 7 - UNIQUE SKILLS
============================================================

Original skills : ['PYTHON', 'Git', 'python', 'javascript', 'SQL', 'git']
Unique skills   : {'python', 'git', 'javascript', 'sql'}

============================================================
LAB 8 - COUNT CHARACTERS
============================================================

Sara       → 4 characters
Dalal      → 5 characters
Nora       → 4 characters
Taif       → 4 characters

============================================================
LAB 9 - GENERATOR EXPRESSION
============================================================

First value : MADA
Second value: KHADIJA
Remaining values: ['YAMAM', 'MESHAEL']

Generator after being consumed:

============================================================
ALL LABS COMPLETED
============================================================
```

---

# 🎯 Learning Goals

By completing these exercises, you will practice:

* Writing Python comprehensions
* Understanding mutable objects
* Understanding object identity with `is`
* Using `.copy()` and `deepcopy()`
* Choosing between lists and sets
* Building dictionaries efficiently
* Working with nested data
* Using conditional expressions
* Understanding generators
* Thinking about basic algorithm complexity

---

## 🛠️ Requirements

* Python 3.10+
* No external libraries required

---

## 👩‍💻 Author

**Sara**

Python Practice & Fundamentals Labs

---

⭐ If this project helped you practice Python, consider giving the repository a star!
