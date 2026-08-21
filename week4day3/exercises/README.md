# 🐍 Python Data Handling & Exception Exercises

A collection of practical Python exercises covering **CSV, JSON, file handling, input validation, exception handling, and custom exceptions**.

The exercises are organized in one Python file and each exercise prints its own title and output.

---

# 📚 Exercises

## Exercise 1 — Write CSV File

Create a CSV file called:

```text
students.csv
```

The file contains student names and their courses.

### Concepts

* `csv`
* `csv.writer()`
* `writerow()`
* Writing files
* Reading file contents

### Expected Output

```text
============================================================
EXERCISE 1: WRITE CSV FILE
============================================================
students.csv created successfully.

CSV content:
name,course
Sara,Python
Ali,Django
```

---

## Exercise 2 — Write and Read JSON

Create a JSON file containing student names and scores.

The data is written using:

```python
json.dump()
```

and loaded using:

```python
json.load()
```

### Expected Output

```text
============================================================
EXERCISE 2: WRITE AND READ JSON
============================================================
students.json created successfully.
First student: Sara
```

The JSON file will contain:

```json
[
  {
    "name": "Sara",
    "score": 92
  },
  {
    "name": "Ali",
    "score": 85
  }
]
```

---

## Exercise 3 — Handle Invalid Input

Demonstrate how `ValueError` can be caught when converting invalid data to an integer.

### Example

```python
try:
    score = int(score_input)
except ValueError:
    print("Enter a whole number")
```

### Expected Output

```text
============================================================
EXERCISE 3: HANDLE INVALID INPUT
============================================================
Enter a whole number
Program continues
```

---

## Exercise 4 — Handle Missing File

Use `pathlib` to read a file and handle possible errors.

The exercise demonstrates:

```python
FileNotFoundError
PermissionError
```

### Expected Output

```text
============================================================
EXERCISE 4: HANDLE MISSING FILE
============================================================
Student file not found
```

If the file exists on the user's machine, the output will instead display its contents.

---

## Exercise 5 — Try, Except, Else, Finally

This exercise demonstrates the four major parts of exception handling:

```text
try
except
else
finally
```

The program attempts to load `students.txt`.

### Expected Output

```text
============================================================
EXERCISE 5: TRY / EXCEPT / ELSE / FINALLY
============================================================
File loaded successfully:
Sara
Ali

Load attempt finished
```

### What Each Block Does

| Block     | Purpose                       |
| --------- | ----------------------------- |
| `try`     | Code that may cause an error  |
| `except`  | Handles the error             |
| `else`    | Runs when no error occurs     |
| `finally` | Runs regardless of the result |

---

## Exercise 6 — Validate Score

Create a function that only accepts scores between `0` and `100`.

```python
def validate_score(score):
    if not 0 <= score <= 100:
        raise ValueError("Score must be 0 to 100")
```

The example uses:

```text
120
```

which is invalid.

### Expected Output

```text
============================================================
EXERCISE 6: VALIDATE SCORE
============================================================
Score must be 0 to 100
```

---

## Exercise 7 — Custom Exception

Create a custom exception:

```python
class StudentNotFoundError(Exception):
    pass
```

The `find_student()` function searches for a student by name.

If the student cannot be found, the custom exception is raised.

The program searches for:

```text
Ali
```

but only `Sara` exists.

### Expected Output

```text
============================================================
EXERCISE 7: CUSTOM EXCEPTION
============================================================
Missing student: Ali
```

---

# 🖥️ Complete Expected Output

When the complete Python file is executed:

```text
============================================================
EXERCISE 1: WRITE CSV FILE
============================================================
students.csv created successfully.

CSV content:
name,course
Sara,Python
Ali,Django

============================================================
EXERCISE 2: WRITE AND READ JSON
============================================================
students.json created successfully.
First student: Sara

============================================================
EXERCISE 3: HANDLE INVALID INPUT
============================================================
Enter a whole number
Program continues

============================================================
EXERCISE 4: HANDLE MISSING FILE
============================================================
Student file not found

============================================================
EXERCISE 5: TRY / EXCEPT / ELSE / FINALLY
============================================================
File loaded successfully:
Sara
Ali

Load attempt finished

============================================================
EXERCISE 6: VALIDATE SCORE
============================================================
Score must be 0 to 100

============================================================
EXERCISE 7: CUSTOM EXCEPTION
============================================================
Missing student: Ali

============================================================
ALL DATA HANDLING EXERCISES COMPLETED
============================================================
```

---

# 📂 Project Structure

```text
python-data-handling/
│
├── data_handling_exercises.py
├── README.md
│
├── students.csv
├── students.json
│
└── students.txt
```

The files are created or modified when the Python program runs.

---

# 🧠 Concepts Summary

| Exercise   | Main Concepts                                  |
| ---------- | ---------------------------------------------- |
| Exercise 1 | CSV, `csv.writer()`, files                     |
| Exercise 2 | JSON, `json.dump()`, `json.load()`             |
| Exercise 3 | `ValueError`, input validation                 |
| Exercise 4 | `Path`, `FileNotFoundError`, `PermissionError` |
| Exercise 5 | `try`, `except`, `else`, `finally`             |
| Exercise 6 | Validation, `raise`, `ValueError`              |
| Exercise 7 | Custom exceptions                              |

---

# 🔑 Important Functions

### CSV

```python
csv.writer(file)
```

Writes rows to a CSV file.

### JSON

```python
json.dump(data, file, indent=2)
```

Writes Python data to JSON.

```python
json.load(file)
```

Reads JSON data into Python.

### Pathlib

```python
Path("students.txt").read_text()
```

Reads text from a file.

### Raise an Exception

```python
raise ValueError("Score must be 0 to 100")
```

Manually creates an error when data is invalid.

### Custom Exception

```python
class StudentNotFoundError(Exception):
    pass
```

Creates an application-specific exception.

---

# 🎯 Learning Goals

After completing these exercises, you should be able to:

* Create and write CSV files
* Read CSV data
* Create and read JSON files
* Work with dictionaries and lists
* Handle invalid user input
* Handle missing files
* Handle permission errors
* Use `try` / `except`
* Use `else` and `finally`
* Validate data
* Raise built-in exceptions
* Create custom exceptions
* Build safer Python programs


