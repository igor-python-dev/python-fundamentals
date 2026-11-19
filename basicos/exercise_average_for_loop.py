total = 0
number_count = int(input("How many numbers do you want to enter? "))

for i in range(number_count):
    num = int(input(f"Enter number {i + 1}: "))
    total += num
    
average = total / number_count

print(f"\nTotal: {total}")
print(f"Average: {average}")