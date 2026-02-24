n = int(input("Enter a number: "))

if n < 0:
    print("Factorial not defined for negative numbers")

elif n == 0:
    print("0! = 1")

else:
    fact = 1
    print(f"{n}! = ", end="")

    for i in range(n, 0, -1):
        fact *= i
        print(i, end="")

        if i != 1:
            print(" × ", end="")

    print(" =", fact)