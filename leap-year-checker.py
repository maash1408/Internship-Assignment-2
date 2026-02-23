# Leap Year Checker Program

year = int(input("Enter a year: "))

# Check leap year condition
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    is_leap = True
else:
    is_leap = False

# Display result with reason
print("=== RESULT ===")
print("Year:", year)

if is_leap:
    if year % 400 == 0:
        reason = "Divisible by 400 (which automatically makes it a leap year)."
    elif year % 100 == 0:
        reason = "Divisible by 100 but also divisible by 400."
    else:
        reason = "Divisible by 4 and not divisible by 100."
    
    print("Leap Year: YES")
    print("Reason:", reason)

else:
    if year % 4 != 0:
        reason = "Not divisible by 4."
    elif year % 100 == 0 and year % 400 != 0:
        reason = "Divisible by 100 but NOT divisible by 400."
    else:
        reason = "Does not meet leap year conditions."
    
    print("Leap Year: NO")
    print("Reason:", reason)