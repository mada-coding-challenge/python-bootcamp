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