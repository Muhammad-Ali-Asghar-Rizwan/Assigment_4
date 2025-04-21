import math


def main():
    """
    Calculate the length of the hypotenuse of a right triangle.
    """
    # Get the lengths of the two sides from the user
    side_a: float = float(input("Enter length of side A: "))
    side_b: float = float(input("Enter length of side B: "))

    # Calculate the length of the hypotenuse using Pythagorean theorem
    hypotenuse: float = math.sqrt(side_a ** 2 + side_b ** 2)

    # Display the result
    print("The length of the hypotenuse is:", hypotenuse)
    
    
    