revenue = 18500
expenses = {
    "Rent": 2500,
    "Wages": 6200,
    "Electricity": 450,
    "Marketing": 850,
    "Transport": 600,
    "Office Supplies": 200
}

print("------ ======== MONTHLY ANALYSIS REPORT ========")
print("")

for name, amount in expenses.items():
    print(f"- {name} - ${amount:,.2f}")

print(f"\nMonthly Revenue: ${revenue}")

total_expenses = sum(expenses.values())
print(f"\nTotal Expenses: ${total_expenses:,.2f}")

business_profit = revenue - total_expenses
print(f"Business Profit: ${business_profit:,.2f}")

if revenue > 0:
    profit_margin = (business_profit / revenue) * 100
    print(f"Profit Margin: {profit_margin:.2f}%")
else:
    print("Profit Margin: N/A (no revenue)")





