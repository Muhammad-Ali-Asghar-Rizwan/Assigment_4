import random

def print_random_numbers():
    for i in range(10):
        value = random.randint(1, 100)
        print(value, end=' ')

# Function ko call karna
print_random_numbers()
# Output: 10 random numbers between 1 and 100 will be printed in a single line.
