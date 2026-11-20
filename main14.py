

import random
import math

print("===== RANDOM FUN CALCULATOR =====")

lucky_number = random.randint(1, 10)
print("Your lucky number is:", lucky_number)


fun_choices = ["Play a game", "Solve a puzzle", "Read a story", "Draw something"]
random_activity = random.choice(fun_choices)
print("Random activity for today:", random_activity)
=number from 1 to 5!")
secret_number = random.randint(1, 5)

while True:
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("Correct! You guessed the number.")
        break
    else:
        print("Wrong guess. Try again!")


decimal_number = float(input("\nEnter a decimal number: "))