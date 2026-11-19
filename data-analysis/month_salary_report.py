employees = {
    "John": 4500,
    "Sarah": 5200,
    "Michael": 3800,
    "Emma": 6100,
    "David": 4900
}
print("------ EMPLOYEES SALARY REPORT ------")
print("")
for name, amount in employees.items():
    print(f"{name} - ${amount:,.2f}")

total_salaries = sum(employees.values())
print(f"\nTotal Salary Expenditure: ${total_salaries:,.2f}")

average_salary = total_salaries / len(employees.values())
print(f"Average Salary: ${average_salary:,.2f}")

highest_employee = ""
highest_amount = 0
for name, amount in employees.items():
    if amount > highest_amount:
      highest_amount = amount
      highest_employee = name
print(f"\nHighest Salary: ${highest_amount:,.2f} from {highest_employee}.")

lowest_employee = ""
lowest_amount = None

for name, amount in employees.items():
    if lowest_amount is None or amount < lowest_amount:
       lowest_amount = amount
       lowest_employee = name
print(f"Lowest Salary: ${lowest_amount:,.2f} from {lowest_employee}.")

#count how many employees earn more than $4.500
count = 0
for name in employees:
    if employees[name] > 4500:
        count += 1
print(f"\n{count} employees earn more than $4500 dollars.")
print("------ EMPLOYEES ABOVE $4,500 ------")
print("")
for name, amount in employees.items():
    if amount > 4500:
        print(f"{name} - ${amount:,.2f}")

print(f"\nTotal employees found: {count}")





