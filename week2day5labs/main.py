#Lab1
rangeNums = int(input("Enter number: "))

evenCount = 0
for number in range(1, rangeNums + 1):
    if number % 2 == 0:
        print(f"{number} is even")
        evenCount += 1
    else:
        print(f"{number} is odd")

print(f"Total even numbers: {evenCount} And total is {rangeNums}")

#Lab1
for number in range(3):
    print(f"Attempt: {number + 1}")

#lab2

for num in range(2 , 11 , 2):
    print(num)

#lab3
for secnndsToLaunch in range(10, 0, -1):
    print(f"T-:{secnndsToLaunch}")  

#lab4

course = "Python"
for letter in course:
    print(letter)


#lab 5
students = ["sara", "Shahad" , "Khadija"]

for student in students:
    print(f"Progressing student is:{student}")

