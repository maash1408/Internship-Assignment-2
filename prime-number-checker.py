# Part 1 : Check if a single number is prime. Handle negative numbers, 0, 1, and 2. 
num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is NOT a prime number")

else:
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, "is a PRIME number")
    else:
        print(num, "is NOT a prime number")

# Part 2 : Find all prime numbers in a given range. 

start = int(input("Enter start range: "))
end = int(input("Enter end range: "))

print("Prime numbers are:")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num, end=" ")