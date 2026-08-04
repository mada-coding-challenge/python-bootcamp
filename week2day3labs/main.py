# description = input("introduce yourself: ")

# height = int(input("enter your height "))

# weight = int(input("enter your weight "))

# bmi = weight / (height/100 ** 2)

# if bmi < 18.5:
#     print("You are underweight.")
# elif 18.5 <= bmi < 24.9:
#     print("You have a normal weight.")
# else:
#     print("You are obese.")


# print(f""" Your first word: {description.split(" ")[0]} 

# try slice {description[0:5:2]} my intrudction in capitle is {description.upper()} 

# you must know that [0 , 5] is [0, 5] is {[0 , 5] is [0, 5]} while [0 , 5] == [0, 5] {[0 , 5] == [0, 5]}""")

#Lab1

results = 10 + 5 * 2 - 4 /2
print("results:", results)

#Lab2
total_items = 17
box_capacity = 5

full_boxes = total_items // box_capacity
remaining_items = total_items % box_capacity
# print("full_boxes:", full_boxes)
# print("remaining_items:", remaining_items)

#Lab3

base_calc = 2 + 3 * 2 **2
gcalc = (2 + 3 )* (2 **2)
print("base_calc:", base_calc)
print("gcalc:", gcalc)

#Lab4
user_age = 25
has_prermission = True


is_eligible = (user_age >= 18 and has_prermission)

print("is_eligible:", is_eligible)

#Lab5

score = 10

score += 5
score *=5
print("final score:", score)

#Lab6

memberships = ["Admin", "Moderator", "Member"]

current_membership = "Admin" 

if current_membership in memberships:
    print("You have access to the system.")
else:
    print("Go Home.")

#Lab7

sentence = "Python web development."

new_sentence = sentence.find("Python")
print("new_sentence:", new_sentence)

print("Python" in sentence)
#give us start index of the word "Python" in the sentence. If the word is not found, it will return -1.

#Lab8

message = "Python programming"

first_char = message[0]
last_char = message[-1]
print("first_char:", first_char , "last_char:", last_char)
slicing = message[0:6]
print(slicing)

#Lab9

my_email = "    mada@g.com   "
clean_email = my_email.strip().lower()
print("clean_email:", clean_email)
message = "python is a powerful programming language."
title_case_message = message.title()
print("title_case_message:", title_case_message)

#Lab10

csv_text = "apple,banana,cherry,grape"
fruits_list = csv_text.split(",")
print("fruits_list:", fruits_list)

joined_fruits = "-".join(fruits_list)
print("joined_fruits:", joined_fruits)

#Lab11

name = "Khaled"
try:
    name[0]= "A"
except TypeError as e:
    print(e)

x = 5
y = 5
if x is y:
    print("x and y are the same object in memory.")
else:
    print("x and y are different objects in memory.")

print(id(x), id(y))