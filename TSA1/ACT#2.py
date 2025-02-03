int_string = input("Enter some Numbers: ")
total = 0

for char in int_string:
    if char.isdigit():
        total += int(char)

print("The sum of the digits is: ", total)
