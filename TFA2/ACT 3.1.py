fname = input("Enter your First Name: ")
lname = input("Enter your Last Name: ")
age = input("Enter your age: ")

fullname = fname + " " + lname

greetengs = """Hi, I'm {} from Las Vegas, Modelss. My age is {} years old.
We're hiring new promoshonal mowdelss, tsu work en Las Vegas, Yoowezey"""

print(" ")
print("==========================================")
print("Full Name: ", fullname)
print("Sliced Name: ", (fname[0:3]))
print("Greeting Message: ", (greetengs.format(fname, age)))
print("==========================================")