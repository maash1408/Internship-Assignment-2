# Restaurant Bill Splitting Program

# Inputs (manually assign values instead of input)
total_bill = float(input("Total bill amount: ")) 
people = int(input("Number of people: ")) 
tax_percent = float(input("Tax percentage: ")) 
tip_percent = float(input("Tip percentage: "))


subtotal = total_bill
tax_amount = subtotal * tax_percent / 100
after_tax = subtotal + tax_amount
tip_amount = after_tax * tip_percent / 100
total = after_tax + tip_amount
per_person = total / people


print("=== BILL BREAKDOWN ===")
print("Subtotal:    ₹", round(subtotal, 2))
print("Tax:", tax_percent, "%   ₹", round(tax_amount, 2))
print("After tax:   ₹", round(after_tax, 2))
print("Tip:", tip_percent, "%   ₹", round(tip_amount, 2))
print("Total:       ₹", round(total, 2))
print("Per person:  ₹", round(per_person, 2))