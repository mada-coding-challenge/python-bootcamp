# ============================================================
#                 PYTHON OOP EXERCISES
# ============================================================


# ============================================================
#                     EXERCISE 1
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 1: STUDENT ATTRIBUTES")
print("=" * 60)

print("""
Task:
Create a Student class with:
- name
- score

Create Sara with score 92.
Create Omar with score 81.
Change Sara's score to 95.
Print both scores.
""")

print("Output:")

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score


sara = Student("Sara", 92)
omar = Student("Omar", 81)

sara.score = 95

print(sara.score)
print(omar.score)


# ============================================================
#                     EXERCISE 2
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 2: CLASS ATTRIBUTE")
print("=" * 60)

print("""
Task:
Create a Student class with a class attribute:
academy = "Tuwaiq Academy"

Create Sara.
Print the academy using the class.
Print the academy using the object.
""")

print("Output:")

class Student:
    academy = "Tuwaiq Academy"

    def __init__(self, name):
        self.name = name


sara = Student("Sara")

print(Student.academy)
print(sara.academy)


# ============================================================
#                     EXERCISE 3
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 3: STUDENT METHOD")
print("=" * 60)

print("""
Task:
Create a Student class with:
- name
- score
- display_result()

display_result() should print the student's
name and score.
""")

print("Output:")

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def display_result(self):
        print(self.name, self.score)


student = Student("Lina", 88)

student.display_result()


# ============================================================
#                     EXERCISE 4
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 4: COUNTER")
print("=" * 60)

print("""
Task:
Create a Counter class.

The counter should:
- Start with value = 0
- Have an increment() method
- Increase by 1 each time increment() is called

Call increment() twice.
Print the value.
""")

print("Output:")

class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1


counter = Counter()

counter.increment()
counter.increment()

print(counter.value)


# ============================================================
#                     EXERCISE 5
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 5: RECTANGLE")
print("=" * 60)

print("""
Task:
Create a Rectangle class with:
- width
- height
- area()

area() should return:

width * height
""")

print("Output:")

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


rectangle = Rectangle(5, 3)

print(rectangle.area())


# ============================================================
#                     EXERCISE 6
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 6: BANK ACCOUNT")
print("=" * 60)

print("""
Task:
Create a BankAccount class.

The class should have:
- balance
- withdraw(amount)

withdraw() should:
- Return False for invalid amounts.
- Return False if there is not enough money.
- Subtract valid withdrawals.
- Return True for successful withdrawals.
""")

print("Output:")

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            return False

        self.balance -= amount
        return True


account = BankAccount(500)

print(account.withdraw(200))
print(account.balance)


# ============================================================
#                     EXERCISE 7
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 7: __str__ METHOD")
print("=" * 60)

print("""
Task:
Create a Student class with:
- name
- score
- __str__()

__str__() should return:

Name: Score
""")

print("Output:")

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return f"{self.name}: {self.score}"


student = Student("Sara", 95)

print(student)


# ============================================================
#                     EXERCISE 8
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 8: INDEPENDENT OBJECTS")
print("=" * 60)

print("""
Task:
Create two Counter objects.

Increment only the first counter.
Print both counter values.
""")

print("Output:")

class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1


first = Counter()
second = Counter()

first.increment()

print(first.value)
print(second.value)


# ============================================================
#                     EXERCISE 9
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 9: STUDENTS AND LOOPS")
print("=" * 60)

print("""
Task:
Create a Student class with:
- name
- greet()

greet() should return:

Hello, <name>

Create:
- Sara
- Omar
- Lina

Store them in a list and print their greetings.
""")

print("Output:")

class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}"


students = [
    Student("Sara"),
    Student("Omar"),
    Student("Lina")
]

for student in students:
    print(student.greet())


# ============================================================
#                     EXERCISE 10
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 10: TYPE AND INSTANCE")
print("=" * 60)

print("""
Task:
Create an empty Student class.

Create a Student object.

Print:
- type(student)
- type(student) is Student
- isinstance(student, Student)
""")

print("Output:")

class Student:
    pass


student = Student()

print(type(student))
print(type(student) is Student)
print(isinstance(student, Student))


# ============================================================
#                     EXERCISE 11
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 11: PROTECTED ATTRIBUTE")
print("=" * 60)

print("""
Task:
Create a Student class with:
- name
- _score

Create Sara with a score of 95.
Print the name and score.
""")

print("Output:")

class Student:
    def __init__(self, name, score):
        self.name = name
        self._score = score


student = Student("Sara", 95)

print(student.name)
print(student._score)


# ============================================================
#                     EXERCISE 12
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 12: STUDENT SCORES")
print("=" * 60)

print("""
Task:
Create a Student class with:
- name
- scores
- average()
- add_score(score)

average() should return the average.

add_score() should only accept
scores between 0 and 100.

Create Sara with:
[80, 90]

Add 100.
Print the name and average.
""")

print("Output:")

class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def average(self):
        return sum(self.scores) / len(self.scores)

    def add_score(self, score):
        if 0 <= score <= 100:
            self.scores.append(score)


student = Student("Sara", [80, 90])

student.add_score(100)

print(student.name)
print(student.average())


# ============================================================
#                     EXERCISE 13
#                     FINAL LAB
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 13: FINAL LAB - DOG")
print("=" * 60)

print("""
Task:
Create a Dog class with:
- name
- legs
- get_legs()
- set_legs(number)

Every dog should start with 4 legs.

Create a dog named Slugi.
Change its legs to 3.
Print the number of legs.
""")

print("Output:")

class Dog:
    def __init__(self, name):
        self.name = name
        self._legs = 4

    def get_legs(self):
        return self._legs

    def set_legs(self, number):
        self._legs = number


myDog = Dog("Slugi")

myDog.set_legs(3)

print(myDog.get_legs())


# ============================================================
#                     END OF EXERCISES
# ============================================================

print("\n" + "=" * 60)
print("ALL EXERCISES COMPLETED")
print("=" * 60)