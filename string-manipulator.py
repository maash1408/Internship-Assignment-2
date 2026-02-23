# Asking user for a sentence
sentence = input("Enter a sentence: ")

# Calculations
original = sentence
char_with_spaces = len(sentence)
char_without_spaces = len(sentence.replace(" ",""))

words = sentence.split()
total_words = len(words)
uppercase = sentence.upper()
lowercase = sentence.lower()
title_case = sentence.title()
first_word = words[0] if total_words > 0 else ""
last_word = words[-1] if total_words > 0 else ""
reversed_sentence = sentence[::-1]

print("Original: ",original)
print("Characters (with spaces):",char_with_spaces)
print("Characters (without spaces): ",char_without_spaces)
print("Words: ",total_words)
print("UPPERCASE: ",uppercase)
print("lowercase: ",lowercase)
print("First word: ",first_word)
print("Last word: ",last_word)
print("Reversed: ",reversed_sentence)