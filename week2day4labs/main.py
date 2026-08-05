name = input("enter your name: ")
if(name):
    print("Name: ", name)
else:
    print("Name is required.")
score = input("enter your score: ")
if(score.isdigit() and 0 <= int(score) <= 100):
    print("Score: ", score)
    score=int(score)  # Convert score to integer for comparison
    #Lab3
    if score >= 90:
       print("Grade: A")
    elif score >= 80:
       print("Grade: B")
    elif score >= 70:
       print("Grade: C")
    elif score >= 60:
       print("Grade: D")
    else:
       print("Grade: F")
else:
    print("Score must be a number between 0 and 100.")  

choice = input("Choose Your course (Python , Java, or C++): ").upper()
match choice:
    case "PYTHON":
        print("Course: ", choice)
    case "JAVA":
        print("Course: ", choice)
    case "C++":
        print("Course: ", choice)
    case _:
        print("Invalid course selection. Please choose Python, Java, or C++.")

# Lab1

age = 20
if 18 <= age <=50:
    print("Age is between 18 and 50.")

print("code completed")

#Lab4

is_active = True
is_verified = True
role="admin"
is_blocked=False

if is_active and is_verified:
    print("account is ready to use")

if role == "admin" or role == "moderator":
    print("You can edit content.")

if not is_blocked:
    print("You can access the account.")

else:
    print("Account is blocked. Please contact support.")

# Lab 5
account_active = True
has_permission = False

if account_active:
    if has_permission:
        print("access granted")
    else:
        print("access denied")

else:
    print("account is inactive")

# Lab 6
name
cart = []
balance = 0

if name:
    print("name has a value")

if not cart:
    print("cart is empty")
print(bool(balance))  # False, since balance is 0

# lab 7

name = input("Enter your name: ").strip()

if not name:
    print("Name is required.")
elif not name.replace(" ", "").isalpha():
    print("Name must contain only letters and spaces.")
else:
    print("Name is valid.")

#lab 8
age_text = input("Enter your age: ").strip();

if age_text.isdigit():
    age = int(age_text)
    print(f"You will be {age + 5} years old in 5 years.")
else:
    print("Invalid age. Please enter a valid number.")

# Lab 9

score_text = input('Enter a number between 0 and 100: ')

if score_text.isdigit():
    score_x = int(score_text)
    if 0 <= score_x and score_x <= 100:
        print("Valid score.")
    else:
        print("Score must be between 0 and 100.")

# lab 10

membership = ["Admin", "Viewer", "Editor"]

current_membership = input("Enter your membership").strip().lower()
print(current_membership.title())
if current_membership.title() in membership:
    print("You are allowed to view the content.") 
    print(current_membership.title())
else:
    print("Please contact the admin team.")

#lab 11

command = input("Please enter a command (start , stop , status): ").strip().lower()

match command:
    case "start":
        print("System is starting...")
    case "stop":
        print("System is stopping...")
    case "status":
        print("System status: Running")
    case _:
        print("Please enter proper command")