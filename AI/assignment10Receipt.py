# creating a list of tuples frm my last supermarket trip (item_name, quantity, unit_price, category)
receipt = [ 
    ("Milk", 2, 150.00, "Food"),
    ("Bread", 1, 100.00, "Food"),
    ("Eggs", 12, 20.00, "Food"),
    ("Hair dye", 1, 6000.00, "Non-Food"),
    ("Soap", 3, 200.00, "Non-Food"),
    ("gala", 5, 500.00, "Food"),
    ("Detergent", 2, 3000.00, "Non-Food")
]   
# Initialize variables for totals and category tracking
category_totals = {}        
grand_total = 0.0   
unique_categories = set()

for item in receipt:
    item_name, quantity, unit_price, category = item
    subtotal = quantity * unit_price
    grand_total += subtotal
    unique_categories.add(category)

    if category not in category_totals:
        category_totals[category] = 0
    category_totals[category] += subtotal

# Apply 7.5% VAT only to non-food items
vat_total = 0.0
for category, total in category_totals.items():
    if category != "Food":
        vat_total += total * 0.075

# Print the formatted receipt
print("Supermarket Receipt")
print("=" * 40)
for item in receipt:
    item_name, quantity, unit_price, category = item
    subtotal = quantity * unit_price
    print(f"{item_name:<15} {quantity:>3} {unit_price:>10.2f} {subtotal:>10.2f}")

print("=" * 40)
for category, total in category_totals.items():
    print(f"{category}: ₦{total:>10.2f}")
print(f"Grand Total (without tax): ₦{grand_total:>10.2f}")
print(f"VAT (7.5%): ₦{vat_total:>10.2f}")
print(f"Grand Total (with tax): ₦{grand_total + vat_total:>10.2f}")

