
def calculate_subtotals(receipt):

    receipt_with_subtotals = []
    
    for item_name, quantity, unit_price, item_category in receipt:
        item_subtotal = quantity * unit_price
        receipt_with_subtotals.append((item_name, quantity, unit_price, item_category, item_subtotal))
    
    return receipt_with_subtotals


def apply_tax(receipt, food_categories):
    total_subtotal = 0
    total_tax = 0
    
    # Process each item in the receipt
    for item_name, qty, price, item_category, item_subtotal in receipt:
        total_subtotal += item_subtotal
        
        # Apply tax only to non-food items
        if item_category not in food_categories:
            tax_amount = item_subtotal * 0.075  # 7.5% VAT
            total_tax += tax_amount
    
    # Calculate grand total
    total_with_tax = total_subtotal + total_tax
    
    return total_subtotal, total_tax, total_with_tax


def find_expensive_items(receipt, threshold=5000):
    expensive_items = []
    
    for item_name, qty, price, category, item_subtotal in receipt:
        if item_subtotal >= threshold:
            expensive_items.append((item_name, qty, price, item_subtotal))
    
    return expensive_items


def get_category_stats(receipt):
    category_totals = {}
    unique_categories = set()
    
    # Sum up amounts by category
    for item_name, qty, price, item_category, item_subtotal in receipt:
        unique_categories.add(item_category)
        
        if item_category not in category_totals:
            category_totals[item_category] = 0
        
        category_totals[item_category] += item_subtotal
    
    # Find the most expensive (highest spending) category
    most_expensive_category = None
    max_category_amount = 0
    
    for category, total_amount in category_totals.items():
        if total_amount > max_category_amount:
            max_category_amount = total_amount
            most_expensive_category = category
    
    return category_totals, most_expensive_category, list(unique_categories)


def generate_receipt_report(receipt, receipt_number=1):
    # Step 1: Calculate subtotals for each item
    receipt_with_subtotals = calculate_subtotals(receipt)
    
    # Step 2: Define tax-exempt categories
    food_categories = ["Food", "Beverages", "Dairy", "Produce"]
    
    # Step 3: Calculate taxes
    total_subtotal, total_tax, total_with_tax = apply_tax(receipt_with_subtotals, food_categories)
    
    # Step 4: Find expensive items
    expensive_items = find_expensive_items(receipt_with_subtotals)
    
    # Step 5: Get category statistics
    category_totals, most_expensive_category, unique_categories = get_category_stats(receipt_with_subtotals)
    
    # Step 6: Print formatted receipt
    print("\n" + "=" * 90)
    print(f"{'SUPERMARKET RECEIPT':^90}")
    print(f"{'Receipt #' + str(receipt_number):^90}")
    print("=" * 90)
    print(f"{'Item':<30} {'Qty':>6} {'Price':>12} {'Category':<15} {'Subtotal':>12}")
    print("-" * 90)
    
    # Print each line item
    for item_name, qty, unit_price, category, subtotal in receipt_with_subtotals:
        print(f"{item_name:<30} {qty:>6} {unit_price:>12,.2f} {category:<15} {subtotal:>12,.2f}")
    
    # Print totals section
    print("-" * 90)
    print(f"{'Subtotal':<68} {total_subtotal:>12,.2f}")
    print(f"{'Tax (7.5% on non-food)':<68} {total_tax:>12,.2f}")
    print("=" * 90)
    print(f"{'TOTAL':<68} {total_with_tax:>12,.2f}")
    print("=" * 90)
    
    # Step 7: Print summary section
    print("\n" + "RECEIPT SUMMARY".center(90))
    print("-" * 90)
    
    total_items_qty = sum(qty for _, qty, _, _, _ in receipt_with_subtotals)
    print(f"Total Items Purchased:        {total_items_qty}")
    print(f"Unique Categories:            {len(unique_categories)} ({', '.join(unique_categories)})")
    print(f"Most Expensive Category:      {most_expensive_category} ({category_totals[most_expensive_category]:,.2f})")
    
    # Print category breakdown
    print("\nCategory Breakdown:")
    for category in sorted(category_totals.keys()):
        amount = category_totals[category]
        tax_indicator = "" if category in food_categories else " (Taxed 7.5%)"
        print(f"  {category:<25} {amount:>12,.2f}{tax_indicator}")
    
    # Print expensive items if any exist
    if expensive_items:
        print(f"\nExpensive Items (>5000):")
        for item_name, qty, price, subtotal in expensive_items:
            print(f"  {item_name:<25} Qty: {qty:>3} | Subtotal: {subtotal:>12,.2f}")
    
    print("=" * 90 + "\n")
    
    # Return summary data for comparisons
    return {
        "subtotal": total_subtotal,
        "tax": total_tax,
        "total": total_with_tax,
        "item_count": total_items_qty,
        "category_count": len(unique_categories)
    }


