# Asking user for two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Performing operations
addition = a+b
subtraction = a-b
multiplication = a*b
division = a/b
modulus = a%b
exponentiation = a**b

print(f"{int(a)} + {int(b)} = {addition}")
print(f"{int(a)} - {int(b)} = {subtraction}")
print(f"{int(a)} * {int(b)} = {multiplication}")
print(f"{int(a)} / {int(b)} = {round(division,2)}")
print(f"{int(a)} % {int(b)} = {modulus}")
print(f"{int(a)} ** {int(b)} = {exponentiation}")