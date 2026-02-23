# Asking user for birth date
b_date = int(input("Enter birth date (DD): "))
b_month = int(input("Enter birth month (MM): "))
b_year = int(input("Enter birth year (YYYY): "))

# Asking user for current date
c_date = int(input("Enter current date (DD): "))
c_month = int(input("Enter current month (MM): "))
c_year = int(input("Enter current year (YYYY): "))

# Calculate age in years
age_years = c_year - b_year

# Adjust if birthday not yet occurred this year
if (c_month, c_date) < (b_month, b_date):
    age_years -= 1

# Total days calculation
total_days_birth = b_year * 365 + b_month * 30 + b_date
total_days_current = c_year * 365 + c_month * 30 + c_date

age_days_exact = total_days_current - total_days_birth

age_months = age_years * 12
age_days_approx = age_years * 365
age_hours = age_days_exact * 24
age_minutes = age_hours * 60
years_until_age_100 = 100 - age_years


print("Results:")
print("Current Age:", age_years, "years")
print("Age in months:", age_months)
print("Age in days (approx 365 days/year):", age_days_approx)
print("Age in days (exact approx):", age_days_exact)
print("Age in hours:", age_hours)
print("Age in minutes:", age_minutes)
print("Years until age 100:", years_until_age_100)