def unique_word_counter(text):
    skip_words = {"and", "but", "or", "nor", "for", "so", "yet", "a", "an", "the", "of"}
    
    words = text.split()
    word_freq = {}
    
    for word in words:
        lower_word = word.lower()
        if lower_word not in skip_words:
            word_freq[word] = word_freq.get(word, 0) + 1
    
    lowercase_entries = {w: c for w, c in word_freq.items() if w.islower()}
    capitalized_entries = {w: c for w, c in word_freq.items() if w.istitle() or w.isupper()}
    
    for w, c in sorted(lowercase_entries.items()):
        print(f"{w:<12} - {c}")
    for w, c in sorted(capitalized_entries.items()):
        print(f"{w:<12} - {c}")
    print ("")
    print(f"TOTAL WORDS COUNTED: {sum(word_freq.values())}")

print("==================================================")
print("                UNIQUE WORD COUNTER               ")
print("==================================================")
print ("")
user_input = input("Enter a string statement: ")
print ("")
unique_word_counter(user_input)

