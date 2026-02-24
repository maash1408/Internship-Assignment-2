n = int(input("How many numbers do you want to enter? "))

total = 0

# Take first number to initialize max and min
num = float(input("Enter number 1: "))
total += num
maximum = num
minimum = num

# Loop for remaining numbers
for i in range(2, n + 1):
    num = float(input(f"Enter number {i}: "))
    total += num

    if num > maximum:
        maximum = num

    if num < minimum:
        minimum = num

average = total / n


print("=== RESULTS ===")
print("Sum:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)

if n <= 0:
    print("Invalid count")