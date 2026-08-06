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

#lab 6

for number in range(1 , 11):
    if number % 2 ==0:
        print(f"{number} is odd")
    print("-------")
    

#lab 7

numbers = [4 , 7 , 10 , 13 , 16 , 21]
even_counter = 0

for num in numbers:
    if num % 2 ==0:
        even_counter += 1

print(f"Total eb=ven numbers is:{even_counter}")

# lab 8

prices = [25 ,30 ,55 ,60]
total = 0

for price in prices:
    total += price

print(f"Your total is {total} VAT: {total * (15/100):.2f} ")

# lab 9

count = 1

while count < 5:
    count += 1
    print(f"Count . . .{count}")
print("Loop completed")

# lab 10
message = "Please enter your age: "
age_text = input(message).strip()

while not age_text.isdigit():
     age_text = input(message).strip()

age = int(age_text)
print(f"You are: {age}")

# lab 11

password = "python123"
print("Enter Your Passwor")
while password != "":
    password = input("Enter Your Passwor")

