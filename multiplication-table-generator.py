num = int(input("Enter a number: "))
end = int(input("Enter range (end): "))

print(f"Multiplicaation Table of {num}")

for i in range(1, end +1):
    print(f"{num} * {i} = {num * i}")

if end <= 0:
    print("Invalid range")