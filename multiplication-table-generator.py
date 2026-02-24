num = int(input("Enter a number: "))
end = int(input("Enter range (end): "))

print(f"\nMultiplication Table of {num}\n")

for i in range(1, end + 1):
    print(f"{num} x {i} = {num * i}")

# for i in range(1, 11):
#   for j in range(1, 11):
#        print(f"{i*j:4}", end=" ")
#    print()