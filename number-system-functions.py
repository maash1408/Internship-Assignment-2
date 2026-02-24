def factorial(n):
    if n < 0:
        return "Not defined for negative numbers"
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def sum_of_digits(n):
    return sum(int(d) for d in str(abs(n)))


def reverse_number(n):
    return int(str(n)[::-1])


def is_armstrong(n):
    power = len(str(n))
    return n == sum(int(d) ** power for d in str(n))


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def is_perfect_number(n):
    if n < 1:
        return False

    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i

    return divisors_sum == n


def math_menu():

    while True:
        print("\n=== NUMBER SYSTEM MENU ===")
        print("1. Factorial")
        print("2. Prime Check")
        print("3. Fibonacci")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Armstrong Number")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect Number")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == "10":
            print("Exiting program...")
            break

        if choice in ["1", "2", "3", "4", "5", "6", "9"]:
            num = int(input("Enter a number: "))

        if choice == "1":
            print("Factorial:", factorial(num))

        elif choice == "2":
            print("Prime Number" if is_prime(num) else "Not a Prime Number")

        elif choice == "3":
            print("Fibonacci:", fibonacci(num))

        elif choice == "4":
            print("Sum of digits:", sum_of_digits(num))

        elif choice == "5":
            print("Reversed number:", reverse_number(num))

        elif choice == "6":
            print("Armstrong Number" if is_armstrong(num) else "Not an Armstrong Number")

        elif choice == "7":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("GCD:", gcd(a, b))

        elif choice == "8":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("LCM:", lcm(a, b))

        elif choice == "9":
            print("Perfect Number" if is_perfect_number(num) else "Not a Perfect Number")

        else:
            print("Invalid choice ❌")


# FUNCTION CALL
math_menu()