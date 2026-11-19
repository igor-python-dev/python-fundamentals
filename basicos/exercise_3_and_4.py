import time

number = int(input("Enter a number: "))

if number % 2 == 0:
  print(f"{number} is even.")
else:
  print(f"{number} is odd.")
  
#Pause for 2 seconds, then print the transition message  
time.sleep(2)
print("\nNice! Next to another problem:")

numb1 = float(input("Enter the first number: "))
numb2 = float(input("Enter the second number: "))

calculator = input("Enter operation(+, -, *, /): ")

#check which operation was chosen
if calculator == "+":
    result = numb1 + numb2

elif calculator == "-":
    result = numb1 - numb2

elif calculator == "*":
    result = numb1 * numb2

elif calculator == "/":
    # prevent the calculator from dividing by zero
    if numb2 != 0:
      result = numb1 / numb2
    else:
      result = None 
      print("Error: Cannot divide by zero.")

else:
    result = None
    print("Invalid operator. Please choose +, -, *, /.")

if result is not None:
    print(f"Result: {result:g}")

time.sleep(2)
print("\nGreat. Thats all for now.")





