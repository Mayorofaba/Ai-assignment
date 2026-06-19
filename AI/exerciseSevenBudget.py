# List of 10 expenses as tuples:
# (item, budgeted_amount, actual_amount)

expenses = [
    ("Food", 30000, 40000),
    ("Transport", 20000, 18000),
    ("Data", 10000, 15000),
    ("Electricity", 15000, 15000),
    ("Books", 10000, 10000),
    ("Clothes", 60000, 70000),
    ("Entertainment", 30000, 45000),
    ("Medical", 50000,5000),
    ("Savings", 100000, 100000),
    ("Miscellaneous", 20000, 18000)
]

total_overspend = 0
total_underspend = 0

worst_item = ""
worst_percentage = 0

total_budget = 0
total_actual = 0

print("=" * 70)
print(f"{'ITEM':<15}{'BUDGET':>10}{'ACTUAL':>10}{'DIFF':>10}")
print("=" * 70)

for item, budget, actual in expenses:

    difference = actual - budget

    total_budget += budget
    total_actual += actual

    if difference > 0:
        total_overspend += difference

        percentage = (difference / budget) * 100

        if percentage > worst_percentage:
            worst_percentage = percentage
            worst_item = item

    elif difference < 0:
        total_underspend += abs(difference)

    print(f"{item:<15}{budget:>10.2f}{actual:>10.2f}{difference:>10.2f}")

# Budget efficiency
efficiency = (total_budget / total_actual) * 100

print("=" * 60)
print(f"Total Budget:          {total_budget:.2f}")
print(f"Total Actual:          {total_actual:.2f}")
print(f"Total Overspend:       {total_overspend:.2f}")
print(f"Total Underspend:      {total_underspend:.2f}")
print(f"Worst Over-budget:     {worst_item}")
print(f"Over-budget Percent:   {worst_percentage:.2f}%")
print(f"Budget Efficiency:     {efficiency:.2f}%")
print("=" * 60)