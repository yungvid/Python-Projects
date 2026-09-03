import random

hidden_number = random.randint(1, 100)
attempts = 0

print("-------Welcome to my Guessing game----------")
print("I have selected a number between 1 and 100. Can you guess it?")

while True:

    guess = int(input("Enter a guess: ")) # Convert user input and convert it to a whole number
    attempts += 1

    if guess < hidden_number: # Checking the guess number if it's less than hidden number
        print("Too low! Try again.")
    elif guess > hidden_number: # Checking the guess number if it's greater than hidden number
        print("Too high! Try again.")
    else: # Print if the guess number == hidden number
        print(f"Congratulations! You guessed the number {hidden_number} in {attempts} attempts.")
        break


