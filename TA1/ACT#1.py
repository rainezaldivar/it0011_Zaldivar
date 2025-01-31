vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
spaces = " "

vowel_count = 0
consonant_count = 0
space_count = 0
other_count = 0

input_string = input("Enter some random words: ")

for char in input_string:
    if char in vowels:
        vowel_count += 1
    elif char in consonants:
        consonant_count += 1
    elif char in spaces:
        space_count += 1
    else:
        other_count += 1

print("Number of Vowels:", vowel_count)
print("Number of Consonants:", consonant_count)
print("Number of Spaces:", space_count)
print("Other Characters:", other_count)