# Problem Statement
# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

# An example run of the program looks like this (user input is in blue):

# Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a num




def count_number():
    count_dict  = {}
    while True:
        num = input("Enter a number (or Exit to quit): ")
        if num.lower() == "exit":
            break
         
        if num.isdigit():
            num = int(num)
            count_dict[num] = count_dict.get(num, 0) + 1
        else:
            print("Invalid input. Please enter a number.")
            
            
def display_count(count_dict):
    print("\n Number counts:")
    for key, value in count_dict.items():
        print(f"{key}: {value}")
 
if __name__ == "__main__":
    count = count_number()
    display_count(count)
    
    
