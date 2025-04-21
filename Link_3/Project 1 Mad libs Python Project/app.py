# Project 1: Mad libs Python Project

def  mad_libs():
    print("Welcome to the Mad Libs Game!")
    print("Fill in the blanks to create a funny story.")

    # Get user inputs
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb: ")
    adjective1 = input("Enter an adjective: ")
    adverb1 = input("Enter an adverb: ")

    # Create the story
    story = f"Once upon a time, there was a {adjective1} {noun1} that loved to {verb1} {adverb1}."
    
    # Print the story
    print("\nHere's your Mad Libs story:")
    print(story)



if __name__ == "__main__":    
    mad_libs()