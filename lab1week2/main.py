Student_name = "Sara"
student_name = "Abdullah"

print(Student_name)
print(student_name)



##Lab2


student_name = "Mada"
student_age = 30

course = "Python Programming"

print(f"""welcome {student_name} """)





student_name, student_age, student_is_registered = "Mada", 30, True

print(type(student_age))
print(type(student_is_registered))
print(type(student_name))

print(isinstance(student_name, str))
print(isinstance(student_age, int))

age = input("Enter your age: ")

if (isinstance(int(age), int)):
    print("You are eligible to register for the course."  )
else:
    print("You are not eligible to register for the course.")


teacher_name = "Faisal"

index = int(input("Enter the index of the character you want to access in the teacher's name: "))

if index < 0 or index >= len(teacher_name):
    print("Invalid index. Please enter a valid index.")
else:       
    print(teacher_name[index])