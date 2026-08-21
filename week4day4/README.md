
# ============================================================
#                       PYTHON OOP LABS
# ============================================================


# ============================================================
# >>>>>>>>>>>>>>>>>>>>>>> LAB 5 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ============================================================
# Name Mangling + Property
#
# Concepts:
# - Private attributes
# - Name mangling
# - @property
# - Getter
# - Setter
# - Data validation
# - Calculating an average
# ============================================================

print("\n" + "=" * 60)
print("LAB 5: NAME MANGLING + PROPERTY")
print("=" * 60)


class Student:

    # Private class attribute
    __enrolled = True

    def __init__(self, name, enrolled=True):
        self.name = name
        self.score = []
        self._enrolled = enrolled

    def add_score(self, score):
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100")

        self.score.append(score)

    # Getter
    @property
    def enrolled(self):
        return self._enrolled

    # Setter
    @enrolled.setter
    def enrolled(self, status):
        self._enrolled = status

    # Property
    @property
    def average(self):
        if not self.score:
            return 0

        return sum(self.score) / len(self.score)


student = Student("Khalifa")

student.add_score(80)
student.add_score(90)
student.add_score(100)

print("Student name:", student.name)
print("Student scores:", student.score)
print("Student average:", student.average)

print("Enrollment status:", student.enrolled)

student.enrolled = False

print("Updated enrollment status:", student.enrolled)


# Demonstrate name mangling
print("Private class attribute:", Student._Student__enrolled)


# ============================================================
# >>>>>>>>>>>>>>>>>>>>>>> LAB 6 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ============================================================
# Inheritance + Static Method
#
# Concepts:
# - Inheritance
# - super()
# - Parent class
# - Child class
# - Static methods
# - String methods
# ============================================================

print("\n" + "=" * 60)
print("LAB 6: INHERITANCE + STATIC METHOD")
print("=" * 60)


class Food:

    def __init__(self, name):
        self.name = name

    def showName(self):
        return self.name


class Fruites(Food):

    def __init__(self, name, cal):
        super().__init__(name)
        self.cal = cal

    @staticmethod
    def stripName(newName):
        return newName.strip()


myFruite = Fruites("Apple", 200)

print("Fruit name:", myFruite.showName())
print("Fruit calories:", myFruite.cal)
print("Stripped name:", myFruite.stripName("   Fa   "))


# ============================================================
#                    ALL LABS COMPLETED
# ============================================================

print("\n" + "=" * 60)
print("ALL LABS COMPLETED")
print("=" * 60)
```

# Expected Output

```text
============================================================
LAB 5: NAME MANGLING + PROPERTY
============================================================
Student name: Khalifa
Student scores: [80, 90, 100]
Student average: 90.0
Enrollment status: True
Updated enrollment status: False
Private class attribute: True

============================================================
LAB 6: INHERITANCE + STATIC METHOD
============================================================
Fruit name: Apple
Fruit calories: 200
Stripped name: Fa

============================================================
ALL LABS COMPLETED
============================================================
```

# `README.md`

# 🐍 Python OOP Labs

This project contains practical Python Object-Oriented Programming labs covering **name mangling, properties, getters, setters, inheritance, `super()`, and static methods**.

The labs are organized in one Python file and each lab has a clearly marked section and output.

---

# 📚 Labs

## Lab 5 — Name Mangling + Property

This lab demonstrates how Python can control access to attributes using private attributes and properties.

### Concepts

* Private attributes
* Name mangling
* `@property`
* Getter
* Setter
* Data validation
* Lists
* Calculating an average

### Student Class

The `Student` class contains:

```text
name
score
_enrolled
__enrolled
```

The student can add scores using:

```python
student.add_score(80)
```

The program prevents scores outside the range:

```text
0 - 100
```

### Property

The `average` property calculates the student's average score:

```python
student.average
```

Instead of calling:

```python
student.average()
```

because `average` is defined using:

```python
@property
```

### Getter and Setter

The `enrolled` property allows the program to read and update the enrollment status:

```python
print(student.enrolled)

student.enrolled = False
```

### Name Mangling

The class contains a private attribute:

```python
__enrolled = True
```

Python internally changes its name to:

```text
_Student__enrolled
```

It can therefore be accessed with:

```python
Student._Student__enrolled
```

for demonstration purposes.

### Expected Output

```text
============================================================
LAB 5: NAME MANGLING + PROPERTY
============================================================
Student name: Khalifa
Student scores: [80, 90, 100]
Student average: 90.0
Enrollment status: True
Updated enrollment status: False
Private class attribute: True
```

---

# Lab 6 — Inheritance + Static Method

This lab demonstrates inheritance using a parent class and a child class.

### Concepts

* Inheritance
* Parent class
* Child class
* `super()`
* Static methods
* String manipulation

---

## Parent Class — `Food`

The `Food` class stores the food name:

```python
class Food:
    def __init__(self, name):
        self.name = name
```

It also contains:

```python
showName()
```

which returns the food name.

---

## Child Class — `Fruites`

`Fruites` inherits from `Food`:

```python
class Fruites(Food):
```

The child class uses:

```python
super().__init__(name)
```

to call the constructor of the parent class.

It also stores calories:

```python
self.cal = cal
```

---

## Static Method

The `stripName()` method is defined using:

```python
@staticmethod
```

It removes spaces from the beginning and end of a string.

Example:

```python
myFruite.stripName("   Fa   ")
```

returns:

```text
Fa
```

### Expected Output

```text
============================================================
LAB 6: INHERITANCE + STATIC METHOD
============================================================
Fruit name: Apple
Fruit calories: 200
Stripped name: Fa
```

---

# 🖥️ Complete Expected Output

When the complete file is executed:

```text
============================================================
LAB 5: NAME MANGLING + PROPERTY
============================================================
Student name: Khalifa
Student scores: [80, 90, 100]
Student average: 90.0
Enrollment status: True
Updated enrollment status: False
Private class attribute: True

============================================================
LAB 6: INHERITANCE + STATIC METHOD
============================================================
Fruit name: Apple
Fruit calories: 200
Stripped name: Fa

============================================================
ALL LABS COMPLETED
============================================================
```

---

# 📂 Project Structure

```text
python-oop-labs/
│
├── labs.py
└── README.md
```

---

# 🧠 Concepts Summary

| Lab   | Concepts                                  |
| ----- | ----------------------------------------- |
| Lab 5 | Name Mangling, Properties, Getter, Setter |
| Lab 5 | Data Validation, Lists, Average           |
| Lab 6 | Inheritance, `super()`, Static Methods    |
| Lab 6 | Parent and Child Classes                  |

---

# 🎯 Learning Goals

After completing these labs, you should be able to:

* Create private attributes
* Understand Python name mangling
* Use `@property`
* Create getters and setters
* Validate object data
* Create inheritance relationships
* Use `super()`
* Create static methods
* Reuse functionality from parent classes
* Work with objects and methods

---

# 🏁 Completion

```text
Lab 5  ✅
Lab 6  ✅
```

**Python OOP Labs — Completed ✅**
