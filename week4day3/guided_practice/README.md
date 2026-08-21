# 🐍 Python JSON — Guided Practice

A beginner-friendly guided practice for working with **JSON data in Python**.

This practice combines JSON file handling, `pathlib`, exception handling, custom exceptions, and data validation.

---

## 🎯 Learning Goals

By completing this guided practice, you will learn how to:

* Create Python data structures for JSON
* Create directories using `Path`
* Create JSON files
* Write data using `json.dump()`
* Read data using `json.load()`
* Handle file-related exceptions
* Handle invalid JSON
* Create custom exceptions
* Validate student data
* Use `try` and `except`

---

# 📚 Guided Practice

## Exercise 1 — Create Student Data

Create a list of dictionaries containing student information.

Each student has:

* `name`
* `score`

Example:

```python
students = [
    {"name": "Sara", "score": 92},
    {"name": "Ali", "score": 85}
]
```

### Expected Output

```text
============================================================
EXERCISE 1: CREATE STUDENT DATA
============================================================
Student data:
[{'name': 'Sara', 'score': 92}, {'name': 'Ali', 'score': 85}]
```

---

## Exercise 2 — Create Data Directory

Create a directory called:

```text
data
```

Then create a path for:

```text
data/students.json
```

### Expected Output

```text
============================================================
EXERCISE 2: CREATE DATA DIRECTORY
============================================================
Directory: data
JSON file: data/students.json
```

---

## Exercise 3 — Write JSON File

Save the student data to:

```text
data/students.json
```

Use:

```python
json.dump()
```

with:

```python
indent=2
```

### Expected Output

```text
============================================================
EXERCISE 3: WRITE JSON FILE
============================================================
Student data saved successfully.
File: data/students.json
```

The resulting JSON file will contain:

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

## Exercise 4 — Read JSON File

Open the JSON file and load the data using:

```python
json.load()
```

The loaded data should be stored in:

```python
loaded
```

### Expected Output

```text
============================================================
EXERCISE 4: READ JSON FILE
============================================================
Student data loaded successfully.
[{'name': 'Sara', 'score': 92}, {'name': 'Ali', 'score': 85}]
```

---

## Exercise 5 — Custom Exception

Create a custom exception called:

```python
InvalidStudentError
```

It should inherit from:

```python
Exception
```

### Expected Output

```text
============================================================
EXERCISE 5: CUSTOM EXCEPTION
============================================================
InvalidStudentError created successfully.
```

---

## Exercise 6 — Validate Students

Create a function:

```python
validate_student()
```

The function checks the student data.

A student is invalid when:

* The name is empty.
* The score is less than `0`.

Valid students should be printed.

Invalid data should raise:

```python
InvalidStudentError
```

### Expected Output

```text
============================================================
EXERCISE 6: VALIDATE STUDENTS
============================================================
{'name': 'Sara', 'score': 92}
{'name': 'Ali', 'score': 85}
```

---

## Exercise 7 — Run Validation

Use `try` and `except` to run the validation function.

The custom exception should be caught using:

```python
except InvalidStudentError as error:
```

### Expected Output

```text
============================================================
EXERCISE 7: RUN VALIDATION
============================================================
{'name': 'Sara', 'score': 92}
{'name': 'Ali', 'score': 85}
```

---

## Exercise 8 — Final JSON Practice

Add another student:

```text
Lina → 95
```

Then validate the complete list.

### Expected Output

```text
============================================================
EXERCISE 8: FINAL JSON PRACTICE
============================================================
Updated students:
{'name': 'Sara', 'score': 92}
{'name': 'Ali', 'score': 85}
{'name': 'Lina', 'score': 95}
```

---

# 🖥️ Complete Expected Output

When the entire Python file is executed, the terminal should display:

```text
============================================================
EXERCISE 1: CREATE STUDENT DATA
============================================================
Student data:
[{'name': 'Sara', 'score': 92}, {'name': 'Ali', 'score': 85}]

============================================================
EXERCISE 2: CREATE DATA DIRECTORY
============================================================
Directory: data
JSON file: data/students.json

============================================================
EXERCISE 3: WRITE JSON FILE
============================================================
Student data saved successfully.
File: data/students.json

============================================================
EXERCISE 4: READ JSON FILE
============================================================
Student data loaded successfully.
[{'name': 'Sara', 'score': 92}, {'name': 'Ali', 'score': 85}]

============================================================
EXERCISE 5: CUSTOM EXCEPTION
============================================================
InvalidStudentError created successfully.

============================================================
EXERCISE 6: VALIDATE STUDENTS
============================================================
{'name': 'Sara', 'score': 92}
{'name': 'Ali', 'score': 85}

============================================================
EXERCISE 7: RUN VALIDATION
============================================================
{'name': 'Sara', 'score': 92}
{'name': 'Ali', 'score': 85}

============================================================
EXERCISE 8: FINAL JSON PRACTICE
============================================================
Updated students:
{'name': 'Sara', 'score': 92}
{'name': 'Ali', 'score': 85}
{'name': 'Lina', 'score': 95}

============================================================
ALL JSON GUIDED PRACTICE COMPLETED
============================================================
```

---

# 📂 Project Structure

```text
json-guided-practice/
│
├── json_guided_practice.py
├── README.md
│
└── data/
    └── students.json
```

---

# ▶️ How to Run

Run the Python file from the terminal:

```bash
python json_guided_practice.py
```

The program automatically creates the `data` directory and `students.json` file.

---

# 🧠 JSON Concepts

### `json.dump()`

Used to write Python data into a JSON file:

```python
json.dump(students, file, indent=2)
```

### `json.load()`

Used to read JSON data from a file:

```python
loaded = json.load(file)
```

### `Path`

Used to work with files and directories:

```python
data_dir = Path("data")
data_file = data_dir / "students.json"
```

### Custom Exception

Used to create application-specific errors:

```python
class InvalidStudentError(Exception):
    pass
```

### Exception Handling

Used to safely handle errors:

```python
try:
    validate_student(loaded)
except InvalidStudentError as error:
    print(error)
```

---

# 🔑 Error Handling

The practice demonstrates handling:

| Exception             | Meaning                  |
| --------------------- | ------------------------ |
| `FileNotFoundError`   | JSON file does not exist |
| `PermissionError`     | File cannot be accessed  |
| `JSONDecodeError`     | JSON content is invalid  |
| `InvalidStudentError` | Student data is invalid  |


