# Project 4: Rock, paper, scissors Python Project


def rock_paper_scissors():
    import random

    print("Welcome to the Rock, Paper, Scissors Game!")
    print("Choose your option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    # Get user input
    user_choice = int(input("Enter your choice (1-3): "))

    # Validate user input
    if user_choice < 1 or user_choice > 3:
        print("Invalid choice! Please choose a number between 1 and 3.")
        return

    # Map user choice to string
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    user_choice_str = choices[user_choice]

    # Generate computer choice
    computer_choice = random.randint(1, 3)
    computer_choice_str = choices[computer_choice]

    print(f"\nYou chose: {user_choice_str}")
    print(f"Computer chose: {computer_choice_str}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        print("You win!")
    else:
        print("Computer wins!")



if __name__ == "__main__":
    rock_paper_scissors() 
    
           