# Main program: Process and compare two shopping trips
if __name__ == "__main__":
    # ============================================================================
    # SHOPPING TRIP 1: Family Groceries
    # ============================================================================
    trip_1_items = [
        ("Milk (2L)", 2, 450, "Dairy"),
        ("Bread (Whole Wheat)", 3, 150, "Food"),
        ("Chicken Breast (1kg)", 2, 800, "Food"),
        ("Apples (1kg)", 4, 200, "Produce"),
        ("Cooking Oil (1L)", 1, 1200, "Food"),
        ("Shampoo", 2, 600, "Personal Care"),
        ("Laundry Detergent", 1, 1800, "Household"),
        ("Orange Juice (1L)", 3, 350, "Beverages"),
        ("Rice (5kg)", 1, 3000, "Food"),
        ("Coffee (500g)", 1, 2500, "Food"),
    ]
    
    # ============================================================================
    # SHOPPING TRIP 2: Home Renovation & Party Supplies
    # ============================================================================
    trip_2_items = [
        ("Paint (1L)", 5, 3500, "Hardware"),
        ("Wood Plywood (1 sheet)", 2, 8000, "Hardware"),
        ("Party Decorations", 1, 4500, "Party Supplies"),
        ("Balloons (Pack of 100)", 3, 1200, "Party Supplies"),
        ("Cake Flour (2kg)", 2, 800, "Food"),
        ("Sugar (2kg)", 3, 600, "Food"),
        ("Champagne (Bottle)", 4, 5000, "Beverages"),
        ("Light Bulbs (LED)", 6, 800, "Hardware"),
        ("Sandpaper (Assorted)", 3, 400, "Hardware"),
        ("Paper Plates (Pack of 50)", 2, 350, "Party Supplies"),
    ]
    
    # Process Trip 1
    print("\n" + "#" * 90)
    print(f"{'SHOPPING TRIP 1: FAMILY GROCERIES':^90}")
    print("#" * 90)
    trip_1_summary = generate_receipt_report(trip_1_items, receipt_number=1001)
    
    # Process Trip 2
    print("\n" + "#" * 90)
    print(f"{'SHOPPING TRIP 2: HOME RENOVATION & PARTY':^90}")
    print("#" * 90)
    trip_2_summary = generate_receipt_report(trip_2_items, receipt_number=1002)
    
    # ============================================================================
    # COMPARISON: Side-by-side analysis of both trips
    # ============================================================================
    print("\n" + "=" * 90)
    print(f"{'SHOPPING TRIPS COMPARISON':^90}")
    print("=" * 90)
    print(f"{'Metric':<35} {'Trip 1':>20} {'Trip 2':>20}")
    print("-" * 90)
    print(f"{'Subtotal':<35} {trip_1_summary['subtotal']:>20,.2f} {trip_2_summary['subtotal']:>20,.2f}")
    print(f"{'Tax (7.5%)':<35} {trip_1_summary['tax']:>20,.2f} {trip_2_summary['tax']:>20,.2f}")
    print(f"{'Total Amount Spent':<35} {trip_1_summary['total']:>20,.2f} {trip_2_summary['total']:>20,.2f}")
    print(f"{'Total Items':<35} {trip_1_summary['item_count']:>20} {trip_2_summary['item_count']:>20}")
    print(f"{'Unique Categories':<35} {trip_1_summary['category_count']:>20} {trip_2_summary['category_count']:>20}")
    print("-" * 90)
    
    # Calculate and display the difference
    spending_difference = trip_2_summary['total'] - trip_1_summary['total']
    comparison_text = "more" if spending_difference > 0 else "less"
    print(f"{'Trip 2 spent ' + comparison_text + ' than Trip 1':<35} {abs(spending_difference):>20,.2f}")
    print("=" * 90 + "\n")
