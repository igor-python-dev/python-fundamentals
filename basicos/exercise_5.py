print("Welcome to the Shopping Calculator!")
print()
name = input("Enter product name: ")
price = float(input("Enter product price: "))
units = int(input("How many units? "))

total = price * units
print()

print("------ RECEIPT ------")
print(f"Product: {name}")
print(f"Unit price: ${price:.2f}")
print(f"Quantity: {units}")
print(f"Total: ${total:.2f}")

if total > 100:
  print("You qualify for free delivery!")
print("---------------------")
print("Thank you for shopping!")

