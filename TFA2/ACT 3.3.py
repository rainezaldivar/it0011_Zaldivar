lname = input("Enter your Last Name: ")
fname = input("Enter your First Name: ")
age = input("Enter your Age: ")
num = input("Enter your Contact Number: ")
course = input("What is your Course: ")

persoinfo  =  f"Reading Students Info: Last Name: {lname}\nFirst Name: {fname}\nAge: {age}\nContact Number: {num}\nCourse: {course}\n"

with open("students.txt", "a") as file:
    file.write(persoinfo)

print("Student information has been saved to 'students.txt'\n")

with open("students.txt", "r") as file:
    print(file.read())