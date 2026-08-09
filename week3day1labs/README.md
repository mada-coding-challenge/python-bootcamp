# 🐍 Week 3 — Day 1

## Python Functions

> Week 3 started with one of the most important concepts in Python: **functions**.
> We learned how to create reusable blocks of code, pass information into functions, return results, use default parameters, work with nested functions, and document our functions using docstrings.

---

## 📚 What We Learned

Functions allow us to organize a program into smaller, reusable pieces.

Instead of writing the same code repeatedly, we can define a function once and call it whenever we need it.

### Main concepts covered:

```text
🔧 Function Definition
📞 Function Calls
📥 Parameters
🎯 Arguments
↩️ Return Values
⚙️ Default Parameters
🪆 Nested Functions
📦 Function Scope
📖 Docstrings
```

---

## 🏆 Practice — Calculate Grade

We started with a function that receives a student's score and determines their grade.

```python
calculate_grade(score)
```

The function uses conditional statements to determine the result:

```text
90+  → 🏆 A
80+  → 🥇 B
70+  → 🥈 C
60+  → 🥉 D
<60  → F
```

### Concepts practiced

* Defining a function
* Passing an argument
* Using `if / elif / else`
* Returning a value
* Calling a function inside `print()`

### Key idea

The function **returns** the grade instead of printing it directly.

```text
Score
  ↓
calculate_grade()
  ↓
Check conditions
  ↓
Return grade
  ↓
Print result
```

---

## 🧪 Lab 1 — Creating & Calling a Function

We created our first simple function:

```python
def great():
    print("Welcome to Python")
```

Then we called it:

```python
great()
```

### 💡 What we learned

The `def` keyword is used to define a function.

Defining a function does not execute it. The function runs when we **call** it.

```text
def great()
     ↓
Function created

great()
     ↓
Function executed
```

---

## 🧪 Lab 2 — Displaying a Menu

We created a reusable menu function:

```python
def show_menu():
```

The same function was called multiple times.

### 💡 What we learned

Functions allow us to **reuse code**.

Instead of writing the menu repeatedly, we can simply use:

```python
show_menu()
```

This makes programs easier to organize and maintain.

---

## 🧪 Lab 3 — Nested Functions & Scope

We created a function inside another function.

```python
def unknownScope():

    def gotFunc():
        ...
```

This introduced the concept of **nested functions** and function scope.

### 💡 What we learned

A function can be defined inside another function.

The inner function belongs to the scope of the outer function.

```text
unknownScope()
      │
      └── gotFunc()
```

We also observed the order in which statements execute inside functions.

---

## 🧪 Lab 4 — Function Parameters

We created a function that accepts a parameter:

```python
def great_student(name):
```

Then we passed a value:

```python
great_student("Sara and Taif")
```

### 💡 Parameter vs Argument

These two terms are important:

| Term      | Meaning                             |
| --------- | ----------------------------------- |
| Parameter | Variable defined in the function    |
| Argument  | Actual value passed to the function |

Example:

```python
def great_student(name):
```

`name` → parameter

```python
great_student("Sara and Taif")
```

`"Sara and Taif"` → argument

---

## 🧪 Lab 5 — Multiple Parameters

We created a function with two parameters:

```python
def show_booking(destination, nights):
```

Then we called it with different values:

```python
show_booking("Jeddah", 2)
show_booking("Doha", 5)
```

### 💡 What we learned

A function can accept multiple pieces of information.

```text
Destination + Nights
        ↓
 show_booking()
        ↓
 Booking Information
```

The same function can therefore handle different bookings without rewriting the function.

---

## 🧪 Lab 6 — Default Parameters, Return Values & Docstrings

The final lab combined several important function concepts.

### ⚙️ Default Parameters

We created:

```python
def getVAT(total, rate=0.15):
```

The `rate` parameter has a default value of `0.15`.

Therefore:

```python
getVAT(154)
```

automatically uses:

```text
rate = 0.15
```

But we can also provide another rate:

```python
getVAT(154, 0.05)
```

This allows the function to be flexible.

---

### ↩️ Return Values

The function calculates the total and returns it:

```python
return subTotal
```

The returned value can then be used elsewhere:

```python
print(getVAT(154))
```

### 💡 Important idea

`return` sends a value **out of the function**.

```text
Input
  ↓
Function
  ↓
Calculation
  ↓
return
  ↓
Result
```

---

### 📖 Docstrings

We also added documentation inside the function:

```python
"""This function will get the total with VAT added to it,
and return the sum"""
```

This is called a **docstring**.

A docstring explains what a function does and can be accessed using:

```python
getVAT.__doc__
```

### 💡 What we learned

Docstrings make functions easier for other developers — and our future selves — to understand.

---

## 🧠 Concepts Practiced

| Concept            | What We Learned                            |
| ------------------ | ------------------------------------------ |
| `def`              | Define a function                          |
| Function call      | Execute a function                         |
| Parameters         | Receive data inside a function             |
| Arguments          | Pass values into a function                |
| `return`           | Send a result back                         |
| Default parameters | Provide a default value                    |
| Nested functions   | Define functions inside functions          |
| Scope              | Understand where functions/variables exist |
| Docstrings         | Document what a function does              |
| `__doc__`          | Access a function's documentation          |
| Reusability        | Use the same function multiple times       |

---

## 🔧 Why Functions Matter

Without functions, programs can become repetitive:

```text
❌ Repeated code
❌ Harder to maintain
❌ Difficult to organize
❌ More chances for mistakes
```

With functions:

```text
✅ Reusable
✅ Organized
✅ Easier to understand
✅ Easier to test
✅ Easier to maintain
```

A function can be thought of as a small machine:

```text
             📥 INPUT
                ↓
        ┌───────────────┐
        │   🔧 FUNCTION │
        │               │
        │    PROCESS    │
        └───────────────┘
                ↓
             📤 OUTPUT
```

---

## 🎯 Week 3 — Day 1 Takeaway

Day 1 introduced functions as a fundamental tool for writing clean and reusable Python programs.

We progressed from:

```text
🔧 Define a function
       ↓
📞 Call a function
       ↓
📥 Pass arguments
       ↓
⚙️ Use parameters
       ↓
↩️ Return values
       ↓
⚙️ Use default values
       ↓
🪆 Understand scope
       ↓
📖 Document functions
```

The main lesson is:

> **Write code once, then reuse it whenever you need it.**

Functions will become especially important as our projects grow because they allow large programs to be divided into smaller, manageable pieces.

---

## 📸 Terminal Output

The terminal output for **Week 3 — Day 1** demonstrates the execution of the practice and six labs, including function calls, parameters, VAT calculations, and function documentation.

<p align="center">
  <img src="image.png" width="850" alt="Week 3 Day 1 Python Functions Output">
</p>

---

<div align="center">

### 🐍 WEEK 3 • DAY 1

**Define • Call • Pass • Return • Reuse**

</div>
