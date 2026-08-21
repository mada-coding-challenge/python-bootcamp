# 📁 Python File Handling Exercises

A collection of beginner-friendly Python exercises for practicing **file handling** using Python's `pathlib` module.

The exercises progress from reading and writing simple text files to working with directories, file paths, logs, lists, and Unicode text.

---

## 📚 Exercises

### Exercise 1 — Read a File

Learn how to:

* Create a `Path` object
* Open a file
* Read file contents
* Use `with`
* Check `file.closed`

---

### Exercise 2 — Working With Paths

Learn how to:

* Create directories
* Check whether a path is a directory
* Check whether a file exists
* Access the file name
* Access the file extension
* Build paths using `/`

---

### Exercise 3 — Append to a File

Learn how to use append mode:

```text
"a"
```

New content is added to the end of the existing file.

The exercise also demonstrates reading the updated file.

---

### Exercise 4 — Read a File Line by Line

Learn how to:

* Loop through a file
* Read one line at a time
* Use `strip()`
* Ignore empty lines

Example:

```python
for line in file:
    name = line.strip()
```

---

### Exercise 5 — Write to a File

Learn how to use:

```text
"w"
```

Write mode replaces the existing contents of the file.

The exercise also demonstrates that `write()` returns the number of characters written.

---

### Exercise 6 — Activity Log

Learn how to create and update a simple log file using append mode.

Example:

```text
Student enrolled: Sara
```

Every new activity can be added to the end of the log.

---

### Exercise 7 — Write a List to a File

Learn how to:

* Store names in a list
* Use `join()`
* Add newline characters
* Write multiple values to a file
* Work with Unicode text

Example:

```text
Sara
نورة
Ali
```

---

### Exercise 8 — Final File Practice

The final exercise combines the previous concepts.

It:

1. Creates a list of students.
2. Writes the students to a file.
3. Opens the file.
4. Reads the students line by line.
5. Displays each student.
6. Counts the total number of students.

---

# 🧠 File Modes

Python provides several common file modes:

| Mode | Purpose                                             |
| ---- | --------------------------------------------------- |
| `r`  | Read an existing file                               |
| `w`  | Write and replace existing content                  |
| `a`  | Append to existing content                          |
| `x`  | Create a new file only if it does not already exist |

---

# 📂 Project Structure

```text
file-handling/
│
├── file_handling_exercises.py
├── README.md
│
├── notes.txt
├── students.txt
├── activity.log
│
└── data/
    └── students.txt
```

The `.txt` and `.log` files are generated or modified when the Python program runs.

---

# ▶️ How to Run

Run the Python file from the terminal:

```bash
python file_handling_exercises.py
```

Each exercise will print its title and output separately.

---

# 🖥️ Expected Output

## Part 1 — Exercises 1–3

```text
============================================================
EXERCISE 1: READ A FILE
============================================================
File content:
Python is easy to learn.
Practice makes progress.

File closed: True

============================================================
EXERCISE 2: WORKING WITH PATHS
============================================================
Is directory: True
Does students.txt exist: False
Full path: data/students.txt
File name: students.txt
File suffix: .txt

============================================================
EXERCISE 3: APPEND TO A FILE
============================================================
New note added.

Updated file:
Python is easy to learn.
Practice makes progress.
New note
```

---

## Part 2 — Exercises 4–6

```text
============================================================
EXERCISE 4: READ FILE LINE BY LINE
============================================================
Students:
Sara
Ali
Omar
Lina

============================================================
EXERCISE 5: WRITE TO A FILE
============================================================
Characters written: 9

File content:
Sara
Ali

============================================================
EXERCISE 6: ACTIVITY LOG
============================================================
Activity saved.

Activity log:
Student enrolled: Sara
```

> The exact `activity.log` output can contain previous entries if the program has been run multiple times because Exercise 6 intentionally uses append mode.

---

## Part 3 — Exercises 7–8

```text
============================================================
EXERCISE 7: WRITE A LIST TO A FILE
============================================================
Names saved successfully.

File content:
Sara
نورة
Ali

============================================================
EXERCISE 8: FINAL FILE PRACTICE
============================================================
Students:
- Sara
- نورة
- Ali
- Omar

Total students: 4

============================================================
ALL FILE HANDLING EXERCISES COMPLETED
============================================================
```

---

# 🎯 Learning Goals

After completing these exercises, you should understand how to:

* Use `Path`
* Create directories
* Check files and directories
* Open files safely with `with`
* Read complete files
* Read files line by line
* Write files
* Append to files
* Use different file modes
* Work with file names and extensions
* Store lists in text files
* Handle Unicode text
* Build simple file-based programs

---

# 🔑 Important Concepts

### `Path`

```python
from pathlib import Path

path = Path("students.txt")
```

### Read

```python
path.read_text(encoding="utf-8")
```

### Write

```python
path.write_text("Hello", encoding="utf-8")
```

### Open

```python
with path.open("r", encoding="utf-8") as file:
    content = file.read()
```

### Create a Directory

```python
Path("data").mkdir(exist_ok=True)
```

### Check Existence

```python
path.exists()
```

### File Extension

```python
path.suffix
```

### File Name

```python
path.name
```

---

# 🏁 Completion

```text
Exercise 1  ✅
Exercise 2  ✅
Exercise 3  ✅
Exercise 4  ✅
Exercise 5  ✅
Exercise 6  ✅
Exercise 7  ✅
Exercise 8  ✅
```

**Python File Handling — Completed ✅**
