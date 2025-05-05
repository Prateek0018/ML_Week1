import random

secret = random.randint(1, 50)
attempts = 5

print("Guess the number between 1 and 50. You have 5 attempts.")

for i in range(1, attempts + 1):
    guess_input = input(f"Attempt {i}: ")

    if not guess_input.isdigit():
        print("Invalid input! Please enter a number.")
        continue

    guess = int(guess_input)

    if guess == secret:
        print("Correct! You guessed the number.")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")
else:
    print(f"Out of attempts! The correct number was {secret}.")
