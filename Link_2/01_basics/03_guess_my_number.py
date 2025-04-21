# Gussing game 

import random


def guess_my_number():
    print("Welcome to the Guess My Number game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Initialize the number of attempts
    attempts = 0
    
    while True:
        # Get the user's guess
        guess = int(input("Take a guess: "))
        attempts += 1
        
        # Check if the guess is correct, too low, or too high
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
            break


if __name__ == "__main__":
    guess_my_number()
