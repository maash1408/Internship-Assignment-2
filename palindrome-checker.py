text = input("Enter a word or number: ")

original = text
reversed_text = text[::-1]

print("\nOriginal:", original)
print("Reversed:", reversed_text)

if original.lower() == reversed_text.lower():
    print("Result: PALINDROME")
else:
    print("Result: NOT A PALINDROME")

print("Checking...")
print(original.lower(), "==", reversed_text.lower())