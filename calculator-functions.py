# Functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def modulus(a, b):
    if b == 0:
        return "Undefined"
    return a % b

def power(a, b):
    return a ** b


# Main calculator function
def calculator():

    while True:
        print("=== CALCULATOR ===")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "7":
            print("Exiting calculator...")
            break

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", add(a, b))

        elif choice == "2":
            print("Result:", subtract(a, b))

        elif choice == "3":
            print("Result:", multiply(a, b))

        elif choice == "4":
            print("Result:", divide(a, b))

        elif choice == "5":
            print("Result:", modulus(a, b))

        elif choice == "6":
            print("Result:", power(a, b))

        else:
            print("Invalid choice")


# Function call
calculator()