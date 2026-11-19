positive_total = 0
negative_total = 0
zero_total = 0

for i in range(5):
     numb = int(input(f"Enter number {i + 1}: "))
   
# Check the number right after it is entered
     if numb > 0:
         print("Positive number!\n")
         positive_total += 1
     elif numb < 0:
         print("Negative number!\n")
         negative_total += 1
     else:
         print("Zero!\n")
         zero_total += 1

print("------ RESULTS ------")
print("")
print(f"Positive numbers: {positive_total}")
print(f"Negative numbers: {negative_total}")
print(f"Zeros: {zero_total}")







