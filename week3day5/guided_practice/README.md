
# Guided Practice — Student Score Report

## Task

Create a student score-report program using Python intermediate techniques.

The program should:

1. Create a list of student dictionaries with names and nested score lists.
2. Use a list comprehension to calculate each student's average.
3. Filter the report to keep only students whose average is at least 60.
4. Build a dictionary index that maps each student name to the report record.
5. Create an independent backup using `deepcopy`, then prove that nested changes stay separate.

## Solution

```python
from copy import deepcopy

students = [
    {"name": "Sara", "scores": [40, 50, 80]},
    {"name": "Omar", "scores": [90, 70, 60]}
]

students_avrg = [
    {
        "name": student["name"],
        "scores": student["scores"],
        "avrg": round(sum(student["scores"]) / len(student["scores"]), 2)
    }
    for student in students
]

averaged_students = [
    student
    for student in students_avrg
    if student["avrg"] >= 60
]

reported_student = {
    student["name"]: student
    for student in averaged_students
}

print(reported_student)

clone = deepcopy(reported_student)

# Change a nested value in the original
reported_student["Omar"]["scores"][0] = 100

print("Original:", reported_student)
print("Backup:", clone)
````

## Explanation

### 1. Student data

The `students` list contains dictionaries. Each dictionary has a name and a nested list of scores.

```python
students = [
    {"name": "Sara", "scores": [40, 50, 80]},
    {"name": "Omar", "scores": [90, 70, 60]}
]
```

### 2. Calculate averages

A list comprehension creates a new list containing each student's name, scores, and average.

```python
"avrg": round(sum(student["scores"]) / len(student["scores"]), 2)
```

For example, Omar's average is:

```text
(90 + 70 + 60) / 3 = 73.33
```

### 3. Filter students

Only students with an average of **60 or higher** are kept.

```python
if student["avrg"] >= 60
```

### 4. Build a dictionary index

The student's name becomes the dictionary key:

```python
reported_student = {
    student["name"]: student
    for student in averaged_students
}
```

This produces a structure like:

```python
{
    "Omar": {
        "name": "Omar",
        "scores": [90, 70, 60],
        "avrg": 73.33
    }
}
```

### 5. Deep copy

`deepcopy()` creates an independent copy, including nested lists.

```python
clone = deepcopy(reported_student)
```

If we change:

```python
reported_student["Omar"]["scores"][0] = 100
```

the original changes, but the backup stays unchanged.

This proves that `deepcopy()` keeps nested objects separate.

```
