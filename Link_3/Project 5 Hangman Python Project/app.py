# Project 5: Hangman Python Project
import random



def hangman():

    # List of words to choose from
    words = ["python", "hangman", "programming", "challenge", "computer"]
    word_to_guess = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")

    while attempts > 0:
        # Display the current state of the word
        display_word = "".join([letter if letter in guessed_letters else "_" for letter in word_to_guess])
        print(f"\nWord: {display_word}")
        print(f"Attempts left: {attempts}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")

        # Get user input
        guess = input("Enter a letter: ").lower()

        # Validate user input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Good guess!")
        else:
            print("Wrong guess!")
            attempts -= 1

        if all(letter in guessed_letters for letter in word_to_guess):
            print(f"\nCongratulations! You've guessed the word: {word_to_guess}")
            break
    else:
        print(f"\nGame over! The word was: {word_to_guess}")



if __name__ == "__main__":
    hangman() 
    
            