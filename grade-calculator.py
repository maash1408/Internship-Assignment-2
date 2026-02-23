# Ask user for marks in 5 subjects(out of 100 each)
marks = []

for i in range(1, 6):
    mark = int(input(f"Enter marks for Subject {i} (out of 100): "))
    marks.append(mark)

# Calculations
total = sum(marks)
percentage = total / 5

# Grade Calculation
if 90 <= percentage <= 100:
    grade = "A+ (Outstanding)"
elif 80 <= percentage < 90:
    grade = "A (Excellent)"
elif 70 <= percentage < 80:
    grade = "B (Good)"
elif 60 <= percentage < 70:
    grade = "C (Average)"
elif 50 <= percentage < 60:
    grade = "D (Pass)"
else:
    grade = "F (Fail)"

# Pass/Fail Condition
if all(mark >= 40 for mark in marks):
    result = "Pass"
else:
    result = "Fail"


print("=== RESULT SUMMARY ===")
for i in range(5):
    print("Subject", i+1, ":", marks[i])

print("Total Marks(out of 500):", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("Result:", result)