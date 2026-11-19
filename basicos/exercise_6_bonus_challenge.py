secret_number = 7

print("Welcome to the Number Guessing Game! *Bonus challenge with Hints* ")
print()
while True:
  assume = float(input("Guess the number: "))

  if assume == secret_number:
      print("Congratulations! You got it!\n")
      print("Game over.")
      break
  elif assume > secret_number:
       print("Too high! Try again.\n")
  else:
       print("Too low! Try again.\n")

