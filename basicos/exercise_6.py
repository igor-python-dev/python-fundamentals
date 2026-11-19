secret_number = 7

print("Welcome to the Number Guessing Game!")
print()
while True:
  assume = int(input("Guess the number: "))

  if assume == secret_number:
      print("Congratulations! You got it!\n")
      print("Game over.")
      break
  else:
        print("Wrong! Try again.\n")

