# Movie Ticket Pricing System

# Inputs
age = int(input("Age: "))
day = input("Day of week: ").strip().lower()
tickets = int(input("Number of tickets: "))

# Age-based Pricing
if age < 3:
    base_price = 0
    category = "Free"
elif 3 <= age <= 12:
    base_price = 150
    category = "Child"
elif 13 <= age <= 59:
    base_price = 300
    category = "Adult"
else:
    base_price = 200
    category = "Senior"

# Day-based Discount
if day in ["friday", "saturday", "sunday"]:
    discount_percent = 20
else:
    discount_percent = 0

# Calculations
discount_amount = base_price * (discount_percent / 100)
price_after_discount = base_price - discount_amount
total_amount = price_after_discount * tickets

# Display
print("\n=== TICKET SUMMARY ===")
print("Category:", category)
print("Base Price: ₹", base_price)
print("Discount(if any):", discount_percent, "%")
print("Price After Discount: ₹", price_after_discount)
print("Number of Tickets:", tickets)
print("Total Amount: ₹", total_amount)