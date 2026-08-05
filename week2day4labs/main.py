name = input("enter your name: ")
if(name):
    print("Name: ", name)
else:
    print("Name is required.")
score = input("enter your score: ")
if(score.isdigit() and 0 <= int(score) <= 100):
    print("Score: ", score)
    score=int(score)  # Convert score to integer for comparison
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
if choice in ["PYTHON", "JAVA", "C++"]:
    print("Course: ", choice)
else:
    print("Invalid course selection. Please choose Python, Java, or C++.")
