expenses = {
    "Rent": 2500,
    "Electricity": 450,
    "Internet": 120,
    "Insurance": 380,
    "Marketing": 850,
    "Transport": 600,
    "Office Supplies": 200,
    "Software": 300
}
total_expenses = sum(expenses.values())
average_expenses = total_expenses / len(expenses.values())
print("------ MONTHLY EXPENSE REPORT ------")
print("")
for name, amount in expenses.items():
    print(f"- {name}: ${amount:.2f}")

print(f"\nTotal Expenses: ${total_expenses:.2f}")
print(f"Average Expenses: ${average_expenses:.2f}")


highest_expense = ""
highest_amount = 0

for name, amount in expenses.items():
    if amount > highest_amount:
      highest_amount = amount
      highest_expense = name 
print(f"\nMost Expensive: {highest_expense}")

cheapest_expense = ""
cheapest_amount = None

for name, amount in expenses.items():
    if cheapest_amount is None or amount < cheapest_amount:
      cheapest_amount = amount
      cheapest_expense = name
print(f"Cheapest Expense: {cheapest_expense}")

expenses_above_500 = [name for name, amount in expenses.items() if amount > 500]
print(f"Categories above $500: {', '.join(expenses_above_500)}")

#Rent represents ...% of total expenses.
rent_percentage = (expenses["Rent"] / total_expenses) *100
print(f"Rent represents {rent_percentage:.1f}% of total expenses.")





